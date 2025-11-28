# pages/Settings.py
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# If you have utils functions, import them:
try:
    from utils.theme import get_theme, set_theme
except:
    # fallback if utils not implemented
    def get_theme():
        return st.session_state.get("theme", "light")

    def set_theme(x):
        st.session_state["theme"] = x

st.set_page_config(page_title="CropWise - Theme Settings", layout="wide")

# ------------------------------------------
#             CURRENT THEME
# ------------------------------------------
theme = get_theme()
is_dark = theme == "dark"

# ------------------------------------------
#         GLOBAL FONTS & STYLES
# ------------------------------------------
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Work+Sans:wght@400;500;700&display=swap');

    html, body, [class*="css"] {{
        font-family: "Work Sans", sans-serif;
    }}

    /* Light Styles */
    .light-bg {{ background:#ffffff; color:#181611; }}
    .light-border {{ border-color:#e6e3db; }}
    .light-muted {{ color:#897f61; }}

    /* Dark Styles */
    .dark-bg {{ background:#0d1410; color:#f3f7f0; }}
    .dark-border {{ border-color:#2e3a2e; }}
    .dark-muted {{ color:#d4d8cc; }}

    .theme-option {{
        padding: 10px 20px;
        border-radius: 10px;
        border-width:2px;
        cursor:pointer;
        font-weight:600;
        display:inline-block;
        margin-right:10px;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

theme_container = "dark-bg" if is_dark else "light-bg"
border_class = "dark-border" if is_dark else "light-border"
muted = "dark-muted" if is_dark else "light-muted"

st.markdown(f"<div class='{theme_container}' style='min-height:100vh; padding:20px 40px;'>", unsafe_allow_html=True)

# ----------------------------------------------------
#                    NAVBAR
# ----------------------------------------------------
nav_left, nav_right = st.columns([1, 4])

with nav_left:
    st.markdown(
        f"<h2 style='margin:0; font-weight:800;'>CropWise</h2>",
        unsafe_allow_html=True,
    )

with nav_right:
    st.markdown(
        f"""
        <div style='display:flex; justify-content:flex-end; gap:20px; align-items:center;'>
            <a href="#" style="color:inherit; text-decoration:none;">Dashboard</a>
            <a href="#" style="color:inherit; text-decoration:none;">Prediction</a>
            <a href="#" style="color:inherit; text-decoration:none;">History</a>
            <a href="#" style="color:inherit; text-decoration:none;">Settings</a>
            <div style="
                width:40px; height:40px; border-radius:50%; background-size:cover;
                background-image:url('https://lh3.googleusercontent.com/aida-public/AB6AXuAUqwmeBiTs6Ajax507jImPOTDDPGFm1xvsjszpmUiIaGloDyZGobiuwBVVYuQQO5oKt0h3LfQVYc6W7BvZJ01eDsDuioCMSNbsPy86ayoqcqVhsE-807Qt1cA08ahVQT7NLvqOikAVlVzYpQ1QIj0g0djDspgyZXnhmS_r4D6yDoCUGu605C43E1bRyEe_n1970Mf-xeHHZ-xtVT7cZW9WzjVpXEJ7L8Q6u975ml-O_NbxWfy05PvXoqDWujBtugICOQ7veol7gck');
            "></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("")

# ----------------------------------------------------
#                  PAGE TITLE
# ----------------------------------------------------
st.markdown(
    "<h1 style='font-weight:800; font-size:32px;'>Theme Settings</h1>",
    unsafe_allow_html=True,
)

# ----------------------------------------------------
#               THEME SELECTION UI
# ----------------------------------------------------
st.markdown("<h3>Select Theme</h3>", unsafe_allow_html=True)

col_light, col_dark = st.columns(2)

# Light Theme Button
with col_light:
    if st.button("☀️ Light Theme", use_container_width=True):
        set_theme("light")
        st.rerun()

# Dark Theme Button
with col_dark:
    if st.button("🌙 Dark Theme", use_container_width=True):
        set_theme("dark")
        st.rerun()

st.write("---")

# ----------------------------------------------------
#                  PREVIEW SECTION
# ----------------------------------------------------
st.markdown("<h3>Preview</h3>", unsafe_allow_html=True)

preview_box = "dark-bg" if is_dark else "light-bg"
preview_border = "dark-border" if is_dark else "light-border"
preview_text = "white" if is_dark else "#181611"
preview_sub = "#cbd5c0" if is_dark else "#897f61"

preview_image = (
    "https://lh3.googleusercontent.com/aida-public/AB6AXuAyGBrWbAFyhorR_-QhQU8EANznBfwKkEnpt_F0HjkYeZy1ConUzbSDlwQS47pdQUSLQEQqklDR7TgSEizEJa41AQONLXkwXtaCj00oFFNKGpFt3VI9BgE0_AD6mAppngVbPuFhvdUyvIPZvfZ_TDcy0125JkQC8Ef8zwi0JJfRGupe_nc5D2uIiKVcag_vktwWAfMQYFVzKUVZrR-g-EAY3r-HClczgxNmbcxBAIHIWttkpe-RKaQPmq2wbZx5oq6uOQZjfTSAXZY"
)

st.markdown(
    f"""
    <div style="
        border:2px solid; 
        border-radius:12px;
        padding:20px;
        {('background:#0d1410;' if is_dark else 'background:white;')}
        border-color:{('#2e3a2e' if is_dark else '#e6e3db')}
    ">
        <div style="display:flex; gap:20px; align-items:center;">
            <div style="
                width:100%; 
                max-width:500px;
                height:220px;
                border-radius:10px;
                background-size:cover;
                background-position:center;
                background-image:url('{preview_image}');
            "></div>

            <div style="flex:1;">
                <p style="font-size:20px; font-weight:700; color:{preview_text}; margin-bottom:8px;">
                    Dashboard Preview
                </p>
                <p style="font-size:15px; color:{preview_sub};">
                    This is a preview of the dashboard with the selected theme.
                </p>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")
st.markdown("<small style='opacity:0.7;'>Changes apply instantly across all pages.</small>", unsafe_allow_html=True)

# Close wrapper
st.markdown("</div>", unsafe_allow_html=True)
