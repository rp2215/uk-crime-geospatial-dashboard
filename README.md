# UK Crime Dashboard

A python geospatial data project for loading, processing, analysing, and visualising UK crime date from Police.uk CSV files.

The long term goal of this project is to turn raw crime CSV files into a cleaned dataset with geospatial analysis outputs and an interactive crime dashboard that can be used to explore crime patterns by category, month, and area UK wide.

---

## Key Features

### Data Loading

- Recursivley searches folders for CSV files
- Loads only required columns to keep memory usage low
- Combines multiple CSV file into a single DataFrame
- Continue loading if one file fails, reporting any skipped files
- Prints progress showing files found, loaded, skipped, and total rows

---

## Validation

- Checks for required columns before processing begins
- Rejects empty datasets early
- Clear validation messages at each stage

---

## Data Cleaning

- Standardises column names to snake_case
- Removes duplicate rows
- Converts and validates lat/lon coordinates, dropping rows outside valid ranges
- Parses month column into YYYY-MM format extracting year, month_number, and month_name
- Maps raw crime types to standardised categories (e.g. shoplifting -> Theft)

---

## Geospatial Processing

- Creates a GeoDataFrame from cleaned lat/lon coordinates using ESPG:4326
- Saves output as a GeoJSON for use in mapping and future spatial analysis

---

## Analytics

- Crime counts are broken down by category, month, area (LSOA boundaries), and responsing police force
- Monthly totals and month by month changes
- Highest crime rate areas
- Highest crime categories in each area

---

## Interactive Map

- Folium map with marker cluster showing crime type, month, and location popups

---
## Planned Features

Planned features include:

- clean column names into consistent format
- remove duplicate rows including crime ID's
- convert lat/lon coordinates into numbers and check they are valid
- standardise crime categories
- clean/format month/date column
- save cleaned file
- convert cleaned data into GeoDataFrame
- create gemoerty points from lat/lon
- load boundary data of LSOA's
- join crime points to geographic boundaries

#### Geospatial

- create geometry points from lat/lon
- load LSOA boundary data

#### Map
- create interactive map
- add crime markers to map
- add marker clustering
- heat map layer
- marker popups
- save map output

#### Analytics
- count crime by:
    - category
    - month
    - area
- show month by month changes
- create summary tables
- identfiy top crimes per area
- identify areas with highest crime counts

#### Dashboard
- dashboard layout
- category filter
- month filter
- area filter
- stats summary cards
- trend charts
- interactive map panel
- crime category breakdown

#### Testing
- unit tests validation
- unit tests cleaning
- unit test data loading
- sample dataset for repeatable testing
- coordinate cleaning tests

--- 

## Tech Stack

Current

- Python
- pandas
- GeoPandas
- Folium
- pytest
- GitHub Actions


Planned:

- Matplotlib - data visualisation and analysis charts
- FastAPI - backend API for dashboard
- PostGIS - geospatial database
- React - dashboard frontend