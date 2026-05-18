from src.crime_dashboard.analytics import (
    crimes_by_category,
    crimes_by_month,
    crimes_by_area,
    top_crime_per_area,
    summary_stats,
)

def test_crimes_by_category_includes_pct(cleaned_df):

    result = crimes_by_category(cleaned_df)

    assert "pct" in result.columns
    assert result["pct"].sum() == 100.0

def test_crimes_by_month_sorted_ascending(cleaned_df):

    result = crimes_by_month(cleaned_df)

    assert list(result["month"]) == sorted(result["month"])

def test_crimes_by_area_returns_lsoa_columns(cleaned_df):

    result = crimes_by_area(cleaned_df)

    assert "lsoa_name" in result.columns
    assert "lsoa_code" in result.columns

def test_top_crime_per_area_one_row_per_lsoa(cleaned_df):

    result = top_crime_per_area(cleaned_df)

    assert result["lsoa_name"].nunique() == len(result)

def test_summary_stats_keys(cleaned_df):

    result = summary_stats(cleaned_df)
    
    for key in ["total_crimes", "unique_categories", "unique_areas", "top_category", "top_area"]:
        assert key in result
