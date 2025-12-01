import streamlit as st
from utils.theme import apply_theme

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="CropWise – Home", layout="wide")

if "theme" not in st.session_state:
    st.session_state.theme = "light"

if "language" not in st.session_state:
    st.session_state.language = "en"

theme = st.session_state.theme
lang = st.session_state.language

apply_theme(theme)

# Color based on theme
text_color = "#ffffff" if theme == "dark" else "#1a1a1a"
card_bg = "rgba(255,255,255,0.1)" if theme == "dark" else "rgba(0,0,0,0.05)"

# -----------------------------
# TITLE SECTION
# -----------------------------
st.markdown(
    f"""
    <div style='text-align:center; padding-top:10px;'>
        <h1 style='color:{text_color}; font-size:45px; font-weight:900;'>🌾 CropWise</h1>
        <p style='color:{text_color}; opacity:0.85; font-size:18px;'>
            AI-powered cotton yield prediction and smart farming assistant.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# INTRODUCTION BLOCK
# -----------------------------
st.markdown(
    f"""
    <div style="
        padding: 22px;
        background:{card_bg};
        border-radius:12px;
        color:{text_color};
        font-size:16px;
        line-height:1.6;
    ">
        <b>CropWise</b> helps cotton farmers make data-driven decisions using:
        <ul>
            <li>📈 AI-based cotton yield predictions</li>
            <li>🌦 Real-time weather forecasting</li>
            <li>🛰 NDVI & vegetation health monitoring</li>
            <li>🌱 Soil moisture and nutrient indicators</li>
            <li>🐛 Pest & disease surveillance</li>
            <li>🔄 Crop rotation & soil improvement suggestions</li>
        </ul>
        Designed to empower farmers with accurate, location-specific insights.
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# -----------------------------
# COTTON GROWTH STAGES
# -----------------------------
st.markdown(
    f"<h2 style='color:{text_color}; margin-top:20px;'>🌾 Cotton Crop Growth Stages</h2>",
    unsafe_allow_html=True
)

s1, s2, s3, s4 = st.columns(4)

for col, title, desc in [
    (s1, "🌱 Germination", "Seed sprouts and begins development."),
    (s2, "🌿 Vegetative", "Leaf and branch development begins."),
    (s3, "🌸 Flowering", "Blooming and pollination stage."),
    (s4, "🧺 Boll Formation", "Cotton bolls grow before harvest.")
]:
    col.markdown(
        f"""
        <div style="padding:15px; background:{card_bg}; border-radius:10px; color:{text_color}; text-align:center;">
            <h4>{title}</h4>
            <p>{desc}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")

# -----------------------------
# NDVI EXPLANATION
# -----------------------------
st.markdown(
    f"<h2 style='color:{text_color}; margin-top:25px;'>🛰 NDVI – Vegetation Index</h2>",
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div style="padding:20px; background:{card_bg}; border-radius:12px; color:{text_color}; line-height:1.6;">
        NDVI helps measure plant health using satellite imagery.
        <br><br>
        <b>NDVI Ranges:</b>
        <ul>
            <li>🌿 <b>0.6 – 0.9</b> Healthy vegetation</li>
            <li>🍃 <b>0.3 – 0.6</b> Moderate health</li>
            <li>🍂 <b>0.1 – 0.3</b> Stressed vegetation</li>
        </ul>
        Lower NDVI alerts farmers about crop stress due to pests, water shortage, or disease.
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# -----------------------------
# WEATHER IMPACT SECTION
# -----------------------------
st.markdown(
    f"<h2 style='color:{text_color}; margin-top:25px;'>🌦 Weather Factors Affecting Cotton</h2>",
    unsafe_allow_html=True
)

w1, w2, w3 = st.columns(3)

for col, title, desc in [
    (w1, "🌡 Temperature", "Optimal: 21–30°C. Extreme heat reduces boll growth."),
    (w2, "🌧 Rainfall", "Too much rain causes fungal issues; too little reduces yield."),
    (w3, "💨 Humidity", "High humidity promotes pests and fungal diseases."),
]:
    col.markdown(
        f"""
        <div style="padding:18px; background:{card_bg}; border-radius:10px; text-align:center; color:{text_color};">
            <h4>{title}</h4>
            <p>{desc}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")

# -----------------------------
# SOIL & FERTILITY
# -----------------------------
st.markdown(
    f"<h2 style='color:{text_color}; margin-top:25px;'>🌱 Soil Requirements & Fertility</h2>",
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div style="padding:20px; background:{card_bg}; border-radius:12px; color:{text_color}; line-height:1.6;">
        <b>Ideal Cotton Soil:</b>
        <ul>
            <li>Black soil / Loamy soil</li>
            <li>pH 5.8 – 8.0</li>
            <li>High nutrient content with proper drainage</li>
        </ul>

        <b>Improve Soil Fertility:</b>
        <ul>
            <li>Apply compost and organic manure</li>
            <li>Use legumes for nitrogen fixation</li>
            <li>Conduct soil testing for NPK balance</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# -----------------------------
# CROP ROTATION SECTION
# -----------------------------
st.markdown(
    f"<h2 style='color:{text_color}; margin-top:25px;'>🔄 Suggested Crop Rotation After Cotton</h2>",
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div style="padding:18px; background:{card_bg}; border-radius:12px; color:{text_color}; line-height:1.6;">
        Plant these crops after cotton to restore soil health:
        <ul>
            <li>🌱 Green gram</li>
            <li>🌱 Black gram</li>
            <li>🌱 Cowpea</li>
            <li>🌱 Red gram</li>
            <li>🌾 Sorghum (Jowar)</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# -----------------------------
# PEST & DISEASE SECTION
# -----------------------------
st.markdown(
    f"<h2 style='color:{text_color}; margin-top:25px;'>🐛 Pest & Disease Surveillance</h2>",
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div style="padding:18px; background:{card_bg}; border-radius:12px; color:{text_color}; line-height:1.6;">
        Common cotton threats include:
        <ul>
            <li>🦋 Pink Bollworm</li>
            <li>🦗 Aphids</li>
            <li>🕷 Mites</li>
            <li>🍂 Leaf spot disease</li>
            <li>🌿 Fusarium wilt</li>
        </ul>
        CropWise detects early risk signals using weather, humidity & NDVI patterns.
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")
