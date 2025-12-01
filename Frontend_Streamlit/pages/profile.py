# pages/Profile.py

import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from utils.theme import apply_theme
from utils.language import translate, languages

# ---------------------------------------------------------
# 1. Session State Init
# ---------------------------------------------------------
if "theme" not in st.session_state:
    st.session_state.theme = "light"

if "language" not in st.session_state:
    st.session_state.language = "en"

# ---------------------------------------------------------
# 2. Apply Theme
# ---------------------------------------------------------
apply_theme(st.session_state.theme)
theme = st.session_state.theme  # <-- IMPORTANT

# ---------------------------------------------------------
# 3. Sidebar Language Dropdown
# ---------------------------------------------------------
st.sidebar.markdown("### 🌐 " + translate("language", st.session_state.language))

selected_lang = st.sidebar.selectbox(
    "",
    list(languages.keys()),
    index=list(languages.keys()).index(st.session_state.language),
)

st.session_state.language = selected_lang

# ---------------------------------------------------------
# Page Config
# ---------------------------------------------------------
st.set_page_config(page_title="CropWise - Profile", layout="wide")

# ---------------------------------------------------------
# STYLES
# ---------------------------------------------------------
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Work+Sans:wght@400;600;700&display=swap');
    html, body, [class*="css"] {{ font-family: 'Work Sans', sans-serif; }}

    .page-wrap {{ min-height:100vh; padding: 18px 40px; }}

    /* light */
    .light-bg {{ background: #fcfbf8; color: #1b180d; }}
    .light-card {{ background: #fff; border: 1px solid #e7e1cf; }}

    /* dark */
    .dark-bg {{ background: #07140a; color: #e6f7e9; }}
    .dark-card {{ background:#0f1f12; border: 1px solid #27482e; }}

    .section-title {{ font-size:20px; font-weight:700; }}
    .small-muted {{ color:#9a864c; font-size:13px; }}

    .btn-cancel {{ background:#f3f0e7; color:#1b180d; padding:8px 14px; border-radius:8px; }}
    .btn-save {{ background:#eebd2b; color:#1b180d; padding:8px 14px; border-radius:8px; font-weight:700; }}

    .stTextInput>div>div>input {{
        padding: 12px;
        border-radius: 10px;
    }}

    .dark-bg ::placeholder {{ color:#9aa98b !important; }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Theme classes
theme_class = "dark-bg" if theme == "dark" else "light-bg"
card_class = "dark-card" if theme == "dark" else "light-card"

# Start Wrapper
st.markdown(f"<div class='page-wrap {theme_class}'>", unsafe_allow_html=True)

# ---------------------------------------------------------
# NAVBAR
# ---------------------------------------------------------
col1, col2 = st.columns([1, 4])
with col1:
    st.markdown("<h2 style='margin:0;'>CropWise</h2>", unsafe_allow_html=True)

with col2:
    st.markdown(
        """
        <div style='display:flex; justify-content:flex-end; gap:18px; align-items:center;'>
            <a style='color:inherit; text-decoration:none;'>Dashboard</a>
            <a style='color:inherit; text-decoration:none;'>Predictions</a>
            <a style='color:inherit; text-decoration:none;'>Resources</a>
            <a style='color:inherit; text-decoration:none;'>Support</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("")

# ---------------------------------------------------------
# PAGE HEADER
# ---------------------------------------------------------
st.markdown(
    f"""
    <div class='{card_class}' style='padding:18px; border-radius:12px; max-width:980px;'>
        <p class='section-title'>Your Profile</p>
        <p class='small-muted'>Manage your account settings and preferences.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

# ---------------------------------------------------------
# FORM
# ---------------------------------------------------------
col_a, col_b = st.columns([1, 1])

with col_a:
    name = st.text_input(
        translate("name", st.session_state.language),
        value=st.session_state.get("profile_name", ""),
        key="profile_name",
    )

    email = st.text_input(
        translate("email", st.session_state.language),
        value=st.session_state.get("profile_email", ""),
        key="profile_email",
    )

    location = st.text_input(
        translate("location", st.session_state.language),
        value=st.session_state.get("profile_location", ""),
        key="profile_location",
    )

with col_b:
    units = st.selectbox(
        translate("preferredUnits", st.session_state.language),
        ["hectares", "acres"],
        key="profile_units",
    )

    notifications = st.checkbox(
        translate("emailNotifications", st.session_state.language),
        value=st.session_state.get("profile_notifications", True),
        key="profile_notifications",
    )

    st.markdown("### Security")

    current_pw = st.text_input("Current Password", type="password")
    new_pw = st.text_input("New Password", type="password")
    confirm_pw = st.text_input("Confirm New Password", type="password")

# ---------------------------------------------------------
# ACTIONS
# ---------------------------------------------------------
col_cancel, col_save = st.columns(2)

with col_cancel:
    if st.button("Cancel"):
        st.success("Changes discarded.")

with col_save:
    if st.button("Save Changes"):
        if new_pw and new_pw != confirm_pw:
            st.error("Passwords do not match.")
        else:
            st.success("Profile updated successfully.")

# END
st.markdown("</div>", unsafe_allow_html=True)
