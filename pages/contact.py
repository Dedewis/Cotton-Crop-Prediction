# pages/Contact_Us.py
import streamlit as st

# Theme import
try:
    from utils.theme import get_theme
except:
    def get_theme():
        return st.session_state.get("theme", "light")

st.set_page_config(page_title="CropWise - Contact Us", layout="centered")

# ---------------------------------------------------------
#                    THEME VALUES
# ---------------------------------------------------------
theme = get_theme()
is_dark = theme == "dark"

# ---------------------------------------------------------
#                GLOBAL STYLES
# ---------------------------------------------------------
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;700;800&display=swap');

    html, body, [class*="css"] {{
        font-family: "Manrope", sans-serif;
    }}

    /* Light Theme */
    .light-bg {{ background:#fcfaf8; color:#1c140d; }}
    .light-text {{ color:#1c140d; }}
    .light-muted {{ color:#9c7349; }}
    .light-input-bg {{ background:#fcfaf8; border-color:#e8dbce; color:#1c140d; }}
    .light-section-border {{ border-color:#e8dbce; }}

    /* Dark Theme */
    .dark-bg {{ background:#0d1115; color:#e6edf3; }}
    .dark-text {{ color:#e6edf3; }}
    .dark-muted {{ color:#c59f74; }}
    .dark-input-bg {{ background:#111820; border-color:#2a2f36; color:#e6edf3; }}
    .dark-section-border {{ border-color:#2a2f36; }}

    textarea, input {{
        border-radius:12px !important;
        padding:14px !important;
        font-size:15px !important;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

bg_class = "dark-bg" if is_dark else "light-bg"
text_class = "dark-text" if is_dark else "light-text"
muted_class = "dark-muted" if is_dark else "light-muted"
input_class = "dark-input-bg" if is_dark else "light-input-bg"
border_class = "dark-section-border" if is_dark else "light-section-border"


# ---------------------------------------------------------
#                    PAGE BACKGROUND
# ---------------------------------------------------------
st.markdown(
    f"<div class='{bg_class}' style='min-height:100vh; padding-top:30px;'>",
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
#                    PAGE HEADER
# ---------------------------------------------------------
st.markdown(
    f"""
    <h1 class="{text_class}" style="font-size:32px; text-align:left; padding-left:15px;">
        Contact Us
    </h1>
    <p class="{muted_class}" style="margin-top:-10px; padding-left:15px;">
        We're here to help! Reach out to us with any questions or feedback.
    </p>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
#                CONTACT FORM
# ---------------------------------------------------------
with st.form("contact_form"):
    st.markdown(f"<p class='{text_class}'><b>Your Name</b></p>", unsafe_allow_html=True)
    name = st.text_input("", placeholder="Enter your name", key="name")

    st.markdown(f"<p class='{text_class}'><b>Your Email</b></p>", unsafe_allow_html=True)
    email = st.text_input("", placeholder="Enter your email", key="email")

    st.markdown(f"<p class='{text_class}'><b>Subject</b></p>", unsafe_allow_html=True)
    subject = st.text_input("", placeholder="Enter the subject", key="subject")

    st.markdown(f"<p class='{text_class}'><b>Message</b></p>", unsafe_allow_html=True)
    message = st.text_area("", placeholder="Enter your message", key="message")

    send = st.form_submit_button("📨 Send Message")

    if send:
        if not name or not email or not subject or not message:
            st.error("Please fill out all fields.")
        else:
            st.success("Your message has been sent successfully!")


# ---------------------------------------------------------
#               ADDITIONAL CONTACT INFO
# ---------------------------------------------------------
st.markdown(
    f"""
    <h2 class="{text_class}" style="font-size:22px; margin-top:35px; padding-left:15px;">
        Additional Contact Information
    </h2>
    """,
    unsafe_allow_html=True,
)

# CONTACT SECTION GRID
st.markdown(
    f"""
    <div style="padding: 15px;">
        <div style="border-top:1px solid; padding:12px 0;" class="{border_class}">
            <p class="{muted_class}" style="margin:0;">Email</p>
            <p class="{text_class}" style="margin:0;">support@cropwise.com</p>
        </div>

        <div style="border-top:1px solid; padding:12px 0;" class="{border_class}">
            <p class="{muted_class}" style="margin:0;">Phone</p>
            <p class="{text_class}" style="margin:0;">+1 (555) 123-4567</p>
        </div>

        <div style="border-top:1px solid; padding:12px 0;" class="{border_class}">
            <p class="{muted_class}" style="margin:0;">Address</p>
            <p class="{text_class}" style="margin:0;">123 AgriTech Lane, Farmville, USA</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("</div>", unsafe_allow_html=True)
