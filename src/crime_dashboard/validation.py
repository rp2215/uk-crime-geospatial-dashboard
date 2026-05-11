import pandas as pd
from . import config

def is_empty_dataframe(data_frame):

    if data_frame.empty:
        print("Validation failed: DataFrame is empty")
        return True

    return False

# find any required columns not included in dataframe
def find_missing_columns(data_frame):

    missing_columns = []

    for column in config.REQUIRED_COLUMNS:
        
        if column not in data_frame.columns:
            missing_columns.append(column)

    return missing_columns

# check dataframe has ALL required columns
def has_required_columns(data_frame):

    missing_column = find_missing_columns(data_frame)

    if missing_column:
        print("Validation failed: missing the following required column(s):")

        for column in missing_column:
            print(f"- {column}")
        
        return False
    
    print("Validation passed: all required columns are present")
    return True

def validate_raw_data(data_frame):

    print("Starting raw data validation...")

    if is_empty_dataframe(data_frame):
        return False
    
    if not has_required_columns(data_frame):
        return False
    
    print("Raw data validation complete")

    return True
