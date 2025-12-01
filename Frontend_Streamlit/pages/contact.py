# pages/Contact_Us.py
import streamlit as st
from utils.theme import apply_theme
from utils.language import translate, languages

# -----------------------------
# Init Session State
# -----------------------------
if "theme" not in st.session_state:
    st.session_state.theme = "light"

if "language" not in st.session_state:
    st.session_state.language = "en"

apply_theme(st.session_state.theme)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.title("🌾 CropWise")

    st.subheader(translate("language", st.session_state.language))
    st.session_state.language = st.selectbox(
        "",
        list(languages.keys()),
        index=list(languages.keys()).index(st.session_state.language),
        format_func=lambda x: languages[x]
    )

    st.subheader(translate("theme", st.session_state.language))
    selected_theme = st.radio(
        "",
        ["light", "dark"],
        index=0 if st.session_state.theme == "light" else 1
    )
    st.session_state.theme = selected_theme


# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="CropWise - Contact Us", layout="wide")

theme = st.session_state.theme
is_dark = theme == "dark"

# -----------------------------
# Global Styles
# -----------------------------
st.markdown(
    f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;700;800&display=swap');

        html, body, [class*="css"] {{
            font-family: 'Manrope', sans-serif;
        }}

        .page-wrap {{
            max-width: 850px;
            margin: auto;
            padding: 30px 20px;
        }}

        .section-card {{
            background: {"#0f1115" if is_dark else "#ffffff"};
            padding: 25px;
            border-radius: 14px;
            border: 1px solid {"#2a2f36" if is_dark else "#e8e2d9"};
            margin-bottom: 25px;
        }}

        .form-label {{
            font-weight: 600;
            margin-bottom: -8px;
            color: {"#e6edf3" if is_dark else "#1c140d"};
        }}

        textarea, input {{
            border-radius: 10px !important;
            padding: 12px !important;
        }}

        .header-title {{
            font-size: 32px;
            font-weight: 800;
            color: {"#e6edf3" if is_dark else "#1c140d"};
        }}

        .header-sub {{
            margin-top: -10px;
            font-size: 15px;
            color: {"#c8b28e" if is_dark else "#9b7b52"};
        }}

        .info-title {{
            font-size: 20px;
            font-weight: 700;
            margin-bottom: 10px;
            color: {"#e6edf3" if is_dark else "#1c140d"};
        }}

        .info-label {{
            color: {"#c8b28e" if is_dark else "#9b7b52"};
            font-size: 14px;
        }}

        .info-value {{
            color: {"#e6edf3" if is_dark else "#1c140d"};
            font-size: 16px;
            font-weight: 500;
        }}
    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# PAGE CONTENT
# -----------------------------
st.markdown("<div class='page-wrap'>", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown(
    f"""
    <h1 class="header-title">📬 Contact Us</h1>
    <p class="header-sub">We’re here to help! Reach out for support, questions, or feedback.</p>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Contact Form Card
# -----------------------------
st.markdown("<div class='section-card'>", unsafe_allow_html=True)

with st.form("contact_form"):
    st.markdown("<p class='form-label'>Your Name</p>", unsafe_allow_html=True)
    name = st.text_input("", placeholder="Enter your name")

    st.markdown("<p class='form-label'>Your Email</p>", unsafe_allow_html=True)
    email = st.text_input("", placeholder="Enter your email")

    st.markdown("<p class='form-label'>Subject</p>", unsafe_allow_html=True)
    subject = st.text_input("", placeholder="Enter the subject")

    st.markdown("<p class='form-label'>Message</p>", unsafe_allow_html=True)
    message = st.text_area("", placeholder="Enter your message", height=150)

    submitted = st.form_submit_button("📨 Send Message")

    if submitted:
        if not name or not email or not subject or not message:
            st.error("⚠ Please fill all fields before sending.")
        else:
            st.success("✅ Your message has been sent successfully!")

st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------
# Additional Information Card
# -----------------------------
st.markdown("<div class='section-card'>", unsafe_allow_html=True)

st.markdown("<div class='info-title'>📎 Additional Contact Information</div>", unsafe_allow_html=True)

st.markdown(
    f"""
    <p class="info-label">Email</p>
    <p class="info-value">support@cropwise.com</p>

    <p class="info-label" style="margin-top:15px;">Phone</p>
    <p class="info-value">+1 (555) 123-4567</p>

    <p class="info-label" style="margin-top:15px;">Address</p>
    <p class="info-value">123 AgriTech Lane, Farmville, USA</p>
    """,
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)

# END WRAPPER
st.markdown("</div>", unsafe_allow_html=True)
