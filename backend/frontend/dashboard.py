import streamlit as st
import pandas as pd
import requests
import plotly.express as px

# ==========================
# CONFIG
# ==========================
FASTAPI_URL = "http://127.0.0.1:8000/predict/"   # FIXED URL (added slash)
DATA_PATH = "mandi_data_with_ndvi_weather.csv"   # Your dataset

# Load dataset
df = pd.read_csv(DATA_PATH)

st.set_page_config(page_title="Cotton Crop Dashboard", layout="wide")
st.title("🌾  Market Analytics Dashboard")

# ==========================
# SIDEBAR — USER INPUT
# ==========================
st.sidebar.header("Prediction Input")

states = sorted(df["State"].unique())
state = st.sidebar.selectbox("Select State", states)

districts = sorted(df[df["State"] == state]["District"].unique())
district = st.sidebar.selectbox("Select District", districts)

if st.sidebar.button("Predict Price"):
    with st.spinner("Fetching prediction..."):

        try:
            # USE POST — FIXED
            response = requests.get(
                FASTAPI_URL,
                params={"state": state, "district": district}
            )

            if response.status_code == 200:
                result = response.json()
            else:
                st.error(f"Error: {response.json()['detail']}")
                result = None

        except Exception as e:
            st.error("Backend not running or endpoint unreachable!")
            result = None
else:
    result = None


# ==========================
# SHOW PREDICTION OUTPUT
# ==========================
if result:
    st.subheader("📌 Prediction Results")

    col1, col2, col3 = st.columns(3)

    col1.metric("Predicted Price (₹)", result["predicted_price"])
    col2.metric("Expected Profit (₹)", result["expected_profit"])
    col3.metric("Temperature (°C)", round(result["weather_temp"], 2))

    col4, col5 = st.columns(2)
    col4.metric("NDVI Mean", round(result["ndvi_mean"], 3))
    col5.metric("Commodity", result["commodity"])





# ==========================
# CHART 2 – NDVI vs Price
# ==========================
st.subheader("🌱 NDVI vs Price Relationship")

fig2 = px.scatter(
    df,
    x="NDVI_Mean",
    y="Modal_x0020_Price",
    color="State",
    title="NDVI vs Price"
)
st.plotly_chart(fig2, use_container_width=True)


# ==========================
# CHART 3 – District Comparison
# ==========================
st.subheader(f"🏙 District-level Comparison – {state}")

district_df = df[df["State"] == state].groupby("District").mean(numeric_only=True)

fig3 = px.bar(
    district_df,
    x=district_df.index,
    y="Modal_x0020_Price",
    title=f"Average Prices of Districts in {state}"
)
st.plotly_chart(fig3, use_container_width=True)
