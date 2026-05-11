# UK Crime Dashboard

A python geospatial data project for loading, validating, cleaning, and eventually visualising UK crime data from Police.uk CSV files.

The long term goal of this project is to turn raw crime CSV files into a cleaned dataset with geospatial analysis outputs and an interactive crime dashboard that can be used to explore crime patterns by category, month, and area UK wide.

---

## Current Features

### Raw CSV Loading

The project can:

- Search recursively through folders and sub folders to find and read CSV files using pandas
- Load only required columns from raw datasets
- Combine multiple CSV files into one DataFrame
- Continue running if one file cannot be loaded
- Print progress messages showing files found, loaded, skipped, and number of total rows loaded

---

## Raw Data Validation

The project includes basic validation checks before data cleaning begins checking for things like missing required columns or empty datasets and displays clear validation messages at each stage to keep the user informed

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
- pandas - working with CSV data

Planned:

- GeoPandas - add geospatial functionality to cleaned data
- Folium or Leaflet - for interactive map
- Matplotlib - data visualisation and analysis charts
- FastAPI - backend API for dashboard
- PostGIS - geospatial database
- React - dashboard frontend