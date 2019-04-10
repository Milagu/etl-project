import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="root",
  database="etl_project"
)


#=========================================
# DROP TABLES
#=========================================

print('1.  ETL_PROJECT Schema: Dropping Tables')
drop_cursor = mydb.cursor()

#order is important when dropping due to fk constraints
drop_cursor.execute('drop table if exists etl_project.county_populations')
drop_cursor.execute('drop table if exists etl_project.schools')
drop_cursor.execute('drop table if exists etl_project.counties')
drop_cursor.execute('drop table if exists etl_project.states')


#=========================================
# CREATE TABLES
#=========================================

print('------------------------')
print('2.  ETL_PROJECT Schema: Creating tables')

mycursor = mydb.cursor()

#states table
mycursor.execute \
("create table etl_project.states \
  (state_pk_id smallint(5) unsigned not null auto_increment \
  ,state_nm varchar(30) \
  ,state_abbr varchar(2) \
  ,primary key (state_pk_id)) ENGINE=InnoDB DEFAULT CHARSET=utf8");

#counties table
mycursor.execute \
("create table etl_project.counties  \
  (counties_pk_id smallint(5) not null auto_increment \
  ,state_id smallint(5) unsigned null \
  ,county_nm varchar(50) null \
  ,primary key (counties_pk_id) \
  ,constraint state_id \
    foreign key (state_id) \
    references etl_project.states (state_pk_id) \
    on delete no action \
    on update no action)");

#county_populations table
mycursor.execute \
("create table etl_project.county_populations \
  (county_pop_pk_id smallint(5) not null auto_increment \
  ,county_id smallint(5) null \
  ,year_de varchar(4) null \
  ,population_nr mediumint(10) null \
  ,primary key (county_pop_pk_id) \
  ,constraint fk_county_id \
    foreign key (county_id) \
    references etl_project.counties (counties_pk_id) \
    on delete no action \
    on update no action)");

#schools table
mycursor.execute \
("CREATE TABLE etl_project.schools \
  (school_pk_id SMALLINT(5) NOT NULL AUTO_INCREMENT \
  ,school_nm VARCHAR(100) NULL \
  ,county_id SMALLINT(5) NULL \
  ,PRIMARY KEY (school_pk_id) \
  ,INDEX fk_schools_county_id_idx (county_id ASC) \
  ,CONSTRAINT fk_schools_county_id \
    FOREIGN KEY (county_id) \
    REFERENCES etl_project.counties (counties_pk_id) \
    ON DELETE NO ACTION \
    ON UPDATE NO ACTION)");

print('------------------------')
print('--- Job Completed ---')

