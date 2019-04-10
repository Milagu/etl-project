#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Dependencies
import requests
from requests import Session
import csv
import copy
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

def get_immunization_df():
    """
    :return Pandas dataframe
    """
    immu_url = "https://data.wa.gov/api/views/kck7-yb2v/rows.csv?accessType=DOWNLOAD"
    immunization_df = pd.read_csv(immu_url, parse_dates=True)
    immunization_df = immunization_df[['County', 'School_Year', 'Reported_enrollment', 'Number_complete_for_all_immunizations']].copy()
    immunization_df = immunization_df.rename(columns = {'County':'county', 
                                                    'School_Year':'school_year', 
                                                    'Reported_enrollment':'number_reported',
                                                    'Number_complete_for_all_immunizations':'number_completed'})
    return immunization_df

def get_county_df():
    wa_county_url = "https://data.wa.gov/api/views/tecv-qzfm/rows.csv?accessType=DOWNLOAD"
    wa_county_df = pd.read_csv(wa_county_url, parse_dates=True)
    wa_county_df = wa_county_df[['COUNTY', 'POP_2016']].copy()
    wa_county_df = wa_county_df.rename(columns = {'COUNTY':'county', 'POP_2016':'pop_2016'})
    print("a")
    return wa_county_df


