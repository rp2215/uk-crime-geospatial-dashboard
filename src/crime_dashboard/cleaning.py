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

def clean_coordinates(data_frame):

    cleaned_data = data_frame.copy()
    before = len(cleaned_data)

    # convert to numbers
    cleaned_data["latitude"] = pd.to_numeric(cleaned_data["latitude"], errors="coerce")
    cleaned_data["longitude"] = pd.to_numeric(cleaned_data["longitude"], errors="coerce")    

    # remove invalid corrdinates
    valid_coordinates = (cleaned_data["latitude"].between(-90,90) & cleaned_data["longitude"].between(-180,180))
    cleaned_data = cleaned_data.loc[valid_coordinates].copy()

    removed = before - len(cleaned_data)
    
    if removed > 0:
        print(f"Removed {removed:,} row(s) with invalid coordinates")
    
    return cleaned_data

def clean_month_column(data_frame):

    cleaned_data = data_frame.copy()
    before = len(cleaned_data)

    # convert month column into datetime values
    cleaned_data["month"] = pd.to_datetime(cleaned_data["month"],errors="coerce")

    # remove rows that coudlnt be converted
    cleaned_data = cleaned_data.dropna(subset=["month"]).copy()
    
    removed = before - len(cleaned_data)

    if removed > 0:
        print(f"Removed {removed:,} row(s) with invalid month values")
    
    cleaned_data["year"] = cleaned_data["month"].dt.year
    cleaned_data["month_number"] = cleaned_data["month"].dt.moth
    cleaned_data["month_name"] = cleaned_data["month"].dt.month_name()

    # convert back to YYYY-MM (easier grouping later)
    cleaned_data["month"] = cleaned_data["month"].dt.to_period("M").astype(str)

    return cleaned_data

def clean_data(data_frame):

    if data_frame.empty:
        print("No data to clean")

        return data_frame
    
    print("Starting data cleaning ...")

    cleaned_data = data_frame.copy()

    cleaned_data = standardise_column_names(cleaned_data)
    cleaned_data = remove_duplicates(cleaned_data)
    cleaned_data = clean_coordinates(cleaned_data)
    cleaned_data = clean_month_column(clean_data)

    print(f"Data cleaning complete. Final row(s): {len(cleaned_data):,}")

    return cleaned_data

# save cleaned df to processed data folder
def save_cleaned_data(data_frame):

    config.PROCESSED_DATA_DIR.mkdir(parents=True,exist_ok=True)
    data_frame.to_csv(config.CLEAN_CSV, index=False)

    print(f"Saved cleaned data to {config.CLEAN_CSV}")
