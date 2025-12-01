import streamlit as st
from utils.theme import apply_theme
from utils.language import translate, languages

# -----------------------------  
# SESSION STATE  
# -----------------------------  
if "theme" not in st.session_state:
    st.session_state.theme = "light"
if "language" not in st.session_state:
    st.session_state.language = "en"

# Apply theme  
apply_theme(st.session_state.theme)

# -----------------------------  
# SIDEBAR  
# -----------------------------  
with st.sidebar:
    st.title("🌾 CropWise")

    # Language selector
    st.subheader(translate("language", st.session_state.language))
    st.session_state.language = st.selectbox(
        "",
        list(languages.keys()),
        index=list(languages.keys()).index(st.session_state.language),
        format_func=lambda x: languages[x]
    )

    # Theme selector
    st.subheader(translate("theme", st.session_state.language))
    st.session_state.theme = st.radio(
        "",
        ["light", "dark"],
        index=0 if st.session_state.theme == "light" else 1
    )

# -----------------------------  
# PAGE STYLES  
# -----------------------------  
st.markdown("""
<style>
.center-container {
    max-width: 900px;
    margin-left: auto;
    margin-right: auto;
    padding: 25px;
}

.section-title {
    font-size: 32px;
    font-weight: 800;
    margin-bottom: 15px;
}

.section-box {
    background: rgba(0,0,0,0.03);
    padding: 20px 25px;
    border-radius: 12px;
    margin-bottom: 35px;
}

.section-box ul li {
    margin-bottom: 10px;
    font-size: 17px;
}

.section-box p {
    font-size: 17px;
}

img.hero-img {
    border-radius: 12px;
    max-width: 100%;
    height: auto;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='center-container'>", unsafe_allow_html=True)

# -----------------------------  
# PAGE TITLE  
# -----------------------------  
st.markdown("<h1 class='section-title'>🌿 About CropWise</h1>", unsafe_allow_html=True)

# -----------------------------  
# ABOUT SECTION  
# -----------------------------  
st.markdown("""
<div class="section-box">
<p><strong>CropWise</strong> is an intelligent Cotton Crop Yield Prediction System built to help
farmers make informed crop decisions using AI and data-driven insights.</p>

<p>Using machine learning, remote sensing, satellite NDVI, and real-time weather analytics,
CropWise provides accurate yield predictions and early risk alerts—helping farmers improve
productivity and reduce losses.</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------  
# OUR MISSION  
# -----------------------------  
st.markdown("<h2 class='section-title'>🌱 Our Mission</h2>", unsafe_allow_html=True)

st.markdown("""
<div class="section-box">
<p>Our mission is to empower cotton farmers with easy-to-use digital tools that enable:</p>

<ul>
<li>✔ Smarter decision-making</li>
<li>✔ Reduced dependency on unpredictable weather</li>
<li>✔ Improved pest and disease management</li>
<li>✔ Better planning for sowing, irrigation & harvesting</li>
</ul>

<p>Agriculture is becoming unpredictable, and CropWise aims to provide stability through
accurate, actionable insights.</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------  
# WHY COTTON MATTERS  
# -----------------------------  
st.markdown("<h2 class='section-title'>🧵 Why Cotton Matters</h2>", unsafe_allow_html=True)

st.markdown("""
<div class="section-box">
<p>Cotton is one of India's most crucial crops, supporting millions of farmers.  
However, cotton production faces several major challenges:</p>

<ul>
<li>🌦 Unpredictable monsoon patterns</li>
<li>🐛 Pest attacks (bollworm, whitefly)</li>
<li>🌱 Soil nutrient imbalance</li>
<li>💸 Fluctuating market prices</li>
<li>🌡 Rising temperatures due to climate change</li>
</ul>
</div>
""", unsafe_allow_html=True)

# -----------------------------  
# HOW CROPWISE WORKS  
# -----------------------------  
st.markdown("<h2 class='section-title'>🤖 How CropWise Works</h2>", unsafe_allow_html=True)

st.markdown("""
<div class="section-box">
<p>CropWise analyzes various agricultural inputs to generate accurate predictions:</p>

<ul>
<li>📊 Historical yield patterns</li>
<li>🛰 Satellite NDVI vegetation index</li>
<li>🌦 Weather forecasting (rainfall, humidity, temperature)</li>
<li>🌱 Soil fertility and pH variation</li>
<li>🤖 Machine Learning prediction models</li>
</ul>
</div>
""", unsafe_allow_html=True)

# -----------------------------  
# IMAGE  
# -----------------------------  
st.markdown("""
<div style='text-align:center; padding:20px 0;'>
    <img class="hero-img" 
         src="https://lh3.googleusercontent.com/aida-public/AB6AXuCa6e8OveXU8O8arm0ElSFH4LT6rQjNsVb0ZRZ-pRZrBJLK2X3-FV6ssL6yUHXQ_4nILqljr-S6eHlMcsEGBlpmd_vRt-0gxKbRQNWBOUSycczpmwgj5n3pq21c2exV-UQ5YxF-v2ldgIbiSRPnO9NUXYHPtnEF8eXuveBRa13N3jSgIkXzCIp-c6PTX4nDjF2vSYM7BFbdbITj5IAYA5K9kFpqkvxFgI49H1v6G2qJT2G_yAcxuB-FTw4nmdStEyJx0gqcEehhBV8">
</div>
""", unsafe_allow_html=True)

# -----------------------------  
# BENEFITS  
# -----------------------------  
st.markdown("<h2 class='section-title'>⭐ Benefits of CropWise</h2>", unsafe_allow_html=True)

st.markdown("""
<div class="section-box">
<ul>
<li>✔ Accurate yield predictions powered by ML</li>
<li>✔ Reduced farming risks and input costs</li>
<li>✔ Improved sowing & harvesting decisions</li>
<li>✔ NDVI-based crop health insights</li>
<li>✔ Better long-term planning for farmers</li>
</ul>
</div>
""", unsafe_allow_html=True)

# -----------------------------  
# CTA  
# -----------------------------  
st.markdown("""
<div style="text-align:center; padding-top:20px;">
    <a href="/Contact">
        <button style="
            background:#2c8a2c; 
            color:white;
            padding:10px 25px;
            border-radius:999px;
            font-weight:700;
            border:none;
            cursor:pointer;">
            📩 Contact Us
        </button>
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
