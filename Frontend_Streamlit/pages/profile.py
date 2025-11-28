# pages/Profile.py
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
# adapt these imports to your project utilities if different
from utils.language import get_language, t
from utils.theme import get_theme

st.set_page_config(page_title="CropWise - Profile", layout="wide")

# ------------------- THEME / LANG -------------------
theme = get_theme()  # should return "light" or "dark"
lang = get_language()  # not used directly but might be needed by your t()

# ------------------- STYLES --------------------------
# Light + Dark styling, ensures good contrast in dark mode
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Work+Sans:wght@400;600;700&display=swap');
    html, body, [class*="css"] {{ font-family: 'Work Sans', sans-serif; }}

    /* wrapper */
    .page-wrap {{ min-height:100vh; padding: 18px 40px; }}

    /* light */
    .light-bg {{ background: #fcfbf8; color: #1b180d; }}
    .light-card {{ background: #fff; border: 1px solid #e7e1cf; }}
    .light-input {{ background:#fcfbf8; color:#1b180d; }}

    /* dark */
    .dark-bg {{ background: #07140a; color: #e6f7e9; }}
    .dark-card {{ background:#0f1f12; border: 1px solid #27482e; }}
    .dark-input {{ background:#102016; color:#e6f7e9; }}

    /* generic controls */
    .section-title {{ font-size:18px; font-weight:700; margin-top:18px; margin-bottom:6px; }}
    .small-muted {{ color: #9a864c; font-size:13px; margin-bottom:12px; }}

    /* buttons */
    .btn-cancel {{ background:#f3f0e7; color:#1b180d; padding:8px 14px; border-radius:8px; }}
    .btn-save {{ background:#eebd2b; color:#1b180d; padding:8px 14px; border-radius:8px; font-weight:700; }}

    /* inputs styling via streamlit selectors */
    .stTextInput>div>div>input, .stSelectbox>div>div>select, .stNumberInput>div>input {{
        padding: 12px;
        border-radius: 10px;
    }}

    /* ensure readable placeholder color in dark mode */
    .dark-bg ::placeholder {{ color: #9aa98b !important; }}

    </style>
    """,
    unsafe_allow_html=True,
)

# outer wrapper with chosen theme class
theme_class = "dark-bg" if theme == "dark" else "light-bg"
card_class = "dark-card" if theme == "dark" else "light-card"
input_class = "dark-input" if theme == "dark" else "light-input"

st.markdown(f"<div class='page-wrap {theme_class}'>", unsafe_allow_html=True)

# ------------------- NAVBAR ---------------------------
col1, col2 = st.columns([1, 4])
with col1:
    st.markdown(
        f"<h2 style='margin:0; color:inherit; font-weight:800;'>CropWise</h2>",
        unsafe_allow_html=True,
    )
with col2:
    # lightweight nav links (non-functional anchors)
    st.markdown(
        f"""
        <div style='display:flex; justify-content:flex-end; gap:18px; align-items:center; margin-top:6px;'>
            <a style='color:inherit; text-decoration:none;' href='#'>Dashboard</a>
            <a style='color:inherit; text-decoration:none;' href='#'>Predictions</a>
            <a style='color:inherit; text-decoration:none;' href='#'>Resources</a>
            <a style='color:inherit; text-decoration:none;' href='#'>Support</a>
            <div style='width:36px; height:36px; border-radius:50%; background-image:url("https://lh3.googleusercontent.com/aida-public/AB6AXuDHAt2cwvQ1_p8vd2Z2iJEHcFRrol6RaVotB2SH2TiNB5XCmiUXmTefR5Jf8vAeBVLs8hTJX8OkTG0RurfgUn8k35OKKQzUCt7ogKyvbwtOqd76tuEW3XNZTMfFndIjt0OZ9Ydi_RePZbWY9D2vu8M7XtM0ZosOIRfKSCHlpu6KljhVt9Oq6UDKduQcKJNCyIWtNg2A2HoysD92pCXPLvKDQkpJMOyVRyS6wpuI6dD-tVV0KBNHtc-_9eyW7QT_GAHfDQtNHp5b4AY"); background-size:cover;'></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("")  # spacer

# ------------------- PAGE HEADER -----------------------
st.markdown(
    f"<div class='{card_class}' style='padding:18px; border-radius:12px; max-width:980px;'>"
    f"<div style='display:flex; gap:12px; align-items:center;'>"
    f"<div style='flex:1;'>"
    f"<p class='section-title' style='margin:0;'>Your Profile</p>"
    f"<p class='small-muted'>Manage your account settings and preferences.</p>"
    f"</div></div></div>",
    unsafe_allow_html=True,
)

st.write("")

# ------------------- FORM FIELDS -----------------------
col_a, col_b = st.columns([1, 1], gap="large")

with col_a:
    name = st.text_input(
        label=t("name") if callable(t) else "Name",
        value=st.session_state.get("profile_name", ""),
        key="profile_name",
        help="Full name",
    )

    email = st.text_input(
        label=t("email") if callable(t) else "Email",
        value=st.session_state.get("profile_email", ""),
        key="profile_email",
        help="Email address",
    )

    location = st.text_input(
        label=t("location") if callable(t) else "Location",
        value=st.session_state.get("profile_location", ""),
        key="profile_location",
        help="Town / State",
    )

with col_b:
    units = st.selectbox(
        label=t("preferredUnits") if callable(t) else "Preferred Units",
        options=["hectares", "acres"],
        index=0,
        key="profile_units",
    )

    notifications = st.checkbox(
        label=t("emailNotifications") if callable(t) else "Email Notifications",
        value=st.session_state.get("profile_notifications", True),
        key="profile_notifications",
    )

    # Security fields
    st.markdown("<div style='margin-top:12px; font-weight:700;'>Security</div>", unsafe_allow_html=True)
    current_pw = st.text_input("Current Password", type="password", key="profile_current_pw")
    new_pw = st.text_input("New Password", type="password", key="profile_new_pw")
    confirm_pw = st.text_input("Confirm New Password", type="password", key="profile_confirm_pw")

# ------------------- ACTIONS ---------------------------
col_cancel, col_save = st.columns([1, 1])
with col_cancel:
    if st.button("Cancel", key="profile_cancel"):
        # revert inputs (simple reset)
        for k in ["profile_name", "profile_email", "profile_location", "profile_units", "profile_notifications"]:
            if k in st.session_state:
                st.session_state[k] = ""
        st.success("Changes discarded.")
with col_save:
    if st.button("Save Changes", key="profile_save"):
        # simple validation
        if new_pw or confirm_pw:
            if new_pw != confirm_pw:
                st.error("New passwords do not match.")
            else:
                # Here you would call backend update logic
                st.success("Profile & password updated successfully.")
        else:
            # update profile only
            st.success("Profile updated successfully.")

# ------------------- FOOTER ------------------------------
st.markdown("<br/>", unsafe_allow_html=True)
st.markdown(
    f"<div style='max-width:980px; padding:10px 0 40px 0;'>"
    f"<small style='color: #9a864c;'>Tip: Use 'Preferred Units' to switch between hectares and acres for area inputs across the application.</small>"
    f"</div>",
    unsafe_allow_html=True,
)

st.markdown("</div>", unsafe_allow_html=True)
