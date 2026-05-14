import folium
import geopandas as gpd

from folium.plugins import MarkerCluster

from . import config

# file created by geoprocessing.py
def load_geo_data():

    if not config.CLEAN_GEOJSON.exists():
        raise FileNotFoundError(f"GeoJSON file not found: {config.CLEAN_GEOJSON}")
    
    geo_data = gpd.read_file(config.CLEAN_GEOJSON)

    print(f"Loaded geospatial data with {len(geo_data):,} row(s)")

    return geo_data

def create_base_map(geo_data):

    # calculate average lat/lon to center map around
    centre_lat = geo_data["latitude"].mean()
    centre_lon = geo_data["longitude"].mean()

    crime_map = folium.Map(location=[centre_lat,centre_lon], zoom_start=10)

    return crime_map

def add_crime_markers(crime_map,geo_data):

    marker_cluster = MarkerCluster().add_to(crime_map)

    # for each crime record create marker with popup
    for _, row in geo_data.iterrows():

        popup_text = (

            f"<strong>Crime type:</strong> "
            f"{row.get('crime_type_std', '')}<br>"
            f"<strong>Month:</strong> "
            f"{row.get('month', '')}<br>"
            f"<strong>Location:</strong> "
            f"{row.get('location', '')}"
        )

        marker = folium.Marker(location=[row["latitude"],row["longitude"]], popup=folium.Popup(popup_text, max_width= 300))
        marker.add_to(marker_cluster)

    return crime_map

def save_map(crime_map):

    config.MAPS_DIR.mkdir(parents=True, exist_ok=True)

    crime_map.save(config.CRIME_MAPS_HTML)

    print(f"Saved crime map to: {config.CRIME_MAPS_HTML}")

def build_map():

    print("Building map")

    geo_data = load_geo_data()

    if geo_data.empty:
        print("No geospatial data available to build map")
        return 
    
    crime_map = create_base_map(geo_data)
    crime_map = add_crime_markers(crime_map,geo_data)
    save_map(crime_map)

    print("Map successfully built")

if __name__ == "__main__":

    build_map()



