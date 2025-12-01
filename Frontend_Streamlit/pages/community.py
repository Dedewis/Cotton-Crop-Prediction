import streamlit as st
from utils.theme import apply_theme
from utils.language import translate, languages

# =========================================================
# 1. PAGE CONFIG  (MUST BE FIRST!!)
# =========================================================
st.set_page_config(
    page_title="CropWise - Community Forum",
    page_icon="🌾",
    layout="wide"
)

# =========================================================
# 2. SESSION STATE
# =========================================================
if "theme" not in st.session_state:
    st.session_state.theme = "light"

if "language" not in st.session_state:
    st.session_state.language = "en"

# Theme Apply
apply_theme(st.session_state.theme)

# =========================================================
# 3. SIDEBAR (Language & Theme Switch)
# =========================================================
with st.sidebar:
    st.title("🌾 CropWise")

    st.subheader(translate("language", st.session_state.language))
    st.session_state.language = st.selectbox(
        "",
        list(languages.keys()),
        index=list(languages.keys()).index(st.session_state.language),
        format_func=lambda x: languages[x]
    )

    st.subheader("theme")
    theme_option = st.radio(
        "",
        ["light", "dark"],
        index=0 if st.session_state.theme == "light" else 1
    )
    st.session_state.theme = theme_option


# =========================================================
# 4. THEME COLORS
# =========================================================
is_dark = st.session_state.theme == "dark"

TEXT_PRIMARY = "#ffffff" if is_dark else "#1b1b1b"
TEXT_SECONDARY = "#d3c7b6" if is_dark else "#7a5a3a"
BG_CARD = "#1c1c1c" if is_dark else "#ffffff"
BORDER_COLOR = "#333" if is_dark else "#e8e3db"


# =========================================================
# 5. PAGE TITLE
# =========================================================
st.markdown(
    f"""
    <h1 style="color:{TEXT_PRIMARY}; font-size:32px; font-weight:800;">
        💬 Community Forum
    </h1>
    <p style="color:{TEXT_SECONDARY}; font-size:14px; margin-top:-5px;">
        Connect with cotton farmers, share experiences, and discuss crop challenges.
    </p>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 6. FEATURED DISCUSSIONS
# =========================================================
st.markdown(
    f"<h2 style='color:{TEXT_PRIMARY}; font-size:22px;'>⭐ Featured Discussions</h2>",
    unsafe_allow_html=True,
)

featured_items = [
    {
        "img": "https://images.unsplash.com/photo-1438109491414-7198515b166b?w=800",
        "title": "Optimizing Irrigation for Higher Yields",
        "desc": "Share your best irrigation practices."
    },
    {
        "img": "https://images.unsplash.com/photo-1498654896293-37aacf113fd9?w=800",
        "title": "Handling Cotton Pest Attacks",
        "desc": "Discuss bollworm & whitefly management."
    },
    {
        "img": "https://images.unsplash.com/photo-1501004318641-b39e6451bec6?w=800",
        "title": "Best Practices for Harvesting",
        "desc": "Learn modern harvesting techniques."
    }
]

cols = st.columns(3)

for i, item in enumerate(featured_items):
    with cols[i % 3]:
        st.markdown(
            f"""
            <div style="
                background:{BG_CARD};
                border:1px solid {BORDER_COLOR};
                border-radius:12px;
                padding:12px;
                margin-bottom:20px;
            ">
                <img src="{item['img']}" style="
                    width:100%; 
                    height:180px;
                    object-fit:cover;
                    border-radius:10px;
                ">
                <h4 style="color:{TEXT_PRIMARY}; font-size:17px; margin-top:10px;">
                    {item['title']}
                </h4>
                <p style="color:{TEXT_SECONDARY}; font-size:14px; margin-top:-5px;">
                    {item['desc']}
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# 7. RECENT POSTS (GRID 3-PER-ROW)
# =========================================================
st.markdown(
    f"<h2 style='color:{TEXT_PRIMARY}; font-size:22px;'>📰 Recent Community Posts</h2>",
    unsafe_allow_html=True,
)

recent_posts = [
    {
        "img": "https://images.unsplash.com/photo-1501004318641-b39e6451bec6?w=600",
        "title": "Leaf Discoloration in Early Stages",
        "desc": "Any suggestions for treating leaf yellowing?",
        "time": "Posted by Arjun • 2 days ago"
    },
    {
        "img": "https://images.unsplash.com/photo-1498654896293-37aacf113fd9?w=600",
        "title": "Fertilizer Recommendations",
        "desc": "Which fertilizers work best for early growth?",
        "time": "Posted by Deepak • 4 days ago"
    },
    {
        "img": "https://images.unsplash.com/photo-1438109491414-7198515b166b?w=600",
        "title": "Prediction Accuracy",
        "desc": "How close was CropWise to your real yield?",
        "time": "Posted by Kavya • 1 week ago"
    }
]

cols2 = st.columns(3)

for i, post in enumerate(recent_posts):
    with cols2[i % 3]:
        st.markdown(
            f"""
            <div style="
                background:{BG_CARD};
                border:1px solid {BORDER_COLOR};
                border-radius:12px;
                padding:12px;
                margin-bottom:20px;
            ">
                <img src="{post['img']}" style="
                    width:100%; 
                    height:150px;
                    object-fit:cover;
                    border-radius:10px;
                ">
                <h4 style="color:{TEXT_PRIMARY}; margin-top:10px; font-size:17px;">
                    {post['title']}
                </h4>
                <p style="color:{TEXT_SECONDARY}; margin-top:-5px; font-size:14px;">
                    {post['desc']}
                </p>
                <p style="color:{TEXT_SECONDARY}; font-size:12px; margin-top:-5px;">
                    {post['time']}
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# 8. VIEW ALL BUTTON
# =========================================================
st.markdown(
    f"""
    <div style="text-align:center; margin-top:20px;">
        <button style="
            background:{BORDER_COLOR};
            color:{TEXT_PRIMARY};
            padding:10px 22px;
            border-radius:25px;
            border:none;
            font-weight:700;
            cursor:pointer;
        ">
            View All Discussions
        </button>
    </div>
    """,
    unsafe_allow_html=True
)
