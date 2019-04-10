#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd
# PyMySQL 
pymysql.install_as_MySQLdb()
# The following code is to call one .ipynb from another
# First install ipynb using the command "pip install ipynb" from command prompt. Then include the following to start
# using your work from the other notebook (here we want to use the dataframes from our extract.ipynb)
from ipynb.fs.full.extract import *

def transform_data(immunization_df,wa_county_df):
# Drop all rows with 0's in number_reported and number_completed columns
    immunization_df = immunization_df.drop(immunization_df[(immunization_df.number_reported == 0.0) & (immunization_df.number_completed == 0.0)].index)
# Count the number of unique rows
    immunization_df['county'].nunique()


# In[29]:


# Count the number of rows with values in'em
    immunization_df.count()


# In[30]:


# The count_null indicates the existance of 'NULL' or 'NaN's in the dataset
# Let's check
    immunization_df.isna().sum()


# In[31]:


# Yet another way to count the total number of 'NULL' or 'NaN' values in the dataframe is...
    count_null = len(immunization_df) - immunization_df.count()
    count_null


# In[32]:


# Let's drop all the rows with 'NULL' or 'NaN's
    immunization_df= immunization_df.dropna()

# Confirm the removal of NULL values
    immunization_df.isna().sum()


# In[33]:


#Count the total number of records with values in the dataframe
    immunization_df.count()


# In[34]:


# Convert the content of wa_county_df column 'county' to uppercase
    wa_county_df['county'] = wa_county_df['county'].str.upper()
# Confirm the conversion
    wa_county_df.head()


# In[35]:


# Note that each county having multiple values in the wa_county_df.  We need to roll'em all up.
    wa_county_grp = wa_county_df.groupby('county').sum()
    wa_county_df = pd.DataFrame(wa_county_grp)
    wa_county_df.count()


# In[36]:


# Let's combine the two dataframes
    combined_df = pd.merge(immunization_df, wa_county_df, on='county', how='left')
    combined_df.sort_values(by='county')
    combined_df.head()


# In[37]:


# Check for NULL values in the dataframe. 'True' values indicate the presence of 'NULL' values.
    combined_df.isna().sum()


# In[38]:


# Yet another way to count the total number of 'NULL' or 'NaN' values in the dataframe is...
    count_null = len(combined_df) - combined_df.count()
    count_null


# In[39]:


# Let's drop all the rows having 'NULL' or 'NaN's.
    combined_df = combined_df.dropna()
    combined_df


# In[40]:


# Drop duplicate rows
    combined_df= combined_df.drop_duplicates(keep='first').reset_index()


# In[41]:


    combined_df.columns


# In[43]:


    combined_df = combined_df.rename(columns={'index':'id'})
    combined_df.columns

    return transformed_data




