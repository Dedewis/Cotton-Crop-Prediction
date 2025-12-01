# utils/ui.py
import streamlit as st
from utils.language import translate, languages
from utils.theme import apply_theme

def page_start(title_key):
    st.set_page_config(page_title="CropWise", layout="wide")

    if "theme" not in st.session_state:
        st.session_state.theme = "light"

    if "language" not in st.session_state:
        st.session_state.language = "en"

    apply_theme()

    # Navbar
    st.markdown(f"""
    <div class="navbar" style="padding:16px 20px; display:flex; justify-content:space-between; align-items:center;">
        <h2 style="margin:0; font-weight:800;">CropWise</h2>

        <div style="display:flex; gap:24px; font-size:15px; align-items:center;">
            <a href="/Home" style="text-decoration:none;">{translate('home', st.session_state.language)}</a>
            <a href="/Prediction" style="text-decoration:none;">{translate('prediction', st.session_state.language)}</a>
            <a href="/Resources" style="text-decoration:none;">{translate('resources', st.session_state.language)}</a>
            <a href="/Profile" style="text-decoration:none;">{translate('profile', st.session_state.language)}</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Sidebar controls
    st.sidebar.title("⚙ Settings")

    # Theme toggle
    theme_choice = st.sidebar.radio(
        translate("theme", st.session_state.language),
        ["light", "dark"],
        index=0 if st.session_state.theme == "light" else 1
    )
    st.session_state.theme = theme_choice

    # Language dropdown
    st.sidebar.selectbox(
        translate("language", st.session_state.language),
        languages.keys(),
        key="language"
    )

    st.markdown(f"<h1 style='margin-top:30px;'>{translate(title_key, st.session_state.language)}</h1>", unsafe_allow_html=True)


def page_end():
    st.markdown("""
    <br><br>
    <div class="footer" style="padding:16px; text-align:center;">
        © 2025 CropWise · Empowering Smart Agriculture 🌱
    </div>
    """, unsafe_allow_html=True)
