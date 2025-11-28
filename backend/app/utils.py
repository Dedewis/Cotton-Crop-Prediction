import os
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
RESOURCE_ID = os.getenv("RESOURCE_ID")

CSV_FILE_PATH = os.path.join(os.path.dirname(__file__), "../data/mandi_data.csv")


# 🔹 API fetch
def fetch_live_cotton_price(state=None, district=None, commodity=None, date=None):
    url = f"https://api.data.gov.in/resource/{RESOURCE_ID}"
    params = {
        "api-key": API_KEY,
        "format": "json",
        "limit": 20
    }

    if state:
        params["filters[state]"] = state
    if district:
        params["filters[district]"] = district
    if commodity:
        params["filters[commodity]"] = commodity
    if date:
        params["filters[arrival_date]"] = date

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if "records" in data and data["records"]:
                return data["records"]
            else:
                return {"error": "No data found for given filters"}
        else:
            return {"error": f"API request failed with status {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}


# 🔹 CSV fetch
def fetch_local_cotton_price(state=None, district=None, commodity=None, date=None):
    try:
        df = pd.read_csv(CSV_FILE_PATH)
        df.columns = [c.strip().lower() for c in df.columns]

        if state:
            df = df[df["state"].str.contains(state, case=False, na=False)]
        if district:
            df = df[df["district"].str.contains(district, case=False, na=False)]
        if commodity:
            df = df[df["commodity"].str.contains(commodity, case=False, na=False)]
        if date:
            df = df[df["arrival_date"].str.contains(date, case=False, na=False)]

        records = df.head(20).to_dict(orient="records")

        if not records:
            return {"error": "No matching records found"}
        return records

    except Exception as e:
        return {"error": str(e)}
    
