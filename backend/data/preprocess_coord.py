import os
import time
import requests
import pandas as pd
from pathlib import Path

# -----------------------------
# Path setup (always relative to this script's folder)
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent
INPUT_CSV = BASE_DIR / "mandi_data.csv"
OUTPUT_CSV = BASE_DIR / "mandi_data_with_coords.csv"

# -----------------------------
# OpenCage API Key
# -----------------------------
API_KEY = os.getenv("OPENCAGE_API_KEY", "ecc75fa4c7c34dbd9636b5dcad612fe8")  # put your key if not using env vars
API_URL = "https://api.opencagedata.com/geocode/v1/json"

# -----------------------------
# Function to fetch coordinates
# -----------------------------
def fetch_coordinates(district, state):
    """
    Fetch (lat, lon) for a district+state using OpenCage API.
    Returns (lat, lon) or (None, None) if not found.
    """
    try:
        query = f"{district}, {state}, India"
        params = {"q": query, "key": API_KEY, "limit": 1}
        resp = requests.get(API_URL, params=params, timeout=10)

        if resp.status_code == 200:
            data = resp.json()
            if data.get("results"):
                coords = data["results"][0]["geometry"]
                return coords["lat"], coords["lng"]
    except Exception as e:
        print(f"❌ Error fetching coords for {district}, {state}: {e}")
    return None, None

# -----------------------------
# Main preprocessing
# -----------------------------
def preprocess_coords(input_csv=INPUT_CSV, output_csv=OUTPUT_CSV, sleep_sec=1.0):
    print(f"📂 Loading: {input_csv}")
    df = pd.read_csv(input_csv)

    if "District" not in df.columns or "State" not in df.columns:
        raise ValueError("CSV must contain 'District' and 'State' columns")

    # Unique district+state combos
    unique_places = df[["District", "State"]].drop_duplicates()

    cache = {}
    results = {}

    for _, row in unique_places.iterrows():
        district, state = row["District"], row["State"]
        key = (district, state)

        if key in cache:
            results[key] = cache[key]
            continue

        lat, lon = fetch_coordinates(district, state)
        cache[key] = (lat, lon)
        results[key] = (lat, lon)

        print(f"✅ {district}, {state} -> {lat}, {lon}")
        time.sleep(sleep_sec)  # to avoid hitting rate limits

    # Add lat/lon to dataframe
    df["lat"] = df.apply(lambda r: results.get((r["District"], r["State"]), (None, None))[0], axis=1)
    df["lon"] = df.apply(lambda r: results.get((r["District"], r["State"]), (None, None))[1], axis=1)

    # Save enriched file
    df.to_csv(output_csv, index=False)
    print(f"\n💾 Saved enriched CSV with coordinates: {output_csv}")


if __name__ == "__main__":
    preprocess_coords()
