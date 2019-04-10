import numpy as np
import pandas as pd
import copy
#import sqlalchemy
#from sqlalchemy.ext.automap import automap_base, declarative_base
#from sqlalchemy.orm import Session
#from sqlalchemy import create_engine, func

# Config
import config
from config import data_src_list, col_list, name_list

# import 
import extract
from extract import extract
# import transform
from transform import transform

# Call the extract python script to extract data
# Construct url strings
url_list = []
url_list = copy.deepcopy(data_src_list)

# Call the extract.py's extract method
extract_out_list = []
extract_out_list = extract(url_list)

# Write output to a .csv file
transform_out_list = []
transform_out_list = transform(extract_out_list)
pd.DataFrame.to_csv(transform_out_list[0], './combined_df.csv', sep=',', na_rep='.', index=False)