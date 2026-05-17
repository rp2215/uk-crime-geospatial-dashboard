import pandas as pd
from . import config

# load cleaned CSV produced by pipeline
def load_data():

    if not config.CLEAN_CSV.exists():
        raise FileNotFoundError(f"Cleaned CSV not found: {config.CLEAN_CSV}")

    df = pd.read_csv(config.CLEAN_CSV, low_memory=False)

    print(f"Loaded {len(df):,} row(s) for analytics")

    return df

# break down total crimes by category
def crimes_by_category(df):

    counts = (
        df.groupby("crime_type_std")
        .size()
        .reset_index(name="count")
        .sort_values("count", ascending=False)
    )

    counts["pct"] = (counts["count"] / counts["count"].sum() * 100).round(1)

    return counts

# get total crime counts per month and calculate monthly changes
def crimes_by_month(df):

    monthly = (
        df.groupby("month")
        .size()
        .reset_index(name="count")
        .sort_values("month")
    )

    monthly["change"] = monthly["count"].diff().fillna(0).astype(int)
    monthly["pct_change"] = (monthly["count"].pct_change() * 100).round(1).fillna(0)

    return monthly

# rank the LSOA's by total crime count
def crimes_by_area(df):

    area = (
        df.groupby(["lsoa_name", "lsoa_code"])
        .size()
        .reset_index(name="count")
        .sort_values("count", ascending=False)
    )

    return area


def top_areas(df, n=10):

    return crimes_by_area(df).head(n)

# find most common crime type per LSOA
def top_crime_per_area(df):

    top = (
        df.groupby(["lsoa_name", "crime_type_std"])
        .size()
        .reset_index(name="count")
        .sort_values("count", ascending=False)
        .drop_duplicates(subset="lsoa_name")
        .rename(columns={"crime_type_std": "top_crime_type"})
        .sort_values("lsoa_name")
    )

    return top

# get total crime counts by each police force
def crimes_by_force(df):

    force = (
        df.groupby("reported_by")
        .size()
        .reset_index(name="count")
        .sort_values("count", ascending=False)
    )

    return force


def summary_stats(df):

    month_sorted = df["month"].sort_values()

    summary = {
        "total_crimes": len(df),
        "unique_categories": df["crime_type_std"].nunique(),
        "unique_areas": df["lsoa_name"].nunique(),
        "date_range_start": month_sorted.iloc[0],
        "date_range_end": month_sorted.iloc[-1],
        "top_category": df["crime_type_std"].value_counts().idxmax(),
        "top_area": df["lsoa_name"].value_counts().idxmax(),
    }

    return summary


def _save_results(category_df, month_df, area_df, top_crime_df, summary):

    config.ANALYTICS_DIR.mkdir(parents=True, exist_ok=True)

    category_df.to_csv(config.ANALYTICS_CATEGORY_CSV, index=False)
    month_df.to_csv(config.ANALYTICS_MONTH_CSV, index=False)
    area_df.to_csv(config.ANALYTICS_AREA_CSV, index=False)
    top_crime_df.to_csv(config.ANALYTICS_TOP_CRIME_PER_AREA_CSV, index=False)
    pd.DataFrame([summary]).to_csv(config.ANALYTICS_SUMMARY_CSV, index=False)

    print(f"Saved analytics to {config.ANALYTICS_DIR}")


def _print_summary(summary, category_df, month_df):

    print("\n--- Analytics Summary ---")
    print(f"  Total crimes    : {summary['total_crimes']:,}")
    print(f"  Date range      : {summary['date_range_start']} to {summary['date_range_end']}")
    print(f"  Categories      : {summary['unique_categories']}")
    print(f"  Areas (LSOAs)   : {summary['unique_areas']}")
    print(f"  Top category    : {summary['top_category']}")
    print(f"  Top area        : {summary['top_area']}")

    print("\n  Crimes by category:")
    for _, row in category_df.iterrows():
        print(f"    {row['crime_type_std']:<25} {row['count']:>6,}  ({row['pct']}%)")

    print("\n  Crimes by month:")
    for _, row in month_df.iterrows():

        # Show a dash for the first month where there is no prior period to compare
        change_str = f"{row['change']:+,}" if row["change"] != 0 else "—"

        print(f"    {row['month']}  {row['count']:>6,}  {change_str}")

    print("--- End of Summary ---\n")

# called by pipeline runs analytic methods and saves the ouputs
def run_analytics():

    print("Starting analytics")

    df = load_data()

    if df.empty:
        print("Analytics skipped: no data available")
        return

    category_df = crimes_by_category(df)
    month_df = crimes_by_month(df)
    area_df = crimes_by_area(df)
    top_crime_df = top_crime_per_area(df)
    force_df = crimes_by_force(df)
    summary = summary_stats(df)

    _print_summary(summary, category_df, month_df)
    _save_results(category_df, month_df, area_df, top_crime_df, summary)

    print("Analytics complete")


if __name__ == "__main__":

    run_analytics()
