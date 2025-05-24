import streamlit as st
import time
import random

# Title
st.title("💰 MoneyMaker-AI Dashboard")

# Sidebar Options
task = st.sidebar.selectbox("Choose Your Task", [
    "Trading Bot",
    "Freelance Bot",
    "Affiliate Bot",
    "Digital Store Bot"
])

# Hourly Earnings Simulation
if "earnings" not in st.session_state:
    st.session_state.earnings = 0

def simulate_earnings():
    earned = random.randint(100, 800)  # simulate ₹100–₹800/hr
    st.session_state.earnings += earned
    return earned

# Task-Based Output
st.header(f"🛠 Running: {task}")
if st.button("▶️ Start Task"):
    with st.spinner("Executing task..."):
        time.sleep(2)
        earned = simulate_earnings()
        st.success(f"Task executed! Earned ₹{earned} this hour.")

# Show Total Earnings
st.metric("💵 Total Earnings", f"₹{st.session_state.earnings}")

# Prompt Box
instruction = st.text_input("📥 Give instruction to the bot:")
if st.button("Send Instruction"):
    st.write(f"✅ Instruction received: {instruction}")
