import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from utils.theme import apply_theme
from utils.language import translate, languages

# ---------------------------------------------------------
# PAGE CONFIG (MUST BE FIRST)
# ---------------------------------------------------------
st.set_page_config(page_title="CropWise - Login", layout="wide")

# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------
if "theme" not in st.session_state:
    st.session_state.theme = "light"

if "language" not in st.session_state:
    st.session_state.language = "en"

apply_theme(st.session_state.theme)

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------
with st.sidebar:
    st.title("🌾 CropWise")

    st.subheader("Language")
    st.session_state.language = st.selectbox(
        "",
        list(languages.keys()),
        index=list(languages.keys()).index(st.session_state.language),
        format_func=lambda x: languages[x]
    )

    st.subheader("Theme")
    st.session_state.theme = st.radio(
        "",
        ["light", "dark"],
        index=0 if st.session_state.theme == "light" else 1
    )

# ---------------------------------------------------------
# THEME COLORS
# ---------------------------------------------------------
is_dark = st.session_state.theme == "dark"

BG = "#0d1115" if is_dark else "#f5f5f3"
CARD_BG = "#111820" if is_dark else "#ffffff"
TEXT = "#e6edf3" if is_dark else "#1c140d"
MUTED = "#c59f74" if is_dark else "#9c7349"
INPUT_BG = "#0f1820" if is_dark else "#ffffff"
INPUT_BORDER = "#2a2f36" if is_dark else "#d8cfc4"

# ---------------------------------------------------------
# PAGE STYLES
# ---------------------------------------------------------
st.markdown(f"""
<style>
body {{
    background-color: {BG} !important;
}}

.center-wrapper {{
    display: flex;
    justify-content: center;
    align-items: flex-start;
    padding-top: 60px;
}}

.center-container {{
    width: 480px;
    background: {CARD_BG};
    padding: 40px;
    border-radius: 18px;
    border: 1px solid {INPUT_BORDER};
    box-shadow: 0px 4px 14px rgba(0,0,0,0.12);
}}

h1 {{
    text-align: center;
    font-weight: 800;
    font-size: 28px;
    margin-bottom: 25px;
    color: {TEXT};
}}

.label {{
    font-weight: 600;
    color: {TEXT};
    margin-bottom: 5px;
    font-size: 15px;
}}

.stTextInput > div > div > input {{
    background: {INPUT_BG} !important;
    color: {TEXT} !important;
    border: 1.4px solid {INPUT_BORDER} !important;
    padding: 13px !important;
    border-radius: 12px !important;
}}

.button-main {{
    background: #E6B31E;
    color: #1a1a1a;
    padding: 12px;
    font-size: 17px;
    font-weight: 700;
    border-radius: 10px;
    width: 100%;
    cursor: pointer;
    margin-top: 10px;
}}

.button-main:hover {{ background: #f3c846; }}

.button-outline {{
    background: #ffe28a;
    color: #1a1a1a;
    padding: 12px;
    font-size: 17px;
    font-weight: 700;
    border-radius: 10px;
    width: 100%;
    cursor: pointer;
    margin-top: 12px;
}}

.forgot {{
    text-align: right;
    margin-bottom: 10px;
}}

.forgot a {{
    color: #4f9f5b;
    font-size: 14px;
    text-decoration: none;
}}

.forgot a:hover {{
    text-decoration: underline;
}}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# LOGIN CONTAINER
# ---------------------------------------------------------
st.markdown("<div class='center-wrapper'>", unsafe_allow_html=True)


# Title
st.markdown("<h1>🔐 Login to CropWise</h1>", unsafe_allow_html=True)

# Email Field
st.markdown("<p class='label'>Email Address</p>", unsafe_allow_html=True)
email = st.text_input("", placeholder="Enter your email")

# Password Field
st.markdown("<p class='label'>Password</p>", unsafe_allow_html=True)
password = st.text_input("", placeholder="Enter your password", type="password")

# Forgot Password
st.markdown(
    "<div class='forgot'><a href='/ResetPassword'>Forgot Password?</a></div>",
    unsafe_allow_html=True
)

# Login Button
if st.button("Login", key="login_btn"):
    if email.strip() == "" or password.strip() == "":
        st.error("Please enter your email and password.")
    else:
        switch_page("Dashboard")

# Signup Button
if st.button("Sign Up", key="signup_btn"):
    switch_page("Signup")

st.markdown("</div></div>", unsafe_allow_html=True)
