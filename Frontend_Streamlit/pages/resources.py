# pages/Resources.py
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


# Import theme system
try:
    from utils.theme import get_theme
except:
    def get_theme():
        return st.session_state.get("theme", "light")


# ---------------------------------------------------------
#                   PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(page_title="CropWise - Resources", layout="wide")
theme = get_theme()
is_dark = theme == "dark"


# ---------------------------------------------------------
#                   GLOBAL STYLES
# ---------------------------------------------------------
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;700;800&display=swap');

    html, body, [class*="css"] {{
        font-family: "Plus Jakarta Sans", sans-serif !important;
    }}

    /* Light */
    .light-bg {{ background:#fcfaf8; color:#1c140d; }}
    .light-text {{ color:#1c140d; }}
    .light-muted {{ color:#9c7349; }}
    .light-card {{ background:#fcfaf8; border-color:#f4ede7; }}
    .light-icon {{ background:#f4ede7; color:#1c140d; }}

    /* Dark */
    .dark-bg {{ background:#0d1115; color:#e6edf3; }}
    .dark-text {{ color:#e6edf3; }}
    .dark-muted {{ color:#c59f74; }}
    .dark-card {{ background:#111820; border-color:#2a2f36; }}
    .dark-icon {{ background:#2a2f36; color:#e6edf3; }}

    /* Generic styles */
    .resource-box {{
        padding:16px;
        border-radius:12px;
        margin-bottom:10px;
        display:flex;
        gap:15px;
        align-items:center;
    }}

    .resource-icon {{
        width:48px;
        height:48px;
        display:flex;
        align-items:center;
        justify-content:center;
        border-radius:10px;
    }}

    .featured-img {{
        width:70px;
        height:70px;
        border-radius:10px;
        background-size:cover;
        background-position:center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

bg_class = "dark-bg" if is_dark else "light-bg"
text_class = "dark-text" if is_dark else "light-text"
muted_class = "dark-muted" if is_dark else "light-muted"
card_class = "dark-card" if is_dark else "light-card"
icon_class = "dark-icon" if is_dark else "light-icon"


# ---------------------------------------------------------
#                   PAGE BACKGROUND
# ---------------------------------------------------------
st.markdown(f"<div class='{bg_class}' style='min-height:100vh; padding:25px;'>", unsafe_allow_html=True)


# ---------------------------------------------------------
#                   HEADER
# ---------------------------------------------------------
st.markdown(
    f"""
    <h1 class="{text_class}" style="font-size:32px; font-weight:700;">Resources</h1>
    <p class="{muted_class}" style="margin-top:-8px;">
        Explore a variety of educational materials to enhance your cotton farming knowledge and skills.
    </p>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
#                   CATEGORY ITEMS
# ---------------------------------------------------------
def category_item(icon_svg, title, description):
    st.markdown(
        f"""
        <div class="resource-box {card_class}">
            <div class="resource-icon {icon_class}">
                {icon_svg}
            </div>
            <div>
                <p class="{text_class}" style="font-weight:600; margin:0;">{title}</p>
                <p class="{muted_class}" style="margin:0; font-size:14px;">{description}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# SVG icons
book_icon = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor"><path d="M224,48H160a40,40,0,0,0-32,16A40,40,0,0,0,96,48H32A16,16,0,0,0,16,64V192a16,16,0,0,0,16,16H96a24,24,0,0,1,24,24,8,8,0,0,0,16,0,24,24,0,0,1,24-24h64a16,16,0,0,0,16-16V64A16,16,0,0,0,224,48ZM96,192H32V64H96a24,24,0,0,1,24,24V200A39.81,39.81,0,0,0,96,192Zm128,0H160a39.81,39.81,0,0,0-24,8V88a24,24,0,0,1,24-24h64Z"/></svg>"""

bug_icon = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor"><path d="M144,92a12,12,0,1,1,12,12A12,12,0,0,1,144,92ZM100,80a12,12,0,1,0,12,12A12,12,0,0,0,100,80Zm116,64A87.76,87.76,0,0,1,213,167l22.24,9.72A8,8,0,0,1,232,192a7.89,7.89,0,0,1-3.2-.67L207.38,182a88,88,0,0,1-158.76,0L27.2,191.33A7.89,7.89,0,0,1,24,192a8,8,0,0,1-3.2-15.33L43,167A87.76,87.76,0,0,1,40,144v-8H16a8,8,0,0,1,0-16H40v-8a87.76,87.76,0,0,1,3-23L20.8,79.33a8,8,0,1,1,6.4-14.66L48.62,74a88,88,0,0,1,158.76,0l21.42-9.36a8,8,0,0,1,6.4,14.66L213,89.05a87.76,87.76,0,0,1,3,23v8h24a8,8,0,0,1,0,16H216Z"/></svg>"""

water_icon = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor"><path d="M174,47.75a254.19,254.19,0,0,0-41.45-38.3,8,8,0,0,0-9.18,0A254.19,254.19,0,0,0,82,47.75C54.51,79.32,40,112.6,40,144a88,88,0,0,0,176,0C216,112.6,201.49,79.32,174,47.75Z"/></svg>"""

basket_icon = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor"><path d="M136,120v56a8,8,0,0,1-16,0V120a8,8,0,0,1,16,0ZM239.86,98.11,226,202.12A16,16,0,0,1,210.13,216H45.87A16,16,0,0,1,30,202.12l-13.87-104A16,16,0,0,1,32,80H68.37L122,18.73a8,8,0,0,1,12,0L187.63,80H224a16,16,0,0,1,15.85,18.11Z"/></svg>"""

chart_icon = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor"><path d="M232,208a8,8,0,0,1-8,8H32a8,8,0,0,1-8-8V48a8,8,0,0,1,16,0v94.37L90.73,98a8,8,0,0,1,10.07-.38l58.81,44.11L218.73,90a8,8,0,1,1,10.54,12Z"/></svg>"""

plant_icon = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor"><path d="M247.63,39.89a8,8,0,0,0-7.52-7.52c-51.76-3-93.32,12.74-111.18,42.22-11.8,19.49-11.78,43.16-.16,65.74"/></svg>"""

# CATEGORY LIST
category_item(book_icon, "Cotton Farming Basics", "Learn the fundamentals of cotton cultivation.")
category_item(bug_icon, "Pest and Disease Management", "Identify and manage common cotton pests.")
category_item(water_icon, "Irrigation Techniques", "Optimize water use & improve yields.")
category_item(basket_icon, "Harvesting Best Practices", "Maximize quality and efficiency.")
category_item(chart_icon, "Market Trends & Analysis", "Stay informed on cotton industry trends.")
category_item(plant_icon, "Sustainable Farming Methods", "Adopt eco-friendly agricultural practices.")


# ---------------------------------------------------------
#                   FEATURED RESOURCES SECTION
# ---------------------------------------------------------
st.markdown(
    f"""
    <h2 class="{text_class}" style="font-size:22px; margin-top:25px;">Featured Resources</h2>
    """,
    unsafe_allow_html=True,
)


def featured_item(image_url, title, desc, published):
    st.markdown(
        f"""
        <div style="display:flex; gap:15px; padding:12px; margin-bottom:10px;" class="{card_class}">
            <div class="featured-img" style="background-image:url('{image_url}')"></div>

            <div style="flex:1;">
                <p class="{text_class}" style="font-weight:600; margin-bottom:4px;">{title}</p>
                <p class="{muted_class}" style="font-size:14px; margin-top:0;">{desc}</p>
                <p class="{muted_class}" style="font-size:13px; margin-top:4px;">{published}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


featured_item(
    "https://lh3.googleusercontent.com/aida-public/AB6AXuAipAiYqBteAZSCAPnALrz2P9t_yeu93EaPuTEYw_u00i1jaxTTN2xc2IdDXhmJDftzWtcBPhQ-WBs3HmRUknbW8no6DtNoRgZ7aLtuHI28DRwQn6JKJsDrx3Qtv2Bbmsw03GFN7XMO0nHfr_70b16CNhwEG3D9viEie8vNA-MONCtsPyT1PD6tZDFdWaUrW1CgAq4dJYN6J83pf06_hIJ6GxryGOcs686Cs5us4rxxhrewlC6wsYCjHWBEQ6g04eB0_gvD2KrHFOs",
    "Cotton Farming Handbook",
    "A comprehensive guide covering essential aspects of cotton farming—from seeds to soil health.",
    "Published by AgriPredict | 2 weeks ago"
)

featured_item(
    "https://lh3.googleusercontent.com/aida-public/AB6AXuA5WMHb6JHtiRmMYmokDkIEQ134B6T3rB3se4RPtsgJZ_pQYpRvvRjIMm-hjk0LB_eJ9AKea7-YiNr26q3MnR9pcCre0JDjfVqlE2G94XX8uOGFiUdduSSo4tf_aZvc4PpoK8CfxnxNCr8nLBp-RFsRGyPvDvQR4egLiFeAvQVbup5JEywUcFmTcXqsc3yn9n5dKwXA6AenduN_SmHs5cvVnY7DpQDw8hCKd6-OmacsFuSJI-zaMWEPoalzOpuMvTd8LUFAd08gEbI",
    "Pest & Disease Management Guide",
    "Identify and control common pests affecting cotton crops with practical, research-backed methods.",
    "Published by CropCare Solutions | 1 month ago"
)

featured_item(
    "https://lh3.googleusercontent.com/aida-public/AB6AXuA-0YOdg-G8b7znUwR2y94A6Bnx7V5B7lJsxHxnlxxui67uOrdqEdg46UorH7zmOV2_5UyNmIY7yG5N7Kd8uFdcXSjQYPwis5OpBLN37rpxB8yYG-4JTe9V883OCSeWUDuWm60ZfT3ZU8aMDNxa22KeRWzt8oCJ0iUOKczcRsbjnujvj87_WE2EBPFw0_IaJpKbXpJyQM6pkNUYDIk7iTZSo-_XPgq-y1b5T4jArYxOWpwefBGl0_aVfDFRyDEnuR2LGc2ZGCS_Zyg",
    "Irrigation Best Practices for Cotton",
    "Explore water-efficient irrigation techniques to boost crop yield and conserve resources.",
    "Published by WaterWise Irrigation | 2 months ago"
)

# Show button
st.markdown(
    f"""
    <div style="text-align:center; margin-top:20px;">
        <button style="padding:10px 22px; border-radius:25px; background:#f4ede7; color:#1c140d; font-weight:600; border:none;">
            View All Resources
        </button>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)
