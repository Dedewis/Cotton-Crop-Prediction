import os
import requests
from dotenv import load_dotenv

# Load environment variable
load_dotenv()
API_KEY = os.getenv("579b464db66ec23bdd0000013f49f7c4e08d40b366c8a3e7a21ea619")
BASE_URL = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"

def fetch_live_cotton_price(limit=1):
    params = {
        "api-key": API_KEY,
        "format": "json",
        "filters[commodity]": "Cotton",
        "limit": limit
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        records = data.get("records", [])
        return records[0] if records else None
    else:
        raise Exception(f"AGMARKNET fetch failed: {response.status_code}")
