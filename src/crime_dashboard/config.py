from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Data Directories
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Output for cleaned data
CLEAN_CSV = PROCESSED_DATA_DIR / "crime_clean.csv"

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
    "Outcome type",
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


