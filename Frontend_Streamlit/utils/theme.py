# utils/theme.py
import streamlit as st

# -------------------------
# LIGHT THEME CSS
# -------------------------
light_theme_css = """
<style>

html, body, [data-testid="stAppViewContainer"] {
    background-color: #f8f9fa !important;
    color: #1a1a1a !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #ffffff !important;
    color: #1a1a1a !important;
}

/* Sidebar text */
[data-testid="stSidebar"] * {
    color: #1a1a1a !important;
}

/* Input fields */
input, textarea, .stTextInput input, .stTextArea textarea {
    background-color: #ffffff !important;
    color: #1a1a1a !important;
    border: 1px solid #d9d9d9 !important;
    border-radius: 8px !important;
    padding: 10px !important;
}

/* Selectbox input box */
div[data-baseweb="select"] > div {
    background-color: #ffffff !important;
    color: #1a1a1a !important;
    border: 1px solid #d9d9d9 !important;
}

/* Dropdown Menu */
div[data-baseweb="menu"] {
    background-color: #ffffff !important;
    border: 1px solid #d9d9d9 !important;
    color: #1a1a1a !important;
}

div[data-baseweb="menu"] div[role="option"] {
    background-color: #ffffff !important;
    color: #1a1a1a !important;
}

div[data-baseweb="menu"] div[role="option"]:hover {
    background-color: #f2f2f2 !important;
}

div[data-baseweb="menu"] div[aria-selected="true"] {
    background-color: #e6e6e6 !important;
}

/* Radio Labels */
[data-testid="stRadio"] label {
    color: #1a1a1a !important;
}

/* Buttons */
.stButton > button {
    background-color: #eebd2b !important;
    color: #1a1a1a !important;
    border-radius: 8px !important;
    font-weight: 700 !important;
    border: none !important;
    padding: 10px 16px !important;
}

/* Navbar + Footer */
.navbar, .footer {
    background-color: #ffffff !important;
    color: #1a1a1a !important;
    padding: 16px !important;
    border-bottom: 1px solid #dcdcdc !important;
}

</style>
"""

# -------------------------
# DARK THEME CSS
# -------------------------
dark_theme_css = """
<style>

html, body, [data-testid="stAppViewContainer"] {
    background-color: #0e0e0e !important;
    color: #f5f5f5 !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #1a1a1a !important;
    color: #ffffff !important;
}

/* Sidebar text */
[data-testid="stSidebar"] * {
    color: #ffffff !important;
}

/* Input fields */
input, textarea, .stTextInput input, .stTextArea textarea {
    background-color: #1a1a1a !important;
    color: #ffffff !important;
    border: 1px solid #444444 !important;
    border-radius: 8px !important;
    padding: 10px !important;
}

/* Selectbox input box */
div[data-baseweb="select"] > div {
    background-color: #1a1a1a !important;
    color: #ffffff !important;
    border: 1px solid #444 !important;
}

/* Dropdown Menu */
div[data-baseweb="menu"] {
    background-color: #1a1a1a !important;
    border: 1px solid #444 !important;
    color: #ffffff !important;
}

div[data-baseweb="menu"] div[role="option"] {
    background-color: #1a1a1a !important;
    color: #ffffff !important;
}

div[data-baseweb="menu"] div[role="option"]:hover {
    background-color: #333333 !important;
}

div[data-baseweb="menu"] div[aria-selected="true"] {
    background-color: #333333 !important;
}

/* Radio Labels */
[data-testid="stRadio"] label {
    color: #ffffff !important;
}

/* Buttons */
.stButton > button {
    background-color: #32693d !important;
    color: #ffffff !important;
    border-radius: 8px !important;
    font-weight: 700 !important;
    border: none !important;
    padding: 10px 16px !important;
}

/* Navbar + Footer */
.navbar, .footer {
    background-color: #111 !important;
    color: #f5f5f5 !important;
    padding: 16px !important;
    border-bottom: 1px solid #333 !important;
}

</style>
"""

# -------------------------
# APPLY THEME FUNCTION
# -------------------------
def apply_theme(theme_choice: str):
    """Injects Light or Dark CSS into Streamlit."""
    if theme_choice == "light":
        st.markdown(light_theme_css, unsafe_allow_html=True)
    else:
        st.markdown(dark_theme_css, unsafe_allow_html=True)
