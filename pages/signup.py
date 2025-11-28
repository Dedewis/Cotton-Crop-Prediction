import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from utils.language import t, set_language, get_language
from utils.theme import get_theme


# ---------------------- PAGE CONFIG -----------------------
st.set_page_config(page_title="CropWise - Signup", layout="wide")


# ---------------------- THEME & LANGUAGE -------------------
theme = get_theme()
lang = get_language()

# Apply custom fonts + page styles
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Work+Sans:wght@400;500;700;900&family=Noto+Sans:wght@400;500;700;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Work Sans', 'Noto Sans', sans-serif;
}

/* Light Theme */
.light-bg {
    background-color: #fcfbf8;
}
.light-text { color: #1b180d !important; }
.light-input {
    background-color: #f3f0e7 !important;
    color: #1b180d !important;
    border: none !important;
}

/* Dark Theme */
.dark-bg {
    background-color: #111 !important;
}
.dark-text { color: #f5f5f5 !important; }
.dark-input {
    background-color: #333 !important;
    color: #f5f5f5 !important;
    border: none !important;
}

/* Buttons */
.signup-btn {
    background-color: #eebd2b;
    color: #1b180d;
    padding: 10px 16px;
    border-radius: 10px;
    font-weight: 700;
    width: 100%;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)


# ---------------------- PAGE WRAPPER -----------------------
st.markdown(
    f"<div class='{theme}-bg' style='min-height:100vh; padding-bottom:20px;'>",
    unsafe_allow_html=True
)


# ----------------------- NAVBAR ----------------------------
col1, col2 = st.columns([1, 5])

with col1:
    st.markdown(
        f"""
        <h2 class="{theme}-text" style="font-size:22px; font-weight:800; margin-top:20px;">
            CropWise
        </h2>
        """, unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div style="display:flex; gap:30px; justify-content:flex-end; margin-top:20px;">
            <a href="/Home" class="{theme}-text" style="text-decoration:none; font-size:14px;">{t("home")}</a>
            <a href="/About" class="{theme}-text" style="text-decoration:none; font-size:14px;">{t("about")}</a>
            <a href="/Services" class="{theme}-text" style="text-decoration:none; font-size:14px;">{t("services")}</a>
            <a href="/Contact" class="{theme}-text" style="text-decoration:none; font-size:14px;">{t("contact")}</a>
            
            <button onclick="window.location.href='/Login'" 
                class="{theme}-text" 
                style="background:#f3f0e7; padding:6px 16px; border-radius:8px; font-weight:700;">
                {t("login")}
            </button>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")


# ---------------------- SIGNUP CONTENT ----------------------
st.markdown(
    f"<h2 class='{theme}-text' style='text-align:center; font-size:28px; font-weight:800; margin-top:20px;'>"
    f"{t('createAccount')}"
    "</h2>",
    unsafe_allow_html=True
)

# INPUT FIELDS
inputs = [
    ("fullName", t("fullName")),
    ("email", t("email")),
    ("password", t("password")),
    ("confirmPassword", t("confirmPassword")),
]

user_data = {}

for key, label in inputs:
    user_data[key] = st.text_input(
        label,
        type="password" if "password" in key.lower() else "default",
        placeholder=label,
        key=key,
    )

# SIGN UP BUTTON
if st.button(t("signup"), use_container_width=True):
    if not all(user_data.values()):
        st.error(t("fillAll"))
    elif user_data["password"] != user_data["confirmPassword"]:
        st.error(t("passwordMismatch"))
    else:
        st.success(t("signupSuccess"))
        switch_page("Login")


# ---------------------- FOOTER TEXT -------------------------
st.markdown(
    f"""
    <p class='{theme}-text' style="text-align:center; margin-top:20px; font-size:14px;">
        {t("alreadyAccount")} 
        <a href="/Login" style="color:#5DAF4D; font-weight:700;">{t("login")}</a>
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)
