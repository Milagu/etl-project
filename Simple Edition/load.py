#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
# ----------------------------------
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
# The following code is to call one .ipynb from another
# First install ipynb using the command "pip install ipynb" from command prompt. Then include the following to start
# using your work from the other notebook (here we want to use the dataframes from our extract.ipynb)
from ipynb.fs.full.transform import *


# In[2]:

def load_data (combined_df):
# Create Engine and Pass in MySQL Connection
    conn_str = "root:root@127.0.0.1/immunization_db"
    engine = create_engine(f'mysql://{conn_str}')


# In[3]:


# Connect
    conn = engine.connect()


# In[4]:


# Check for table(s) in the database
    engine.table_names()


# In[5]:


    combined_df.columns


# In[6]:


# Dump data from dataframe to SQL database table
    combined_df.to_sql(name='wa_immunizations', con=engine, if_exists='append', index=False)


# In[7]:


# Query All Records to confirm the load
    data = pd.read_sql("SELECT * FROM wa_immunizations", conn)
    data






