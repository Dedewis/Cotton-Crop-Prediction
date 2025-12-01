import streamlit as st
from utils.theme import apply_theme
from utils.language import translate, languages
import requests
from streamlit_extras.switch_page_button import switch_page

# -----------------------------
# Page Setup
# -----------------------------
st.set_page_config(page_title="CropWise – Predict", layout="wide")

if "theme" not in st.session_state:
    st.session_state.theme = "light"
if "language" not in st.session_state:
    st.session_state.language = "en"

theme = st.session_state.theme
lang = st.session_state.language

# translation helper
def t(key):
    return translate(key, st.session_state.language)

apply_theme(theme)

# -----------------------------
# Title
# -----------------------------
st.markdown(
    f"""
    <h1 style="font-weight:900; font-size:35px;">
        🌾 {t("predict")}
    </h1>
    <p style="opacity:0.8;">{t("predict_sub")}</p>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Input Fields
# -----------------------------
st.subheader(t("select_location"))

states = ["Maharashtra", "Gujarat", "Telangana", "Andhra Pradesh", "Karnataka", "Tamil Nadu"]
selected_state = st.selectbox(t("state"), states)

districts = {
    "Maharashtra": ["Akola", "Amravati", "Buldhana"],
    "Gujarat": ["Surat", "Rajkot", "Vadodara"],
    "Telangana": ["Adilabad", "Nizamabad"],
    "Andhra Pradesh": ["Guntur", "Nellore"],
    "Karnataka": ["Dharwad", "Gadag"],
    "Tamil Nadu": ["Coimbatore", "Salem"]
}

selected_district = st.selectbox(
    t("district"),
    districts.get(selected_state, [])
)

# -----------------------------
# Predict Button
# -----------------------------
if st.button(t("predict"), use_container_width=True):

    # Save values for Dashboard
    st.session_state.selected_state = selected_state
    st.session_state.selected_district = selected_district

    st.success(f"✅ {t('success')} {selected_district}, {selected_state}")

    # Redirect → Dashboard
    switch_page("Dashboard")

