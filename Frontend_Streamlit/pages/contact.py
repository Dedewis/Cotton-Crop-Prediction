# pages/Contact.py

import streamlit as st
from utils.theme import apply_theme
from utils.language import translate, languages

# ---------------------------------------------------------
# MUST BE FIRST
# ---------------------------------------------------------
st.set_page_config(page_title="CropWise - Contact Us", layout="centered")

# ---------------------------------------------------------
# Session State Init
# ---------------------------------------------------------
if "theme" not in st.session_state:
    st.session_state.theme = "light"

if "language" not in st.session_state:
    st.session_state.language = "en"

theme = st.session_state.theme
lang = st.session_state.language

# ---------------------------------------------------------
# Apply Theme
# ---------------------------------------------------------
apply_theme(theme)

# ---------------------------------------------------------
# Sidebar Language + Theme
# ---------------------------------------------------------
st.sidebar.markdown("### 🌐 Language")
selected_lang = st.sidebar.selectbox(
    "",
    list(languages.keys()),
    index=list(languages.keys()).index(lang),
)
st.session_state.language = selected_lang
lang = selected_lang

st.sidebar.markdown("### 🎨 Theme")
selected_theme = st.sidebar.radio("", ["light", "dark"])
st.session_state.theme = selected_theme
theme = selected_theme

# ---------------------------------------------------------
# Styling
# ---------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Manrope', sans-serif;
}

.light-bg  { background:#faf9f7; color:#1a1a1a; }
.dark-bg   { background:#0d1115; color:#e6edf3; }

.light-card {
    background:white;
    padding:32px;
    border-radius:16px;
    box-shadow:0 4px 16px rgba(0,0,0,0.06);
}
.dark-card {
    background:#111820;
    padding:32px;
    border-radius:16px;
    box-shadow:0 4px 16px rgba(0,0,0,0.25);
}

input, textarea {
    border-radius:12px !important;
    padding:14px !important;
    font-size:15px !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Page Wrapper
# ---------------------------------------------------------
wrapper_bg = "dark-bg" if theme == "dark" else "light-bg"
card_bg = "dark-card" if theme == "dark" else "light-card"



# ---------------------------------------------------------
# Title
# ---------------------------------------------------------
st.markdown("""
<div style="text-align:center;">
    <h1 style="font-weight:800; font-size:32px;">📩 Contact Us</h1>
    <p style="opacity:0.8; margin-top:-8px;">We're here to help! Reach out anytime.</p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Input helpers
# ---------------------------------------------------------
def labeled_input(label, placeholder="", key="", type="default"):
    st.markdown(
        f"<p style='margin-bottom:6px; font-weight:600; font-size:16px;'>{label}</p>",
        unsafe_allow_html=True
    )
    return st.text_input("", placeholder=placeholder, key=key, type=type)

def labeled_area(label, placeholder="", key=""):
    st.markdown(
        f"<p style='margin-bottom:6px; font-weight:600; font-size:16px;'>{label}</p>",
        unsafe_allow_html=True
    )
    return st.text_area("", placeholder=placeholder, key=key)

# ---------------------------------------------------------
# Contact Form Card
# ---------------------------------------------------------
st.markdown(
    f"<div class='{card_bg}' style='max-width:700px; margin:auto;'>",
    unsafe_allow_html=True
)

name = labeled_input("Full Name", "Enter your full name", "name")

email = labeled_input("Email Address", "Enter your email", "email", type="default")

subject = labeled_input("Subject", "What is this about?", "subject")

message = labeled_area("Message", "Write your message...", "message")

st.write("")
submit = st.button("Send Message", use_container_width=True)

if submit:
    if not name or not email or not subject or not message:
        st.error("Please fill all fields.")
    else:
        st.success("Your message has been sent successfully!")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
