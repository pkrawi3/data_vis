"""
Library housing functions and perhaps classes for modelling and plotting to be used by main.py
"""

# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Global Table
main_table = pd.DataFrame()
x_label    = ''
y_label    = ''

"""
Reads in the table file to be used by the rest of the program
Accepts:
    -   csv
    -   xlsx
    -   xls
Returns:
    table   :   containter of the DataFrame associated with the table file
    error   :   Boolean value indicating if a table was successfully read in
"""
def read_table(file_path, sheet=0):

    # Check file typ
    file_ending = file_path.split('.')[-1] 
    if(file_ending != 'csv' and file_ending != 'xls' and file_ending != 'xlsx'):
        return pd.DataFrame(), 1

    # Continue 
    try:
        table = pd.read_csv(file_path)
        error = 0
    except:
        try:
            table = pd.read_excel(file_path, sheet_name=sheet)
            error = 0
        except Exception as error_text:
            table = pd.DataFrame()
            error = 1
            print(error_text)

    return table, error
