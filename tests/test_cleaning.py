import pandas as pd
from src.crime_dashboard.cleaning import (
    standardise_column_names,
    remove_duplicates,
    clean_coordinates,
    clean_month_column,
    standardise_crime_type,
)

def test_column_names_are_snake_case(raw_df):

    result = standardise_column_names(raw_df)

    assert "crime_type" in result.columns
    assert "Crime type" not in result.columns

def test_duplicate_rows_are_removed(raw_df):

    doubled = pd.concat([raw_df, raw_df], ignore_index=True)
    renamed = standardise_column_names(doubled)

    result = remove_duplicates(renamed)

    assert len(result) == len(raw_df)

def test_invalid_coordinates_are_dropped():

    df = pd.DataFrame([
        {"latitude": 999, "longitude": -2.5},   # invalid
        {"latitude": 53.2, "longitude": -2.5},  # valid
    ])

    result = clean_coordinates(df)

    assert len(result) == 1

def test_month_parsed_to_period(raw_df):

    renamed = standardise_column_names(raw_df)

    result = clean_month_column(renamed)

    assert result["month"].iloc[0] == "2025-08"
    assert "year" in result.columns
    assert "month_name" in result.columns

def test_crime_type_std_mapped(cleaned_df):

    # shoplifting should roll up to Theft via CATEGORY_MAP
    assert "Theft" in cleaned_df["crime_type_std"].values

def test_unmapped_crime_type_becomes_other():
   
    df = pd.DataFrame([{"crime_type": "unknown offence type"}])

    result = standardise_crime_type(df)
    
    assert result["crime_type_std"].iloc[0] == "Other"
