# pages/Reset_Password.py
import streamlit as st
from utils.theme import apply_theme
from utils.language import translate, languages

# -----------------------------
# 1. Init Session States
# -----------------------------
if "theme" not in st.session_state:
    st.session_state.theme = "light"

if "language" not in st.session_state:
    st.session_state.language = "en"

# -----------------------------
# 2. Apply Theme
# -----------------------------
apply_theme(st.session_state.theme)

# -----------------------------
# 3. Language Dropdown
# -----------------------------
st.sidebar.markdown("### 🌐 " + translate("language", st.session_state.language))

selected_lang = st.sidebar.selectbox(
    "",
    list(languages.keys()),
    index=list(languages.keys()).index(st.session_state.language),
)

st.session_state.language = selected_lang

# Theme import (from your utils)
try:
    from utils.theme import get_theme
except:
    def get_theme():
        return st.session_state.get("theme", "light")


st.set_page_config(page_title="CropWise - Reset Password", layout="centered")

# ---------------------------------------------------------
#                    THEME VALUES
# ---------------------------------------------------------
theme = get_theme()
is_dark = theme == "dark"

# ---------------------------------------------------------
#                GLOBAL STYLING
# ---------------------------------------------------------
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;900&display=swap');

    html, body, [class*="css"] {{
        font-family: "Inter", sans-serif;
    }}

    /* Light Theme */
    .light-bg {{ background:#f8fafc; color:#0d141b; }}
    .light-text {{ color:#0d141b; }}
    .light-muted {{ color:#4c739a; }}

    /* Dark Theme */
    .dark-bg {{ background:#0d1115; color:#e6edf3; }}
    .dark-text {{ color:#e6edf3; }}
    .dark-muted {{ color:#8db7e6; }}

    input {{
        border-radius:10px !important;
    }}

    </style>
    """,
    unsafe_allow_html=True,
)

bg_class = "dark-bg" if is_dark else "light-bg"
text_class = "dark-text" if is_dark else "light-text"
muted_class = "dark-muted" if is_dark else "light-muted"

# ---------------------------------------------------------
#                    MAIN BACKGROUND
# ---------------------------------------------------------
st.markdown(
    f"<div class='{bg_class}' style='min-height:100vh; padding-top:30px;'>",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
#                     PAGE TITLE
# ---------------------------------------------------------
st.markdown(
    f"""
    <h1 style="text-align:center; font-size:32px; font-weight:800;" class="{text_class}">
        Reset Password
    </h1>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <p style="text-align:center; font-size:15px; margin-top:-10px;" class="{text_class}">
        Enter your email and new password to reset it.
    </p>
    """,
    unsafe_allow_html=True,
)

st.write("")

# ---------------------------------------------------------
#                     RESET FORM
# ---------------------------------------------------------
with st.form(key="reset_form"):
    email = st.text_input("Email", placeholder="your@email.com")
    new_pass = st.text_input("New Password", type="password", placeholder="Enter new password")
    confirm_pass = st.text_input("Retype New Password", type="password", placeholder="Retype new password")

    submit = st.form_submit_button("Reset Password")

    if submit:
        if email.strip() == "" or new_pass.strip() == "" or confirm_pass.strip() == "":
            st.error("Please fill all fields.")
        elif new_pass != confirm_pass:
            st.error("Passwords do not match.")
        else:
            st.success("Password has been reset successfully!")

# ---------------------------------------------------------
#                   SIGN IN LINK
# ---------------------------------------------------------
st.markdown(
    f"""
    <p style="text-align:center; margin-top:10px;" class="{muted_class}">
        <u>Remember your password? Sign In</u>
    </p>
    """,
    unsafe_allow_html=True,
)

st.markdown("</div>", unsafe_allow_html=True)
