# LIBRARIES
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Fixing the column names
def rename_columns(data_df, long_name_series):

    '''
    The function is get used to renaming the columns based on another dataset.
    '''
    # Create a dictionary to map old column names to new column names
    column_name_mapping = dict(zip(data_df.columns, long_name_series))
    
    # Rename the columns of the DataFrame using the mapping
    data_df.rename(columns=column_name_mapping, inplace=True)


def splitting_median(data):
    """
    My computer is not enough to make the whole proccess for NaN values, I am going to create a 
    function to fill the columns with their medians.
    """
    data.fillna[data.median()]
    return data

