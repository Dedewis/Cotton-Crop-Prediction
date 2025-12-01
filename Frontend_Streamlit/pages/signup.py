# pages/Signup.py

import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from utils.theme import apply_theme
from utils.language import translate, languages

# ---------------------------------------------------------
# Session State Init
# ---------------------------------------------------------
if "theme" not in st.session_state:
    st.session_state.theme = "light"

if "language" not in st.session_state:
    st.session_state.language = "en"

# ---------------------------------------------------------
# Apply Theme
# ---------------------------------------------------------
apply_theme(st.session_state.theme)
theme = st.session_state.theme
lang = st.session_state.language

# ---------------------------------------------------------
# Sidebar Language
# ---------------------------------------------------------
st.sidebar.markdown("### 🌐 " + translate("language", lang))

chosen = st.sidebar.selectbox(
    "",
    list(languages.keys()),
    index=list(languages.keys()).index(lang),
)

st.session_state.language = chosen
lang = chosen

# ---------------------------------------------------------
# Page Config
# ---------------------------------------------------------
st.set_page_config(page_title="CropWise - Signup", layout="wide")

# ---------------------------------------------------------
# Styles
# ---------------------------------------------------------
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Work+Sans:wght@400;500;700;900&family=Noto+Sans:wght@400;500;700;900&display=swap');

html, body, [class*="css"] {{
    font-family: 'Work Sans', 'Noto Sans', sans-serif;
}}

.light-bg {{ background-color: #fcfbf8; color:#1b180d; }}
.dark-bg  {{ background-color: #111; color:#f5f5f5; }}

.light-input {{
    background-color:#f3f0e7 !important;
    color:#1b180d !important;
    border:none !important;
}}

.dark-input {{
    background-color:#333 !important;
    color:#f5f5f5 !important;
    border:none !important;
}}

.signup-btn {{
    background-color:#eebd2b;
    color:#1b180d;
    padding:10px 16px;
    border-radius:10px;
    font-weight:700;
    width:100%;
    text-align:center;
}}
</style>
""", unsafe_allow_html=True)

wrapper_class = "dark-bg" if theme == "dark" else "light-bg"
text_class = "dark-text" if theme == "dark" else "light-text"
input_class = "dark-input" if theme == "dark" else "light-input"

st.markdown(f"<div class='{wrapper_class}' style='min-height:100vh;'>", unsafe_allow_html=True)

# ---------------------------------------------------------
# NAVBAR
# ---------------------------------------------------------
col1, col2 = st.columns([1,5])

with col1:
    st.markdown(f"<h2 style='margin-top:20px;'>CropWise</h2>", unsafe_allow_html=True)

with col2:
    st.markdown(
        f"""
        <div style="display:flex; justify-content:flex-end; gap:28px; margin-top:25px;">
            <p style="margin:0;"><a style="text-decoration:none; color:inherit;">{translate("home", lang)}</a></p>
            <p style="margin:0;"><a style="text-decoration:none; color:inherit;">{translate("about", lang)}</a></p>
            <p style="margin:0;"><a style="text-decoration:none; color:inherit;">{translate("services", lang)}</a></p>
            <p style="margin:0;"><a style="text-decoration:none; color:inherit;">{translate("contact", lang)}</a></p>

            <button 
                onclick="window.location.href='/Login'"
                style="background:#f3f0e7; padding:6px 16px; border-radius:8px; font-weight:700; border:none;">
                {translate("login", lang)}
            </button>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")

# ---------------------------------------------------------
# PAGE TITLE
# ---------------------------------------------------------
st.markdown(
    f"<h2 style='text-align:center; font-size:28px; margin-top:20px;'>{translate('createAccount', lang)}</h2>",
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# INPUT FIELDS
# ---------------------------------------------------------
fields = [
    ("fullName", translate("fullName", lang)),
    ("email", translate("email", lang)),
    ("password", translate("password", lang)),
    ("confirmPassword", translate("confirmPassword", lang)),
]

user = {}

for key, label in fields:
    user[key] = st.text_input(
        label,
        type="password" if "password" in key.lower() else "default",
        placeholder=label,
        key=key,
    )

# ---------------------------------------------------------
# SIGNUP BUTTON
# ---------------------------------------------------------
if st.button(translate("signup", lang), use_container_width=True):
    if not all(user.values()):
        st.error(translate("fillAll", lang))
    elif user["password"] != user["confirmPassword"]:
        st.error(translate("passwordMismatch", lang))
    else:
        st.success(translate("signupSuccess", lang))
        switch_page("Login")

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown(
    f"""
    <p style="text-align:center; margin-top:20px;">
        {translate("alreadyAccount", lang)}
        <a href="/Login" style="color:#5DAF4D; font-weight:700;">
            {translate("login", lang)}
        </a>
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)
