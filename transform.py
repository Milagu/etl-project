# Dependencies
import pandas as pd
import copy

import functools
from functools import reduce

# Config
import config
from config import col_list, name_list, aggr_fun, var_on

import extract
from extract import extract

# A method to merge dataframes on a given column 
# Please refer config.py on the column to merge on. The argument 'on' can also be a list.
def merge_dataframes(aList, on = config.var_on):
    merged_list = []
    if (len(aList) == 1):
        print( "Cannot combine. List has only one dataframe!")
        merged_list = copy.deepcopy(aList)
        return merged_list
    elif (len(aList) >= 2):
        for position in range(len(aList)):
            df1 = aList[position].copy()
            df2 = aList[position+1].copy()
            combined_df = reduce(lambda df1, df2  : pd.merge(df1, df2, on=config.var_on, how="left"), aList)
            merged_list = merged_list.append(combined_df)
        return merged_list

def transform(aList):
    """
    aList: list
    :return 
    """
    # Loop through the list of dataframes and perform common transformations here...
    outList = []
    for position in range(len(aList)):
        # Select the required columns into a dataframe
        temp_df = aList[position][[config.col_list[position]]].copy()
        # Rename the selected columns
        temp_df = temp_df.rename(columns = config.name_list[position])
        # Drop all rows with 0's
        temp_df = temp_df.T[temp_df.any()].T
        # Drop all rows with 'NULL' or 'NaN's
        temp_df = temp_df.dropna()
        # Convert all text columns from lowercase to uppercase
        temp_df = temp_df.apply(lambda x: x.str.upper() if(x.dtype == 'object') else x)
        # Apply aggregation on the dataframes using the config variable aggr_fun
        temp_df.agg(aggr_fun)
        print(temp_df)
        aList[position] = temp_df.copy()
    # Combine list elements into desired dataframes and return in a list
    outList = merge_dataframes(aList, on=config.var_on)
    # Let's drop all the rows having 'NULL' or 'NaN's.
    outList[position] = outList[position].dropna()
    # Drop duplicate rows
    outList[position]= outList[position].drop_duplicates(keep='first').reset_index()
    outList[position] = outList[position].rename(columns={'index':'id'})
    return outList

#if __name__ == '__main__':
    #transform([])
    #print("Hello?")