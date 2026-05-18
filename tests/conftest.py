import pandas as pd
import pytest

# minimal sample data matching shape of a cleaned Ploice.uk CSV file used across testing suite
SAMPLE_RAW_COLUMNS = [
    "Crime ID", "Month", "Reported by", "Falls within",
    "Longitude", "Latitude", "Location", "LSOA code",
    "LSOA name", "Crime type", "Last outcome category",
]

# build df that matches what data loder produces given the raw CSV files
@pytest.fixture
def raw_df():
    return pd.DataFrame([
        {
            "Crime ID": "abc123", "Month": "2025-08",
            "Reported by": "Cheshire Constabulary", "Falls within": "Cheshire Constabulary",
            "Longitude": -2.5, "Latitude": 53.2, "Location": "On or near High Street",
            "LSOA code": "E01234", "LSOA name": "Cheshire 001A",
            "Crime type": "burglary", "Last outcome category": "Under investigation",
        },
        {
            "Crime ID": "def456", "Month": "2025-08",
            "Reported by": "Cheshire Constabulary", "Falls within": "Cheshire Constabulary",
            "Longitude": -2.6, "Latitude": 53.3, "Location": "On or near Park Road",
            "LSOA code": "E01235", "LSOA name": "Cheshire 001B",
            "Crime type": "shoplifting", "Last outcome category": "Under investigation",
        },
    ], columns=SAMPLE_RAW_COLUMNS)

# clean the mimiced raw df using clean data method
@pytest.fixture
def cleaned_df(raw_df):

    from src.crime_dashboard.cleaning import clean_data
    return clean_data(raw_df)