import pandas as pd
from . import config

# Rename given column names from raw CSV files into standard snake case
def standardise_column_names(data_frame):
    
    standardised_data = data_frame.copy()

    # dict mapping old to new column names
    rename_map = { 
        "Crime ID": "crime_id", 
        "Month": "month", 
        "Reported by": "reported_by",  
        "Falls within": "falls_within",  
        "Longitude": "longitude",  
        "Latitude": "latitude",  
        "Location": "location",  
        "LSOA code": "lsoa_code",  
        "LSOA name": "lsoa_name",  
        "Crime type": "crime_type",  
        "Last outcome category": "last_outcome_category",  
        "source_file": "source_file",  
    }  

    standardised_data = standardised_data.rename(columns=rename_map) # apply renaming using map

    return standardised_data

def remove_duplicates(data_frame):

    duplicate_free = data_frame.copy()
    before = len(duplicate_free)

    duplicate_free = duplicate_free.drop_duplicates()

    removed = before - len(duplicate_free)

    if removed > 0:
        print(f"Removed {removed:,} duplicate row(s)")

    return duplicate_free

def clean_data(data_frame):

    if data_frame.empty():
        print("No data to clean")

        return data_frame
    
    print("Starting data cleaning ...")

    cleaned_data = data_frame.copy()

    cleaned_data = standardise_column_names(cleaned_data)
    cleaned_data = remove_duplicates(cleaned_data)

    print(f"Data cleaning complete. Final row(s): {len(cleaned_data):,}")

    return cleaned_data