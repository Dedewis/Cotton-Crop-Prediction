import streamlit as st

def apply_theme():
    theme = st.get_option("theme.base")
    is_dark = theme == "dark"

    colors = {
        "primary": "#FFFFFF" if is_dark else "#1c140d",
        "secondary": "#c9b18f" if is_dark else "#9c7349",
        "background": "#111111" if is_dark else "#fcfaf8",
        "card": "#1b1b1b" if is_dark else "#fcfaf8",
        "border": "#3a3a3a" if is_dark else "#f4ede7",
    }

    return colors
