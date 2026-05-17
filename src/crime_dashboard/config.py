from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Data Directories
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
MAPS_DIR = PROJECT_ROOT / "maps"

# Output for cleaned data
CLEAN_CSV = PROCESSED_DATA_DIR / "crime_clean.csv"

# output for cleaned geo data
CLEAN_GEOJSON = PROCESSED_DATA_DIR / "crime_clean_geo.geojson"

# output for generated maps
CRIME_MAPS_HTML = MAPS_DIR / "crime_map.html"

# Analytics output directory and files
ANALYTICS_DIR = PROCESSED_DATA_DIR / "analytics"
ANALYTICS_CATEGORY_CSV = ANALYTICS_DIR / "crimes_by_category.csv"
ANALYTICS_MONTH_CSV = ANALYTICS_DIR / "crimes_by_month.csv"
ANALYTICS_AREA_CSV = ANALYTICS_DIR / "crimes_by_area.csv"
ANALYTICS_TOP_CRIME_PER_AREA_CSV = ANALYTICS_DIR / "top_crime_per_area.csv"
ANALYTICS_SUMMARY_CSV = ANALYTICS_DIR / "summary.csv"
 
# column names expected in raw csv file (Police.uk)
REQUIRED_COLUMNS = [
    "Crime ID",
    "Month",
    "Reported by",
    "Falls within",
    "Longitude",
    "Latitude",
    "Location",
    "LSOA code",
    "LSOA name",
    "Crime type",
    "Last outcome category",
]

# used for map display
CATEGORY_MAP = {
    "theft from the person": "Theft",
    "shoplifting": "Theft",
    "other theft": "Theft",
    "bicycle theft": "Theft",
    "vehicle crime": "Vehicle Crime",
    "robbery": "Robbery",
    "violence and sexual offences": "Violence/Sexual",
    "public order": "Public Order",
    "burglary": "Burglary",
    "criminal damage and arson": "Criminal Damage/Arson",
    "drugs": "Drugs",
    "possession of weapons": "Weapons",
    "anti-social behaviour": "ASB",
    "other crime": "Other",
}


