import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from utils.theme import apply_theme
from utils.language import translate, languages

# ---------------------------------------------------------
# 1. SET PAGE CONFIG FIRST
# ---------------------------------------------------------
st.set_page_config(page_title="CropWise - Reset Password", layout="centered")


# ---------------------------------------------------------
# 2. INITIALIZATION
# ---------------------------------------------------------
if "theme" not in st.session_state:
    st.session_state.theme = "light"

if "language" not in st.session_state:
    st.session_state.language = "en"


# ---------------------------------------------------------
# 3. APPLY THEME
# ---------------------------------------------------------
apply_theme(st.session_state.theme)
is_dark = st.session_state.theme == "dark"

# Color palette
text_color = "#E6EDF3" if is_dark else "#1C140D"
subtext_color = "#A5A5A5" if is_dark else "#6B6B6B"
card_bg = "#111820" if is_dark else "#FFFFFF"
border_color = "#2A2F36" if is_dark else "#E8E8E8"


# ---------------------------------------------------------
# 4. SIDEBAR (Language + Theme)
# ---------------------------------------------------------
st.sidebar.markdown("### 🌐 Language")
selected_lang = st.sidebar.selectbox(
    "",
    list(languages.keys()),
    index=list(languages.keys()).index(st.session_state.language),
)
st.session_state.language = selected_lang

st.sidebar.markdown("### 🎨 Theme")
theme_choice = st.sidebar.radio("", ["light", "dark"])
st.session_state.theme = theme_choice
apply_theme(theme_choice)


# ---------------------------------------------------------
# 5. GLOBAL UI FIXES
# ---------------------------------------------------------
# Notice all CSS % symbols are escaped as %% !!
st.markdown(f"""
    <style>
        div[data-testid="stElementContainer"]:has(> div:empty) {{
            display: none !important;
        }}
        div[data-testid="stMarkdownContainer"]:empty {{
            display: none !important;
        }}

        .center-box {{
            max-width: 650px;
            margin: auto;
            background: {card_bg};
            padding: 35px 40px;
            border-radius: 20px;
            border: 1px solid {border_color};
            box-shadow: 0px 4px 18px rgba(0,0,0,0.12);
        }}

        .title-text {{
            font-size: 34px;
            font-weight: 800;
            color: {text_color};
            text-align: center;
            margin-bottom: 5px;
        }}

        .subtitle-text {{
            color: {subtext_color};
            font-size: 15px;
            text-align: center;
            margin-bottom: 25px;
        }}

        label {{
            color: {text_color} !important;
            font-size: 15px !important;
            font-weight: 600 !important;
        }}

        input {{
            border-radius: 12px !important;
            padding: 14px !important;
            font-size: 15px !important;
            width: 100%% !important;
        }}

        .btn-primary {{
            width: 100%%;
            padding: 12px;
            background: #E0B024;
            border-radius: 12px;
            border: none;
            font-size: 17px;
            font-weight: 700;
            cursor: pointer;
        }}

        .btn-secondary {{
            width: 100%%;
            padding: 12px;
            background: #2E7D32;
            color: white;
            border-radius: 12px;
            border: none;
            font-weight: 700;
            cursor: pointer;
            margin-top: 15px;
        }}
    </style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# 6. PAGE HEADER
# ---------------------------------------------------------
st.markdown(f"""
    <h1 class="title-text">🔐 Reset Password</h1>
    <p class="subtitle-text">
        Enter your email and set a new password.
    </p>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# 7. CENTERED FORM CARD
# ---------------------------------------------------------


with st.form("reset_form"):
    st.write("### Email Address")
    email = st.text_input("", placeholder="Enter your email")

    st.write("### New Password")
    new_pass = st.text_input("", type="password", placeholder="Enter new password")

    st.write("### Confirm Password")
    confirm_pass = st.text_input("", type="password", placeholder="Retype new password")

    submit = st.form_submit_button("Reset Password")

    if submit:
        if not email or not new_pass or not confirm_pass:
            st.error("Please fill all fields.")
        elif new_pass != confirm_pass:
            st.error("Passwords do not match.")
        else:
            st.success("Password reset successfully!")

st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------------------------------------
# 8. RETURN BUTTON
# ---------------------------------------------------------
if st.button("Back to Login"):
    switch_page("Login")
