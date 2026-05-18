import pandas as pd
from fastapi import FastAPI, Query
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from src.crime_dashboard import config

app = FastAPI(title="Crime Dashboard API")

# allow the React dev server to call this API without being blocked by the browser
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# serve the generated Folium map as a static file at /map
app.mount("/map", StaticFiles(directory=config.MAPS_DIR, html=True), name="map")


# returns analytics for dataset
@app.get("/summary")
def get_summary():

    df = pd.read_csv(config.ANALYTICS_SUMMARY_CSV)

    return df.iloc[0].to_dict()


# returns total crime count and percentage share for each standardised crime category
@app.get("/crimes/category")
def get_crimes_by_category():

    df = pd.read_csv(config.ANALYTICS_CATEGORY_CSV)

    return df.to_dict(orient="records")


# returns monthly crime totals with month-on-month change 
@app.get("/crimes/month")
def get_crimes_by_month():

    df = pd.read_csv(config.ANALYTICS_MONTH_CSV)

    return df.to_dict(orient="records")


# returns all LSOAs ranked by total crime count
@app.get("/crimes/area")
def get_crimes_by_area():

    df = pd.read_csv(config.ANALYTICS_AREA_CSV)

    return df.to_dict(orient="records")

# returns LSOAs ranked by crime rate 
# default top 10 max 100
@app.get("/crimes/area/top")
def get_top_areas(n: int = Query(default=10, ge=1, le=100)):

    df = pd.read_csv(config.ANALYTICS_AREA_CSV)

    return df.head(n).to_dict(orient="records")
