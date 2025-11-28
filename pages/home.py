import streamlit as st
import json

# -----------------------------
# Load India state/district data
# -----------------------------
with open("data/India.json", "r", encoding="utf-8") as f:
    INDIA_DATA = json.load(f)

# -----------------------------
# Language Content
# -----------------------------
LANG = {
    "en": {
        "home": "Home",
        "about": "About",
        "services": "Services",
        "contact": "Contact",
        "get_started": "Get Started",
        "title": "Predict Your Cotton Yield",
        "subtitle": "Maximize your harvest with our advanced prediction system. Enter your crop details and get accurate yield forecasts.",
        "welcome_title": "Welcome to the Cotton Crop Prediction System",
        "welcome_desc": "Cotton, often called 'white gold,' is a globally significant crop. Our system forecasts cotton yields accurately, helping farmers maximize productivity.",
        "enter_details": "Enter Your Crop Details",
        "state": "State",
        "district": "District",
        "predict": "Predict Yield",
    },
    "hi": {
        "home": "मुखपृष्ठ",
        "about": "हमारे बारे में",
        "services": "सेवाएँ",
        "contact": "संपर्क करें",
        "get_started": "शुरू करें",
        "title": "अपनी कपास उपज की भविष्यवाणी करें",
        "subtitle": "उन्नत पूर्वानुमान प्रणाली के साथ अपनी फसल का अधिकतम लाभ उठाएँ।",
        "welcome_title": "कपास उपज पूर्वानुमान प्रणाली में आपका स्वागत है",
        "welcome_desc": "कपास एक महत्वपूर्ण वैश्विक फसल है। यह प्रणाली किसानों को सटीक उपज पूर्वानुमान प्रदान करती है।",
        "enter_details": "अपनी फसल विवरण दर्ज करें",
        "state": "राज्य",
        "district": "ज़िला",
        "predict": "उपज भविष्यवाणी करें",
    },
    "kn": {
        "home": "ಮುಖಪುಟ",
        "about": "ಬಗ್ಗೆ",
        "services": "ಸೇವೆಗಳು",
        "contact": "ಸಂಪರ್ಕಿಸಿ",
        "get_started": "ಪ್ರಾರಂಭಿಸಿ",
        "title": "ನಿಮ್ಮ ಹತ್ತಿ ಉತ್ಪಾದನೆಯನ್ನು ಊಹಿಸಿ",
        "subtitle": "ನಮ್ಮ ಪ್ರಗತಿಶೀಲ ಪೂರ್ವಾನುಮಾನ ವ್ಯವಸ್ಥೆಯಿಂದ ನಿಮ್ಮ ಬೆಳೆ ಉತ್ಪಾದನೆಯನ್ನು ಹೆಚ್ಚಿಸಿ.",
        "welcome_title": "ಹತ್ತಿ ಉತ್ಪಾದನೆ ಪೂರ್ವಾನುಮಾನ ವ್ಯವಸ್ಥೆಗೆ ಸ್ವಾಗತ",
        "welcome_desc": "ಹತ್ತಿ ಒಂದು ಪ್ರಮುಖ ಜಾಗತಿಕ ಬೆಳೆ. ನಮ್ಮ ವ್ಯವಸ್ಥೆ ನಿಖರ ಉತ್ಪಾದನೆ ಪೂರ್ವಾನುಮಾನಗಳನ್ನು ನೀಡುತ್ತದೆ.",
        "enter_details": "ನಿಮ್ಮ ಬೆಳೆ ವಿವರಗಳನ್ನು ನಮೂದಿಸಿ",
        "state": "ರಾಜ್ಯ",
        "district": "ಜಿಲ್ಲೆ",
        "predict": "ಉತ್ಪಾದನೆ ಊಹಿಸಿ",
    }
}

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="CropWise", layout="wide")

# -----------------------------
# SIDEBAR — Theme + Language
# -----------------------------
st.sidebar.header("⚙️ Settings")

theme = st.sidebar.radio("Theme", ["Light", "Dark"])
lang = st.sidebar.selectbox("Language", ["en", "hi", "kn"])

t = LANG[lang]

# -----------------------------
# Apply Dark Theme Styling
# -----------------------------
if theme == "Dark":
    st.markdown("""
        <style>
            body { background-color: #0d1b10; color: white; }
            .stSelectbox > div > div { background: #1e2b1f !important; color: white; }
            .stButton button { background:#1ad64d; color:black; font-weight:700; }
            .title-text { color:white !important; }
            .sub-text { color:#d7e8d8 !important; }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
            body { background-color: #f8fcf9; color:#0d1b10; }
            .title-text { color:#0d1b10 !important; }
            .sub-text { color:#4b5c4b !important; }
        </style>
    """, unsafe_allow_html=True)

# -----------------------------
# NAVBAR
# -----------------------------
st.markdown(f"""
    <div style='display:flex; justify-content:space-between; 
                padding:12px 40px; border-bottom:1px solid #e7f3e9;'>
        <div style='display:flex; align-items:center; gap:8px;'>
            <span style='font-size:20px; font-weight:700;'>CropWise</span>
        </div>
        <div style='display:flex; gap:25px; font-size:15px;'>
            <a href='#' style='text-decoration:none; color:inherit;'>{t['home']}</a>
            <a href='#' style='text-decoration:none; color:inherit;'>{t['about']}</a>
            <a href='#' style='text-decoration:none; color:inherit;'>{t['services']}</a>
            <a href='#' style='text-decoration:none; color:inherit;'>{t['contact']}</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# -----------------------------
# HERO SECTION
# -----------------------------
st.markdown(f"""
<div style='background-image:
linear-gradient(rgba(0,0,0,0.1), rgba(0,0,0,0.4)),
url("https://lh3.googleusercontent.com/aida-public/AB6AXuDcBnoyswmC_vRaKxkrNukCKAnVK4naU17otfZ9QhqJwqMhfzPoh_ZX_Nn6gmJcsQ0BQS4Wz1RftQvjtMtJug-uRrqKkj2ckA-UCaIQphgF-0fGSSLHlmFvjHwQpvZLFNacINvSvBGx8Kb9nrQa6z7ntj90w_URmSmapsVcO2cswlB2vatmj6SAUt-3POxCCcZDtLQIcn-I6v3neG9SMdI_8SiC0PbY1T2rJpV8VyqfSCcOGR7iN3OSI8X0KAE5BWTOvuicAFg-24E");
     height:420px; border-radius:12px; background-size:cover;
     display:flex; flex-direction:column; align-items:center; justify-content:center; gap:12px;'>
    <h1 class='title-text' style='font-size:42px; font-weight:900; text-align:center;'>{t['title']}</h1>
    <p class='sub-text' style='font-size:16px; max-width:600px; text-align:center;'>{t['subtitle']}</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# -----------------------------
# CONTENT SECTION
# -----------------------------
st.subheader(t["welcome_title"])
st.write(t["welcome_desc"])

st.subheader(t["enter_details"])

# -----------------------------
# STATE & DISTRICT SELECT
# -----------------------------
state_list = sorted([item["state"] for item in INDIA_DATA])
selected_state = st.selectbox(t["state"], state_list)

district_list = []
for item in INDIA_DATA:
    if item["state"] == selected_state:
        district_list = item["districts"]
        break

selected_district = st.selectbox(t["district"], district_list)

# -----------------------------
# BUTTON
# -----------------------------
if st.button(t["predict"]):
    st.success(f"✅ Yield prediction initiated for **{selected_district}, {selected_state}**.")
