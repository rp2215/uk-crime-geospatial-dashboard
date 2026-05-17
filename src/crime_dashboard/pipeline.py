# run full data processing pipeline

from .data_loader import read_raw_csvs
from .validation import validate_raw_data
from .cleaning import clean_data
from .cleaning import save_cleaned_data
from .geoprocessing import run_geoprocessing
from .analytics import run_analytics

def run_pipeline():

    print("Starting crime data processing pipeline")

    raw_data = read_raw_csvs()

    if raw_data.empty:
        print("Pipeline Failure: No raw data was loaded")
        return
    
    is_valid = validate_raw_data(raw_data)

    if not is_valid:
        print("Pipeline Failure: Raw data validation failed")
        return

    cleaned_data = clean_data(raw_data)

    if cleaned_data.empty:
        print("Pipeline Failure: Cleaning process resulted in no usable data")
        return 

    save_cleaned_data(cleaned_data)

    run_geoprocessing()

    run_analytics()

    print("Full pipeline complete")

if __name__ == "__main__":

    run_pipeline()