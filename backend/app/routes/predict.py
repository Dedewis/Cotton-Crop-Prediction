from fastapi import APIRouter, HTTPException
import pandas as pd
import joblib
import os

router = APIRouter()

# ============================
# PATHS
# ============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "../../data/mandi_data_with_ndvi_weather.csv")
MODEL_PATH = os.path.join(BASE_DIR, "../../models/finall_cotton_model.pkl")

# ============================
# LOAD MODEL + DATA
# ============================
try:
    model = joblib.load(MODEL_PATH)  # MUST be full pipeline
except Exception as e:
    raise RuntimeError(f"❌ Could not load model: {e}")

try:
    df = pd.read_csv(DATA_PATH)
except Exception as e:
    raise RuntimeError(f"❌ Could not load dataset: {e}")

mean_price = df["Modal_x0020_Price"].mean()


# ============================
# MAIN API
# ============================
@router.get("/")
def predict_price(state: str, district: str):

    # 1 — Filter row
    row = df[
        (df["State"].str.lower() == state.lower()) &
        (df["District"].str.lower() == district.lower())
    ]

    if row.empty:
        raise HTTPException(404, "State/District not found.")

    row = row.iloc[0]

    # 2 — Prepare input EXACTLY as model expects
    input_df = pd.DataFrame([{
        "State": row["State"],
        "District": row["District"],
        "Commodity": row["Commodity"],
        "lat": row["lat"],
        "lon": row["lon"],
        "NDVI_Mean": row["NDVI_Mean"],
        "Weather_Temp": row["Weather_Temp"]
    }])

    # 3 — Directly use pipeline
    try:
        predicted_price = float(model.predict(input_df)[0])
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Model prediction failed: {e}"
        )

    expected_profit = predicted_price - mean_price

    return {
        "state": row["State"],
        "district": row["District"],
        "latitude": row["lat"],
        "longitude": row["lon"],
        "commodity": row["Commodity"],
        "ndvi_mean": row["NDVI_Mean"],
        "weather_temp": row["Weather_Temp"],

        "predicted_price": round(predicted_price, 2),
        "expected_profit": round(expected_profit, 2)
    }
