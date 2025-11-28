import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from utils.language import t

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="CropWise - About", layout="wide")

# Load fonts
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Lexend:wght@400;500;700;900&family=Noto+Sans:wght@400;500;700;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Lexend', 'Noto Sans', sans-serif;
}
</style>
""", unsafe_allow_html=True)

# ------------------ NAVBAR ------------------
st.markdown("""
<style>
.navbar {
    display: flex;
    justify-content: space-between;
    padding: 12px 40px;
    border-bottom: 1px solid #e8efe8;
}
.nav-links a {
    margin-right: 25px;
    font-size: 15px;
    color: var(--text);
    text-decoration: none;
    font-weight: 500;
}
.brand-title {
    font-size: 20px;
    font-weight: 700;
    color: var(--text);
}
.get-btn {
    background:#298621;
    padding: 8px 20px;
    border-radius: 999px;
    color: white;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="navbar">
    <div class="brand-title">🌾 CropWise</div>
    <div class="nav-links">
        <a href="/">Home</a>
        <a href="/Predict">Prediction</a>
        <a href="/About">About</a>
        <a href="/Contact">Contact</a>
    </div>
    <div class="get-btn">Get Started</div>
</div>
""", unsafe_allow_html=True)

# ------------------ PAGE TITLE ------------------
st.markdown("""
<h1 style='font-size:32px; font-weight:800; margin-top:25px; color:var(--text);'>
    About CropWise
</h1>
""", unsafe_allow_html=True)

# ------------------ SECTION: MISSION ------------------
st.markdown("""
### Our Mission
At CropWise, our mission is to empower cotton farmers with accurate and timely crop predictions.
We use advanced data analytics and machine learning techniques to help farmers optimize their
farming practices, improve yields, and enhance their livelihoods.
""")

# ------------------ SECTION: WHY COTTON MATTERS ------------------
st.markdown("""
### Why Cotton Farming Matters
Cotton farming plays a crucial role in the global economy, supporting millions of livelihoods.
However, cotton cultivation faces challenges such as unpredictable weather, pest attacks,
and fluctuating market prices. Accurate predictions help farmers take preventive action and
maximize productivity.
""")

# ------------------ SECTION: HOW SYSTEM WORKS ------------------
st.markdown("""
### How Our Prediction System Works
Our system combines:
- 📊 Historical crop data  
- 🌦 Real-time weather  
- 🛰 Satellite NDVI  
- 🤖 Machine learning models  

All these inputs are processed to provide reliable cotton yield predictions.
""")

# ------------------ IMAGE BLOCK ------------------
st.markdown("""
<div style='text-align:center; padding:20px 0;'>
    <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuCa6e8OveXU8O8arm0ElSFH4LT6rQjNsVb0ZRZ-pRZrBJLK2X3-FV6ssL6yUHXQ_4nILqljr-S6eHlMcsEGBlpmd_vRt-0gxKbRQNWBOUSycczpmwgj5n3pq21c2exV-UQ5YxF-v2ldgIbiSRPnO9NUXYHPtnEF8eXuveBRa13N3jSgIkXzCIp-c6PTX4nDjF2vSYM7BFbdbITj5IAYA5K9kFpqkvxFgI49H1v6G2qJT2G_yAcxuB-FTw4nmdStEyJx0gqcEehhBV8"
         style="border-radius:12px; max-width:100%; height:auto;">
</div>
""", unsafe_allow_html=True)

# ------------------ BENEFITS ------------------
st.markdown("""
### Benefits of Using CropWise
- ✔ Better decision-making  
- ✔ Risk mitigation  
- ✔ Higher productivity  
- ✔ Increased profitability  
- ✔ Sustainable farming  
""")

# ------------------ TEAM ------------------
st.markdown("""
### Our Team
Our team includes experts in agriculture, data science, and AI engineering.
We are committed to helping farmers succeed using modern technology.
""")

# ------------------ CTA BUTTON ------------------
st.markdown("""
<div style="padding: 20px 0;">
    <a href="/Contact">
        <button style="
            background:#298621; 
            color:white;
            padding:10px 25px;
            border-radius:999px;
            font-weight:700;
            border:none;
            cursor:pointer;">
            Contact Us
        </button>
    </a>
</div>
""", unsafe_allow_html=True)
