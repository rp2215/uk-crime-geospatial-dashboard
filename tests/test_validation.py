import pandas as pd
from src.crime_dashboard.validation import validate_raw_data, has_required_columns

def test_valid_data_passes(raw_df):

    assert validate_raw_data(raw_df) is True

def test_empty_dataframe_fails():

    assert validate_raw_data(pd.DataFrame()) is False

def test_missing_column_fails(raw_df):

    df = raw_df.drop(columns=["Crime type"])

    assert has_required_columns(df) is False

def test_all_columns_present(raw_df):
    
    assert has_required_columns(raw_df) is True
