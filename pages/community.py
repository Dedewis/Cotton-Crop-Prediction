import streamlit as st

# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(
    page_title="CropWise - Community Forum",
    page_icon="🌾",
    layout="wide"
)

# ---------------------- THEME MODE DETECTION ----------------------
# Streamlit provides "light" or "dark"
theme = st.get_option("theme.base")
is_dark = theme == "dark"

# ---------------------- GLOBAL COLORS ----------------------
TEXT_PRIMARY = "#FFFFFF" if is_dark else "#1c140d"
TEXT_SECONDARY = "#c9b18f" if is_dark else "#9c7349"
BG_PRIMARY = "#111111" if is_dark else "#fcfaf8"
BG_CARD = "#1b1b1b" if is_dark else "#fcfaf8"
BORDER_COLOR = "#3a3a3a" if is_dark else "#f4ede7"

# ---------------------- PAGE WRAPPER ----------------------
st.markdown(
    f"""
    <style>
        body {{
            font-family: 'Plus Jakarta Sans', sans-serif;
        }}

        .title-text {{
            color: {TEXT_PRIMARY};
            font-size: 32px;
            font-weight: 800;
            margin-bottom: -5px;
        }}

        .sub-text {{
            color: {TEXT_SECONDARY};
            font-size: 14px;
            margin-bottom: 20px;
        }}

        .section-title {{
            color: {TEXT_PRIMARY};
            font-size: 22px;
            font-weight: 700;
            margin-top: 25px;
        }}

        .resource-card {{
            background: {BG_CARD};
            border-radius: 16px;
            padding: 12px;
            border: 1px solid {BORDER_COLOR};
            display: flex;
            gap: 12px;
            margin-bottom: 10px;
        }}

        /* Horizontal scroll container */
        .scroll-container {{
            display: flex;
            gap: 20px;
            overflow-x: auto;
            scrollbar-width: none;
        }}
        .scroll-container::-webkit-scrollbar {{
            display: none;
        }}

        .discussion-card {{
            min-width: 240px;
            background: {BG_CARD};
        }}

        .card-title {{
            color: {TEXT_PRIMARY};
            font-size: 16px;
            font-weight: 600;
        }}

        .card-desc {{
            color: {TEXT_SECONDARY};
            font-size: 14px;
        }}
    </style>
    """,
    unsafe_allow_html=True
)


# ---------------------- HEADER ----------------------
st.markdown(f"""
<div class="title-text">Community Forum</div>
<p class="sub-text">
    Connect with other cotton farmers and experts to share insights and discuss crop prediction strategies.
</p>
""", unsafe_allow_html=True)

# ---------------------- FEATURED DISCUSSIONS ----------------------
st.markdown(f"""
<div class="section-title">Featured Discussions</div>
<div class="scroll-container">
""", unsafe_allow_html=True)

featured_items = [
    {
        "img": "https://lh3.googleusercontent.com/aida-public/AB6AXuAk4BOowJARO4S6OWn_mzoJ6J-cwMRsm6nElTxo_VPfnZb03evmPUR-R9fPm3Xb5DFQ54Yw8sIVsGj4q_Dxyyr0F99BiqsvcNNYHr4dPJgRV8PXVgWYWm9I9-Heu58kMWNKT9G33R4THfGXY87UCZvkwpEti6dNiUOVQugaIWWWw2LknS4O3Ad1Nfrs8Z1HU-CgDribueUg1Le_p-waSol3NAEanZXsDL6S4u5QTccsuMvuMgoxHggK6Bdi4-OvASoHnxyxFyDxyio",
        "title": "Optimizing Irrigation for Higher Yields",
        "desc": "Discuss effective irrigation techniques to maximize your cotton yield."
    },
    {
        "img": "https://lh3.googleusercontent.com/aida-public/AB6AXuDNnww8-77Cj6cXCnNuNPMveKPI0CnagAr80XHNbnvR61KKVRgRlfvMvM9fOfvvpbZS8eWaEsIO0TUOWwkhXnPPnYfqiUslHzhRz6f3ibWSJCH__R_Fj_cBsheWOFZKb6dFh7CDKARKOciwVXLqyuWwPJHBjY0uXKBPUEh3iZQAbS3BLxC8yIYJvX445oLdS19xdDmyaBUacCFKqrRMDpjm61LSC2Wqukd1nLO1QlDSjEyxrjPFVxi9s0LiOhG7rZNYgmiEGgLR2V4",
        "title": "Dealing with Common Cotton Pests",
        "desc": "Share your experiences and solutions for managing pests in cotton crops."
    },
    {
        "img": "https://lh3.googleusercontent.com/aida-public/AB6AXuDYEgKeHq0SNKaHNyy_5PU3qcBvUlNwjLE9S6KJAHEqmlbty9Fpo3Qpehc64vOhjyobl8UEvFUzElYkT5rmtqkPGLyxT9rA7ZxUySIzazQy_-4R4iOLVbys-8RWLOKNCSQQ92hsklEktlrD1tqdy-IIow7FZpfXLjmDIRe60CZ32W19KwAPqRa0oXl-1KPYGroWqhaIiSFf8zFflIkZLmc22E_oRUMqVaD3-ZFg7BwBCIdMcFG_JvB_-TuaGgrf0-kVZdVVMM6-dVg",
        "title": "Best Practices for Cotton Harvesting",
        "desc": "Learn and share the best methods for harvesting cotton efficiently."
    }
]

