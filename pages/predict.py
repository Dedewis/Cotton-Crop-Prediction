import streamlit as st
import json

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(page_title="Predict – CropWise", layout="wide")

# -----------------------------------
# LOAD INDIA STATE → DISTRICT JSON
# -----------------------------------
with open("data/india_states.json", "r", encoding="utf-8") as f:
    india_data = json.load(f)

states = [item["state"] for item in india_data]


# -----------------------------------
# TITLE SECTION
# -----------------------------------
st.markdown(
    """
    <h1 style='text-align:center; color:#1c140d;'>🌾 Cotton Yield Prediction</h1>
    <p style='text-align:center; color:#4c3a28; margin-top:-10px;'>
        Select your State and District to generate yield prediction.
    </p>
    """,
    unsafe_allow_html=True,
)

st.write("")  # spacing


# -----------------------------------
# FORM CARD UI
# -----------------------------------
st.markdown(
    """
    <div style="
        background:#f4ede7;
        padding: 24px;
        border-radius:16px;
        max-width:480px;
        margin:auto;
        border:1px solid #e8dbce;
    ">
    """,
    unsafe_allow_html=True,
)

# 🔽 STATE SELECT
state = st.selectbox("State", ["Select State"] + states)

# 🔽 DISTRICT SELECT (dynamic)
district_list = []

if state != "Select State":
    for entry in india_data:
        if entry["state"] == state:
            district_list = entry["districts"]

district = st.selectbox(
    "District",
    ["Select District"] + district_list if district_list else ["Select District"],
)

# -----------------------------------
# PREDICT BUTTON
# -----------------------------------
predict_btn = st.button(
    "🔍 Predict Yield",
    use_container_width=True,
)

st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------------
# HANDLE SELECTION
# -----------------------------------
if predict_btn:
    if state == "Select State" or district == "Select District":
        st.error("⚠️ Please select both State and District.")
    else:
        st.session_state["selected_state"] = state
        st.session_state["selected_district"] = district

        st.success("✔ Selection saved successfully!")
        st.info("Now go to the **Result** page to view the prediction.")


