import streamlit as st
from utils.language import translate, languages
from utils.theme import apply_theme

# ----------------------------------------------------------
# SESSION STATE
# ----------------------------------------------------------
if "language" not in st.session_state:
    st.session_state.language = "en"

if "theme" not in st.session_state:
    st.session_state.theme = "light"

# ----------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------
st.set_page_config(
    page_title="CropWise",
    page_icon="🌾",
    layout="wide"
)

# APPLY THEME
apply_theme(st.session_state.theme)

lang = st.session_state.language

# ----------------------------------------------------------
# SIDEBAR LAYOUT
# ----------------------------------------------------------
with st.sidebar:
    st.markdown("<h2>🌾 CropWise</h2>", unsafe_allow_html=True)

    # Language Selector
    st.subheader(translate("language", lang))
    selected_language = st.selectbox(
        "",
        list(languages.keys()),
        index=list(languages.keys()).index(lang),
        format_func=lambda x: languages[x],
    )
    st.session_state.language = selected_language
    lang = selected_language

    # Theme selector
    st.subheader(translate("theme", lang))
    theme_option = st.radio("", ["light", "dark"])
    st.session_state.theme = theme_option

    st.markdown("---")

    # PAGE LINKS (must match file names inside /pages/)
    st.page_link("pages/Home.py", label="Home")
    st.page_link("pages/About.py", label="About")
    st.page_link("pages/Community.py", label="Community")
    st.page_link("pages/Contact.py", label="Contact")
    st.page_link("pages/Dashboard.py", label="Dashboard")
    st.page_link("pages/Login.py", label="Login")
    st.page_link("pages/Predict.py", label="Predict")
    st.page_link("pages/Profile.py", label="Profile")
    st.page_link("pages/ResetPassword.py", label="Reset Password")
    st.page_link("pages/Resources.py", label="Resources")
    st.page_link("pages/Result.py", label="Result")
    st.page_link("pages/Settings.py", label="Settings")
    st.page_link("pages/Signup.py", label="Signup")

# ----------------------------------------------------------
# MAIN SCREEN CONTENT
# ----------------------------------------------------------
st.markdown(
    f"""
    <h1 style='font-size:44px; font-weight:900;'>🌱 CropWise</h1>
    <p style='font-size:18px; opacity:0.8;'>
        Welcome to CropWise — your intelligent cotton farming assistant.
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

st.markdown(
    """
    <div style="
        padding: 20px;
        border-radius: 12px;
        background: rgba(0,0,0,0.05);
        font-size:17px;
        line-height:1.7;
    ">
        CropWise helps cotton farmers make data-driven decisions with:
        <ul>
            <li>📊 Accurate cotton yield predictions</li>
            <li>🌦 Weather forecasting</li>
            <li>🛰 Satellite NDVI analysis</li>
            <li>📚 Farming knowledge bank</li>
            <li>🤝 Farmer community discussions</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)
