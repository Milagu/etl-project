# Enter your config elements here
data_src_list = ["https://data.wa.gov/api/views/kck7-yb2v/rows.csv?accessType=DOWNLOAD",
                 "https://data.wa.gov/api/views/tecv-qzfm/rows.csv?accessType=DOWNLOAD"]

col_list = [['County', 'School_Name', 'School_Year', 'Reported_enrollment', 'Number_complete_for_all_immunizations'],
             ['COUNTY', 'POP_2016']]
             
name_list = [{'County': 'county',
                'School_Name': 'school_name',
                'School_Year': 'school_year', 
                'Reported_enrollment': 'number_reported',
                'Number_complete_for_all_immunizations': 'number_completed'},
                {'COUNTY': 'county', 'POP_2016': 'pop_2016'}]
# Merge on variable
var_on = '[\'county\']'
# Create a dictionary with column names against a list of aggregrations.
# ***Remember, the dictionary index starts at 1 and the list index starts at 0!
# Also, having the dictionary value as a list provides the flexibility to select and apply sub-sets of aggregations of any order on
# any given dataframe's column or series.
# We can use tuples instead of list if we want the list to be immutable.
aggr_fun = {'county': ['sum']}
#"""--------------------------------"""
# Example: If we have {'county':['sum','mean', 'median', min','max','sem','count','std']}, we can select the required
# aggregations as shown below:
#"""from operator import itemgetter
#"""dict = {'county':["sum","mean","max"],2:["count","median","std"],3:["max","mean"]}
#"""myList = dict['county'] #***note that the key should match!***
#"""print(myList)
#"""my_unordered_List = itemgetter(1,2,0)(myList)
#"""print(my_unordered_List)
#"""my_selective_list = itemgetter(2,0)(myList)
#"""print(my_selective_list)
#"""-x-x-x-x-xThis produces an output as follows-x-x-x-x-x-x"""
#"""['sum', 'mean', 'max']
#"""('mean', 'max', 'sum')
#"""('max', 'sum')
#"""---------------------------------"""