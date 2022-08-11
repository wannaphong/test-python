import pandas as pd
#------------------------------------
# Function: netincome
# Description:
# Parameters:
#   - dataframe: Pandas dataframe that contain income and outcome trainsection
# Return:
#   - a net income from dataframe
#------------------------------------
def netincome(dataframe):
    result = 0
    col_one_list = sum(dataframe['income'].tolist())
    col_two_list = sum(dataframe['outcome'].tolist())

    #------------------------------------
    # TODO! write your code here.
    #------------------------------------
    return col_one_list - col_two_list
#------------------------------------
# DO NOT CHANGE a function name
# DO NOT CHANGE a Column name
#------------------------------------