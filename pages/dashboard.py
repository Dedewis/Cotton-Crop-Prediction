import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import json

# ----------------------------------
# PAGE CONFIG
# ----------------------------------
st.set_page_config(page_title="Cotton Dashboard", layout="wide")

# ----------------------------------
# LOAD TRANSLATIONS
# ----------------------------------
with open("translations/translations.json", "r", encoding="utf-8") as f:
    translations = json.load(f)

def t(key):
    lang = st.session_state.get("lang", "en")
    parts = key.split(".")
    value = translations.get(lang, {})
    for p in parts:
        value = value.get(p, p)
    return value

# ----------------------------------
# LOAD DATA (CSV)
# ----------------------------------
DATA_PATH = "data/mandi_data_with_ndvi_weather.csv"

try:
    df = pd.read_csv(DATA_PATH)
except:
    st.error("❌ CSV file not found! Please place 'mandi_data_with_ndvi_weather.csv' inside the data/ folder.")
    st.stop()

# ----------------------------------
# SIDEBAR INPUT
# ----------------------------------
st.sidebar.title("🔍 Filter Data")

states = sorted(df["State"].dropna().unique())
state = st.sidebar.selectbox("Select State", states)

districts = sorted(df[df["State"] == state]["District"].dropna().unique())
district = st.sidebar.selectbox("Select District", districts)

st.sidebar.markdown("---")
st.sidebar.write("Prediction will be added after backend.")

# ----------------------------------
# PAGE TITLE
# ----------------------------------
st.markdown(
    f"""
    <h1 style="margin-bottom:0">{t("dashboard.heading")}</h1>
    <p style="color:#4c3a28">Interactive analysis of NDVI, Price, Rainfall and District comparisons.</p>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------
# TOP CARDS (Mock until backend arrives)
# ----------------------------------
st.subheader("📊 Key Insights (Temporary Mock Values)")

col1, col2, col3 = st.columns(3)

col1.metric("Predicted Price (Mock)", "₹ 5420")
col2.metric("Expected Profit (Mock)", "₹ 1375")
col3.metric("Avg Temperature (°C)", "29.4")

col4, col5 = st.columns(2)
col4.metric("NDVI Mean (Mock)", "0.56")
col5.metric("Commodity", "Cotton")

st.markdown("---")

# ----------------------------------
# NDVI vs PRICE SCATTER
# ----------------------------------
st.subheader("🌱 NDVI vs Market Price")

scatter_fig = px.scatter(
    df,
    x="NDVI_Mean",
    y="Modal_x0020_Price",
    color="State",
    title="NDVI vs Price Relationship",
    height=500
)
scatter_fig.update_layout(margin=dict(l=10, r=10, b=10, t=40))
st.plotly_chart(scatter_fig, use_container_width=True)

# ----------------------------------
# DISTRICT-WISE PRICE BAR CHART
# ----------------------------------
st.subheader(f"🏙 Average Price Comparison — {state}")

district_df = (
    df[df["State"] == state]
    .groupby("District")
    .mean(numeric_only=True)
    .reset_index()
)

bar_fig = px.bar(
    district_df,
    x="District",
    y="Modal_x0020_Price",
    title=f"Average Cotton Prices Across Districts in {state}",
    color="District",
    height=500
)
bar_fig.update_layout(showlegend=False)
st.plotly_chart(bar_fig, use_container_width=True)

# ----------------------------------
# NDVI TREND (Altair)
# ----------------------------------
st.subheader("📈 NDVI Trend Over Time (Filtered District)")

try:
    ndvi_trend = df[df["District"] == district][["Date", "NDVI_Mean"]]
    ndvi_trend["Date"] = pd.to_datetime(ndvi_trend["Date"])

    trend_chart = (
        alt.Chart(ndvi_trend)
        .mark_line(point=True)
        .encode(
            x="Date:T",
            y="NDVI_Mean:Q",
            tooltip=["Date", "NDVI_Mean"]
        )
        .properties(height=350)
    )

    st.altair_chart(trend_chart, use_container_width=True)

except:
    st.info("No NDVI trend data available for this district.")

# ----------------------------------
# RAINFALL TREND
# ----------------------------------
st.subheader("🌧 Rainfall Trend (If Available)")

if "Rainfall" in df.columns:
    rain_df = df[df["District"] == district][["Date", "Rainfall"]]
    rain_df["Date"] = pd.to_datetime(rain_df["Date"])

    rain_chart = (
        alt.Chart(rain_df)
        .mark_area(opacity=0.6)
        .encode(
            x="Date:T",
            y="Rainfall:Q",
            tooltip=["Date", "Rainfall"]
        )
        .properties(height=350)
    )

    st.altair_chart(rain_chart, use_container_width=True)
else:
    st.info("No rainfall column found in dataset.")

st.markdown("---")
st.success("Dashboard loaded successfully ✔")
