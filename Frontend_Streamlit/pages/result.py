import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from utils.theme import apply_theme
from utils.language import translate, languages

# -----------------------------
# 1. Init Session States
# -----------------------------
if "theme" not in st.session_state:
    st.session_state.theme = "light"

if "language" not in st.session_state:
    st.session_state.language = "en"

# -----------------------------
# 2. Apply Theme
# -----------------------------
apply_theme(st.session_state.theme)

# -----------------------------
# 3. Language Dropdown
# -----------------------------
st.sidebar.markdown("### 🌐 " + translate("language", st.session_state.language))

selected_lang = st.sidebar.selectbox(
    "",
    list(languages.keys()),
    index=list(languages.keys()).index(st.session_state.language),
)

st.session_state.language = selected_lang

st.set_page_config(page_title="Result – CropWise", layout="wide")

# -----------------------------------
# READ SELECTED STATE & DISTRICT
# -----------------------------------
state = st.session_state.get("selected_state", None)
district = st.session_state.get("selected_district", None)

if not state or not district:
    st.error("⚠ Please go to the Predict page and select State & District first.")
    st.stop()

# -----------------------------------
# MOCK PREDICTION (Replace with backend later)
# -----------------------------------
data = {
    "yield": {
        "monthly": [
            {"month": "Jan", "yield": 150},
            {"month": "Feb", "yield": 180},
            {"month": "Mar", "yield": 210},
            {"month": "Apr", "yield": 260},
        ],
    },
    "rainfall": [
        {"month": "Jan", "rainfall": 55},
        {"month": "Feb", "rainfall": 42},
        {"month": "Mar", "rainfall": 88},
        {"month": "Apr", "rainfall": 120},
    ],
    "ndvi": [
        {"month": "Jan", "ndvi": 0.32},
        {"month": "Feb", "ndvi": 0.48},
        {"month": "Mar", "ndvi": 0.56},
        {"month": "Apr", "ndvi": 0.61},
    ],
    "soil_moisture": 62,
    "suitability": "Suitable",
    "season": "Kharif",
    "recommendation":
        "Ideal conditions for cotton. Maintain irrigation and monitor weather forecasts.",
}

# -----------------------------------
# TITLE
# -----------------------------------
st.markdown(f"""
<h1 style='text-align:center; color:#1c140d;'>🌱 Prediction Result</h1>
<p style='text-align:center; color:#4c3a28;'>
State: <b>{state}</b> &nbsp; | &nbsp; District: <b>{district}</b>
</p>
""", unsafe_allow_html=True)

st.write("")


# -----------------------------------
# TOP CARDS — Suitability, Season, Soil Moisture
# -----------------------------------
col1, col2, col3 = st.columns(3)

# Suitability Card
col1.markdown(f"""
<div style="
    padding:18px; 
    border-radius:12px; 
    background:#f4ede7; 
    border:1px solid #e8dbce;
">
<h3 style="color:#1c140d;">Suitability</h3>
<p style="font-size:22px; font-weight:bold; color:#13ec37;">
{data['suitability']}
</p>
</div>
""", unsafe_allow_html=True)

# Season Card
col2.markdown(f"""
<div style="
    padding:18px; 
    border-radius:12px; 
    background:#f4ede7; 
    border:1px solid #e8dbce;
">
<h3 style="color:#1c140d;">Season</h3>
<p style="font-size:22px; font-weight:bold; color:#1c140d;">
{data['season']}
</p>
</div>
""", unsafe_allow_html=True)

# Soil Moisture Donut
moisture_value = data['soil_moisture']
fig_donut = go.Figure(go.Pie(
    values=[moisture_value, 100 - moisture_value],
    labels=["Moisture", "Remaining"],
    hole=0.65,
))
fig_donut.update_layout(showlegend=False)

col3.plotly_chart(fig_donut, use_container_width=True)


# -----------------------------------
# CHARTS — NDVI, Rainfall, Yield
# -----------------------------------
st.markdown("### 📊 Analysis Charts")

chart_col1, chart_col2 = st.columns(2)

# NDVI Trend
ndvi_df = data["ndvi"]
fig_ndvi = px.line(ndvi_df, x="month", y="ndvi", markers=True,
                   title="NDVI Trend", color_discrete_sequence=["green"])
chart_col1.plotly_chart(fig_ndvi, use_container_width=True)

# Rainfall Chart
rain_df = data["rainfall"]
fig_rain = px.bar(rain_df, x="month", y="rainfall",
                  title="Rainfall (mm)", color_discrete_sequence=["#4c9a59"])
chart_col2.plotly_chart(fig_rain, use_container_width=True)

# Yield Chart
yield_df = data["yield"]["monthly"]
fig_yield = px.line(yield_df, x="month", y="yield", markers=True,
                    title="Predicted Yield (kg/acre)",
                    color_discrete_sequence=["#2d6a4f"])
st.plotly_chart(fig_yield, use_container_width=True)


# -----------------------------------
# Recommendation
# -----------------------------------
st.markdown("""
### 🌟 Recommendation
""")

st.markdown(f"""
<div style="
    background:#eef3e8;
    padding:18px; 
    border-radius:12px; 
    border:1px solid #d8e2c3;
    color:#1c140d;
">
{data['recommendation']}
</div>
""", unsafe_allow_html=True)
