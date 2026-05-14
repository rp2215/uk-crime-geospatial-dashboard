import pandas as pd
import geopandas as gpd

from . import config

# loads data produced by pipeline
def load_cleaned_data():

    if not config.CLEAN_CSV.exists():
        raise FileNotFoundError(f"Cleaned CSV file not found: {config.CLEAN_CSV}")
    
    data_frame = pd.read_csv(config.CLEAN_CSV, low_memory=False)

    print(f"Loaded cleaned data with: {len(data_frame):,} row(s)")

    return data_frame

# check cleaned data has the lat/lon columns
def validate_coordinate_columns(data_frame):

    required_columns = ["longitude","latitude"]

    missing_columns = []

    for column in required_columns:

        if column not in data_frame.columns:
            missing_columns.append(column)

    # required columns are missing
    if missing_columns:
        raise ValueError(f"Cannot create geometry due to following columns missing: {missing_columns}")
    
    print("Coordinate columns found")

def create_geo_dataframe(data_frame):

    geo_data = data_frame.copy()

    # build GDP using geomerty points
    # EPSG:4326 expected format for web maps
    geometry_points = gpd.points_from_xy(geo_data["longitude"],geo_data["latitude"])
    geo_data = gpd.GeoDataFrame(geo_data, geometry=geometry_points, crs="EPSG:4326")

    print(f"Created GeoDataFrame with {len(geo_data):,} row(s)")

    return geo_data

# save as GeoJSON file
def save_geo_data(geo_data):

    # ensure folder exists and save
    config.PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    geo_data.to_file(config.CLEAN_GEOJSON, driver="GeoJSON")

    print(f"Saved geospatial data to {config.CLEAN_GEOJSON}")

def run_geoprocessing():

    print("Starting geospatial processing")

    cleaned_data = load_cleaned_data()
    validate_coordinate_columns(cleaned_data)
    
    geo_data = create_geo_dataframe(cleaned_data)
    save_geo_data(geo_data)

    print("Geospatial processing complete")

if __name__ == "__main__":

    run_geoprocessing()

