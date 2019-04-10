# Dependencies
import requests
from requests import Session
import csv
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine


def extract(aList):
    ret_df = []
    # For each element in aList, download/extract
    # data into a python dataframe and return the same
    for i in range(len(aList)):
        ret_df.append(pd.read_csv(aList[i], header=None, index_col=False, sep=',', parse_dates=True))
    return ret_df