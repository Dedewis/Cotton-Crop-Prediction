import streamlit as st
import pandas as pd
import plotly.express as px
from utils.theme import apply_theme
from utils.language import translate, languages

# -------------------------------
# CONFIG
# -------------------------------
st.set_page_config(page_title="CropWise – Dashboard", layout="wide")

if "theme" not in st.session_state:
    st.session_state.theme = "light"

if "language" not in st.session_state:
    st.session_state.language = "en"

# translation helper
def t(key):
    return translate(key, st.session_state.language)

apply_theme(st.session_state.theme)


# -------------------------------
# LOAD DATA (FIXED PATH)
# -------------------------------
import os

# Determine the project root no matter where streamlit was launched
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

DATA_PATH = os.path.join(BASE_DIR, "backend", "app", "data", "mandi_data_with_ndvi_weather.csv")

if not os.path.exists(DATA_PATH):
    st.error(f"❌ Dataset not found.\nPath checked:\n{DATA_PATH}")
    st.stop()

df = pd.read_csv(DATA_PATH)



# -------------------------------
# FETCH SESSION VALUES
# -------------------------------
state = st.session_state.get("selected_state", None)
district = st.session_state.get("selected_district", None)

if not state or not district:
    st.warning("⚠ Please go to the Predict page and select State & District first.")
    st.stop()


# -------------------------------
# PAGE TITLE
# -------------------------------
st.markdown(
    f"""
    <h1 style="font-weight:900;">📊 {t("dashboard")}</h1>
    <p style="opacity:0.8;">{t("dashboard_sub")}</p>
    """,
    unsafe_allow_html=True,
)

st.write("")


# -------------------------------
# FILTER DATA FOR STATE & DISTRICT
# -------------------------------
filtered_df = df[
    (df["State"] == state) &
    (df["District"] == district)
]

if filtered_df.empty:
    st.error(f"No data found for {district}, {state}.")
    st.stop()


# -------------------------------
# METRICS
# -------------------------------
latest = filtered_df.iloc[-1]

c1, c2, c3, c4 = st.columns(4)

c1.metric("🌡 Temperature (°C)", round(latest["Temperature"], 2))
c2.metric("🌧 Rainfall (mm)", round(latest["Rainfall"], 2))
c3.metric("🌱 NDVI Mean", round(latest["NDVI_Mean"], 3))
c4.metric("💰 Modal Price (₹)", round(latest["Modal_x0020_Price"], 2))


st.write("")


# -------------------------------
# CHART 1 – NDVI Trend
# -------------------------------
st.subheader("🛰 NDVI Trend Over Time")

fig1 = px.line(
    filtered_df,
    x="Date",
    y="NDVI_Mean",
    title=f"NDVI Trend for {district}, {state}",
)
st.plotly_chart(fig1, use_container_width=True)


# -------------------------------
# CHART 2 – Price Trend
# -------------------------------
st.subheader("💰 Price Trend Over Time")

fig2 = px.line(
    filtered_df,
    x="Date",
    y="Modal_x0020_Price",
    title=f"Market Price Trend for {district}, {state}",
)
st.plotly_chart(fig2, use_container_width=True)


# -------------------------------
# CHART 3 – District Comparison
# -------------------------------
st.subheader(f"🏙 District Comparison – {state}")

state_df = df[df["State"] == state].groupby("District").mean(numeric_only=True)

fig3 = px.bar(
    state_df,
    x=state_df.index,
    y="Modal_x0020_Price",
    title=f"Average Market Price per District ({state})",
)
st.plotly_chart(fig3, use_container_width=True)
