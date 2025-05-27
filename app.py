
import streamlit as st
import json
from strategy import run_strategy
from telegram_bot import send_telegram_alert

st.set_page_config(page_title="AI Trading Bot Dashboard", layout="wide")
st.title("📈 AI Trading Bot Dashboard")

# Login check
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    with st.form("Login"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")
        if submitted:
            with open("users.json") as f:
                users = json.load(f)
            if username in users and users[username] == password:
                st.session_state.logged_in = True
            else:
                st.error("Invalid credentials")

if st.session_state.logged_in:
    st.sidebar.success("Logged in as admin")
    symbol = st.selectbox("Select Symbol", ["XAUUSD", "US30", "NAS100"])
    run = st.button("Run Paper Test")

    if run:
        st.write(f"Running strategy for {symbol}...")
        result = run_strategy(symbol)
        st.json(result)
        send_telegram_alert(f"Paper trade executed on {symbol}: {result}")
