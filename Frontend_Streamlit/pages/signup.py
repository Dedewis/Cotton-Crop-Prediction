# pages/Signup.py

import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from utils.theme import apply_theme
from utils.language import translate, languages

# ---------------------------------------------------------
# 1. PAGE CONFIG (FIRST)
# ---------------------------------------------------------
st.set_page_config(page_title="CropWise - Signup", layout="centered")

# ---------------------------------------------------------
# 2. INIT SESSION STATES
# ---------------------------------------------------------
if "theme" not in st.session_state:
    st.session_state.theme = "light"

if "language" not in st.session_state:
    st.session_state.language = "en"

theme = st.session_state.theme
lang = st.session_state.language

# ---------------------------------------------------------
# 3. APPLY THEME
# ---------------------------------------------------------
apply_theme(theme)
is_dark = theme == "dark"

text_color = "#E6EDF3" if is_dark else "#1C140D"
subtext_color = "#9BA0A8" if is_dark else "#6B6B6B"
card_bg = "#111820" if is_dark else "#FFFFFF"
border_color = "#2A2F36" if is_dark else "#E4E4E4"

# ---------------------------------------------------------
# 4. SIDEBAR — LANGUAGE + THEME
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
theme_choice = st.sidebar.radio("", ["light", "dark"])
st.session_state.theme = theme_choice
apply_theme(theme_choice)

# ---------------------------------------------------------
# 5. GLOBAL CLEANUP CSS (NO BLUE BOXES)
# ---------------------------------------------------------
st.markdown(
    """
    <style>
        div[data-testid="stElementContainer"]:has(> div:empty) {
            display: none !important;
        }
        div[data-testid="stMarkdownContainer"]:empty {
            display: none !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# 6. PAGE TITLE
# ---------------------------------------------------------
st.markdown(
    f"""
    <h1 style="text-align:center; font-size:34px; font-weight:800; color:{text_color}; margin-top:20px;">
        📝 {translate("Create Account", lang)}
    </h1>
    <p style="text-align:center; color:{subtext_color}; margin-top:-5px;">
        {translate("Sign Up Subtext", lang) if "Sign Up Subtext" in languages[lang] else "Create your account to get started."}
    </p>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# 7. CENTERED FORM CARD
# ---------------------------------------------------------
st.markdown(
    f"""
    <div style="
        max-width: 650px;
        margin: auto;
        background: {card_bg};
        padding: 35px 40px;
        border-radius: 20px;
        border: 1px solid {border_color};
        box-shadow: 0px 4px 16px rgba(0,0,0,0.12);
        margin-top: 20px;
    ">
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# 8. INPUT FIELDS
# ---------------------------------------------------------
st.write(f"### {translate('Full Name', lang)}")
name = st.text_input("", placeholder=translate("Full Name", lang))

st.write(f"### {translate('Email', lang)}")
email = st.text_input("", placeholder=translate("Email", lang))

st.write(f"### {translate('Password', lang)}")
password = st.text_input("", type="password", placeholder=translate("Password", lang))

st.write(f"### {translate('Confirm Password', lang)}")
confirm = st.text_input("", type="password", placeholder=translate("Confirm Password", lang))

# ---------------------------------------------------------
# 9. SIGNUP BUTTON
# ---------------------------------------------------------
if st.button(translate("Sign Up", lang), use_container_width=True):
    if not name or not email or not password or not confirm:
        st.error(translate("Fill All", lang))
    elif password != confirm:
        st.error(translate("Password Mismatch", lang))
    else:
        st.success(translate("Sign Up Success", lang))
        switch_page("Login")

# ---------------------------------------------------------
# 10. FOOTER LINK
# ---------------------------------------------------------
st.markdown(
    f"""
    <p style="text-align:center; margin-top: 20px; color:{text_color};">
        {translate("Already Account", lang)}
        <a href="/Login" style="color:#5DAF4D; font-weight:700;">
            {translate("Login", lang)}
        </a>
    </p>
    """,
    unsafe_allow_html=True,
)

st.markdown("</div>", unsafe_allow_html=True)
