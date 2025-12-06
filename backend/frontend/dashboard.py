
import requests
import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import time
import random
import io
import base64

# ==========================
# CONFIG
# ==========================
FASTAPI_URL = "http://127.0.0.1:8000/predict/"
DATA_PATH = "mandi_data_with_ndvi_weather.csv"

df = pd.read_csv(DATA_PATH)

from st_audiorec import st_audiorec
import requests
import streamlit as st


st.set_page_config(page_title="Cotton Crop Dashboard", layout="wide")
st.title("🌾 Cotton Crop Intelligence Dashboard")

# Seasonal hints
SEASONAL_TIPS = [
    "Check for early pest symptoms this month!",
    "Ideal time for fertilizer adjustment.",
    "Monitor soil moisture regularly.",
    "NDVI trends show moderate crop health this week.",
]

# ==========================
# SIDEBAR – USER INPUT
# ==========================
st.sidebar.header("🔍 Prediction Input")

states = sorted(df["State"].unique())
state = st.sidebar.selectbox("State", states)

districts = sorted(df[df["State"] == state]["District"].unique())
district = st.sidebar.selectbox("District", districts)

commodities = sorted(df[(df["State"] == state) & (df["District"] == district)]["Commodity"].unique())
commodity = st.sidebar.selectbox("Commodity", commodities)

# Predict Button
if st.sidebar.button("Predict Price"):
    with st.spinner("Predicting best market estimate..."):
        try:
            response = requests.get(
                FASTAPI_URL,
                params={"state": state, "district": district, "commodity": commodity}
            )
            result = response.json() if response.status_code == 200 else None
        except:
            st.error("Backend not reachable.")
            result = None
else:
    result = None


# =======================================================
# MAIN – PREDICTION RESULTS + INSIGHTS + MINI MAP
# =======================================================
if result:
    st.subheader("🎯 Prediction Overview")

    # Animated counters
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Predicted Price (₹)", result["predicted_price"])

    with col2:
        profit = result["expected_profit"]
        emoji = "🟢" if profit > 0 else "🔴"
        st.metric("Expected Profit", f"{emoji} {profit}")

    with col3:
        st.metric("Temperature (°C)", round(result["weather_temp"], 2))

    # NDVI + commodity
    colA, colB = st.columns(2)
    colA.metric("NDVI Mean", round(result["ndvi_mean"], 3))
    colB.metric("Commodity", commodity)

    # -----------------------------------------------------
    # ⭐ Cotton Vibes of the Day — summary box
    # -----------------------------------------------------
    st.markdown("### ✨ Cotton Vibes of the Day")
    weather_temp = result["weather_temp"]
    weather_mood = (
        "Sunny & Bright 🌞" if weather_temp > 30 else
        "Cool Breeze 🌤" if weather_temp > 20 else
        "Chilly Air ❄"
    )
    crop_status = (
        "Healthy Growth 🌱" if result["ndvi_mean"] > 0.4 else
        "Moderate Condition 🍂"
    )

    st.info(f"""
        **🌡 Weather says:** {weather_mood}  
        **🌱 Crop Status:** {crop_status}  
        **💹 Market Pulse:** {'📈 Strong demand expected' if profit > 0 else '📉 Weak movement in trading'}  
        **🎯 Your Selection:** {commodity} in {district}, {state}
    """)

    # -----------------------------------------------------
    # ⭐ State Mini Map
    # -----------------------------------------------------
    st.markdown("### 🗺 Mini Map of Selected State")
    state_df = df[df["State"] == state]

    fig_map = px.scatter_geo(
        state_df,
        lat="lat", 
        lon="lon",
        hover_name="District",
        scope="asia",
        title=f"{state} District Map",
        size=[8]*len(state_df),
    )

    st.plotly_chart(fig_map, use_container_width=True)

# =======================================================
# FUN ELEMENTS + INSIGHT CARDS
# =======================================================

st.markdown("## ⭐ Smart Insight Cards")

colA, colB, colC = st.columns(3)

with colA:
    st.success("🌦 Seasonal Tip")
    st.write(random.choice(SEASONAL_TIPS))

with colB:
    st.warning("📊 NDVI Insight")
    st.write("Higher NDVI regions consistently show better price trends.")

with colC:
    st.info("📰 Mandi News")
    st.write("Cotton arrivals slightly increased across major mandis today.")

# =======================================================
# COLLAPSIBLE CHARTS
# =======================================================

st.markdown("## 📈 Visual Insights")

# --- Button 1: NDVI vs Price ---
if st.button("Show NDVI vs Price"):
    st.subheader("🌱 NDVI vs Price")
    fig2 = px.scatter(
        df,
        x="NDVI_Mean",
        y="Modal_x0020_Price",
        color="State",
        title="NDVI vs Price Relationship"
    )
    st.plotly_chart(fig2, use_container_width=True)

# --- Button 2: District Comparison ---
if st.button("Show District Price Comparison"):
    st.subheader(f"🏙 District Price Comparison – {state}")
    district_df = df[df["State"] == state].groupby("District").mean(numeric_only=True)
    fig3 = px.bar(
        district_df,
        x=district_df.index,
        y="Modal_x0020_Price",
        title=f"Average Price of Districts in {state}"
    )
    st.plotly_chart(fig3, use_container_width=True)

    
st.subheader("🎤 Voice Input")

wav_audio_data = st_audiorec()

if wav_audio_data is not None:
    st.audio(wav_audio_data, format='audio/wav')

    if st.button("Convert Voice to Text"):
        response = requests.post(
            "http://127.0.0.1:8000/voice/speech-to-text/",
            files={"file": ("audio.wav", wav_audio_data, "audio/wav")}
        )

        text_output = response.json()
        st.success(f"Recognized Speech: {text_output.get('text')}")








