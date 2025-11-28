import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from utils.language import t

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="CropWise - Login", layout="wide")

# ------------------ FONTS ------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Work+Sans:wght@400;500;700;900&family=Noto+Sans:wght@400;500;700;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Work Sans', 'Noto Sans', sans-serif;
}
</style>
""", unsafe_allow_html=True)

# ------------------ NAVBAR ------------------
st.markdown("""
<style>
.navbar {
    display:flex;
    justify-content:space-between;
    padding:12px 40px;
    border-bottom:1px solid #eef3e8;
}
.nav-links a{
    margin-right:25px;
    font-size:15px;
    color:var(--text);
    text-decoration:none;
    font-weight:500;
}
.brand-title{
    font-size:20px;
    font-weight:700;
    color:var(--text);
}
.signup-btn{
    background:#8de12d;
    padding:8px 20px;
    border-radius:10px;
    color:#151b0e;
    font-weight:700;
    border:none;
}
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class='navbar'>
    <div class='brand-title'>🌾 CropWise</div>

    <div class='nav-links'>
        <a href="/">Home</a>
        <a href="/About">About</a>
        <a href="/Services">Services</a>
        <a href="/Contact">Contact</a>
    </div>

    <button class='signup-btn'>Sign Up</button>
</div>
""", unsafe_allow_html=True)

# ------------------ LOGIN FORM ------------------
st.markdown("""
<h2 style='text-align:center; font-size:28px; font-weight:700; margin-top:25px; color:var(--text);'>
    Login to CropWise
</h2>
""", unsafe_allow_html=True)

st.write("")  # spacing

# Center the form
with st.container():
    st.write("<div style='display:flex; justify-content:center;'>", unsafe_allow_html=True)
    st.write("<div style='width:420px;'>", unsafe_allow_html=True)

    # Username
    username = st.text_input(
        label="",
        placeholder="Username or Email",
        label_visibility="collapsed",
        key="login_username",
    )

    # Password
    password = st.text_input(
        label="",
        placeholder="Password",
        type="password",
        label_visibility="collapsed",
        key="login_password",
    )

    # Forgot password
    st.markdown(
        "<p style='color:#759550; text-decoration:underline; cursor:pointer; font-size:14px;'>"
        "Forgot Password?</p>",
        unsafe_allow_html=True,
    )

    # Login button
    login_clicked = st.button(
        "Login",
        use_container_width=True,
        type="primary",
    )

    if login_clicked:
        if username.strip() == "" or password.strip() == "":
            st.error("Please enter both username and password.")
        else:
            switch_page("Dashboard")

    # Signup link
    st.markdown(
        "<p style='color:#759550; text-align:center; text-decoration:underline; cursor:pointer; font-size:14px;'>"
        "Don't have an account? Sign Up</p>",
        unsafe_allow_html=True,
    )

    st.write("</div></div>", unsafe_allow_html=True)
