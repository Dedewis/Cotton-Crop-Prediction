import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("VISUAL_CROSSING_API_KEY")
BASE_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"

def fetch_weather(lat: float, lon: float):
    try:
        url = f"{BASE_URL}/{lat},{lon}?unitGroup=metric&key={API_KEY}&contentType=json"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        today = data["days"][0]
        return {
            "temperature": today.get("temp", None),
            "humidity": today.get("humidity", None),
            "rainfall": today.get("precip", None)
        }
    except Exception as e:
        print(f"❌ Weather fetch failed: {e}")
        return {"temperature": None, "humidity": None, "rainfall": None}