for item in featured_items:
    st.markdown(
        f"""
        <div class="discussion-card">
            <img src="{item['img']}" style="width:100%; border-radius:12px;">
            <p class="card-title">{item['title']}</p>
            <p class="card-desc">{item['desc']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("</div>", unsafe_allow_html=True)

# ---------------------- RECENT POSTS ----------------------
st.markdown(f"""<div class="section-title">Recent Posts</div>""", unsafe_allow_html=True)

recent_posts = [
    {
        "img": "https://lh3.googleusercontent.com/aida-public/AB6AXuCWL19uMR7Nir4Xd1S0CA_t8br57cMuhpykChpyPTd8oAriW3b1BMLZLzcKpZOl6qowIL9MISgLtRhZrSUS2KzTIsfROJwzYE8hNUdPsxBl7qc5HCUJQVGkUXyITgaKDo5OC4D0Fn2Fpytn1wo64n1CsgMVgW_LUks4EAQ8OZoEQvKGhPSoq3ygPYdAaqMn8IdW4iLPtUUSI3dnNTm6OrHZ39TJmp0lPrsHE5FnyMEbMkNWdD2sg38hy20LjLFjZjPNjbgj4PqyIZg",
        "title": "Leaf Discoloration in Cotton Plants",
        "desc": "I've noticed leaf discoloration in my cotton plants. Any advice?",
        "time": "Posted by Alex Bennett | 2 days ago"
    },
    {
        "img": "https://lh3.googleusercontent.com/aida-public/AB6AXuDWW2adVYLNYhlM6ZmoAH1wHB2KMVfMK1n1Bferm8c4I4CTo-zhmTtPbVBgH9Mj19OePmMl6jdTYWS365JEyeS-NHRhlTMKyjKj2uPCEnXDcvxpQkn3zb95qX8pTq4D8a0g970cIzA2OolwzO-F-amHqPaCA-X4u60bhTTre-HvjfYt4TI6pw2w-gX64P4O2JocNwZAzFIK_H3mkocRUFo_QUexcQbL_rApYf7OrjPiPM35yIDNoWXNkcRRqGng35XMWOPCDvqO3K8",
        "title": "Fertilizer Recommendations for Early Growth",
        "desc": "Looking for the best fertilizer options for early-stage cotton.",
        "time": "Posted by Sarah Carter | 4 days ago"
    },
    {
        "img": "https://lh3.googleusercontent.com/aida-public/AB6AXuBWtAhaFwryNP68H_NVL9O9baZmjE0ZipFlDJt4-QIo3Tb6qPqibGWSMk5aeZPWp12dttt90bW5Jg2gR4zdAodTyJSOPoD6euj1a0Q-l98qhKGIUvUx3ewHGKUNLS3Xw0dd7lnkMZXMbsdG3IibfVFU0Vfd6tMNbL9Bk8xat-soI8btyN5eP7j6tJhllTDAhzJaMenqO5QYX5evMWGkeikjtaRJjmxnyOF8vKKmGrSccEb_gkxrG89VD6q18hI_pPWCRpJ5Nvk90_g",
        "title": "Crop Prediction Accuracy",
        "desc": "Has anyone compared predicted yield vs actual harvest?",
        "time": "Posted by David Lee | 1 week ago"
    },
]

for post in recent_posts:
    st.markdown(
        f"""
        <div class="resource-card">
            <img src="{post['img']}" style="width:70px; height:70px; border-radius:50%;">
            <div>
                <p class="card-title">{post['title']}</p>
                <p class="card-desc">{post['desc']}</p>
                <p class="card-desc">{post['time']}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ---------------------- VIEW ALL BUTTON ----------------------
st.markdown(
    f"""
    <div style="text-align:center; margin-top:20px;">
        <button style="
            background:{BORDER_COLOR};
            color:{TEXT_PRIMARY};
            padding:10px 20px;
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
