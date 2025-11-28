import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

SENTINEL_CLIENT_ID = os.getenv("SENTINEL_CLIENT_ID")
SENTINEL_CLIENT_SECRET = os.getenv("SENTINEL_CLIENT_SECRET")

AUTH_URL = "https://services.sentinel-hub.com/oauth/token"
STAT_URL = "https://services.sentinel-hub.com/api/v1/statistical"

def get_access_token():
    """Fetch a fresh access token from Sentinel Hub"""
    data = {
        "client_id": SENTINEL_CLIENT_ID,
        "client_secret": SENTINEL_CLIENT_SECRET,
        "grant_type": "client_credentials"
    }
    response = requests.post(AUTH_URL, data=data)
    response.raise_for_status()
    return response.json().get("access_token")

def fetch_ndvi(lat: float, lon: float, window_km: float = 5):
    """
    Fetch average NDVI for a given lat/lon.
    Returns a single numeric value (mean NDVI over last 30 days).
    """
    token = get_access_token()
    headers = {"Authorization": f"Bearer {token}"}

    # Last 30 days
    end = datetime.utcnow()
    start = end - timedelta(days=30)

    # Convert km to ~degrees (1 degree ≈ 111 km)
    delta = window_km / 111.0
    bbox = [lon - delta, lat - delta, lon + delta, lat + delta]

    payload = {
        "input": {
            "bounds": {"bbox": bbox},
            "data": [
                {
                    "type": "sentinel-2-l2a",
                    "dataFilter": {
                        "timeRange": {
                            "from": start.strftime("%Y-%m-%dT%H:%M:%SZ"),
                            "to": end.strftime("%Y-%m-%dT%H:%M:%SZ")
                        }
                    }
                }
            ]
        },
        "aggregation": {
            "timeRange": {
                "from": start.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "to": end.strftime("%Y-%m-%dT%H:%M:%SZ")
            },
            "aggregationInterval": {"of": "P1M"},
            "resx": 100,
            "resy": 100,
            "evalscript": """
                //VERSION=3
                function setup() {
                    return {
                        input: ["B04", "B08"],
                        output: { bands: 1, sampleType: "FLOAT32" }
                    };
                }
                function evaluatePixel(sample) {
                    let ndvi = (sample.B08 - sample.B04) / (sample.B08 + sample.B04);
                    return [ndvi];
                }
            """
        }
    }

    try:
        response = requests.post(STAT_URL, headers=headers, json=payload)
        response.raise_for_status()
        stats = response.json()

        ndvi_mean = stats["data"][0]["outputs"]["default"]["bands"][0]["stats"]["mean"]
        return {"mean": ndvi_mean}

    except Exception as e:
        return {"mean": None, "error": str(e)}
