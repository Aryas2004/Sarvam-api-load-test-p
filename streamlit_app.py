import streamlit as st
import subprocess
import os
import pandas as pd
import time

# Streamlit UI
st.set_page_config(page_title="Sarvam API Load Tester", layout="centered")
st.title("🚀 Sarvam API Load Testing Dashboard")

st.markdown("""
This dashboard lets you run Locust tests with custom parameters and see the results live.
""")

# User Inputs
users = st.number_input("👥 Number of Users (Concurrency)", min_value=1, value=1)
rps = st.number_input("⚡ Spawn Rate (RPS)", min_value=1, value=1)
duration = st.text_input("⏱️ Duration (e.g., 1m, 3m, 5m)", value="1m")

if st.button("▶️ Start Load Test"):
    st.info("Running Locust... Please wait until test completes.")

    # Locust command (update path as needed)
    cmd = f'locust -f "C:/Users/Arya Singh/Desktop/sarvam-load-test/locustfile.py" '
    f'--headless -u {users} -r {rps} --run-time {duration} --csv=output --only-summary'

    # Run the command
    with st.spinner("Executing test..."):
        process = subprocess.Popen(cmd, shell=True)
        process.wait()

    st.success("✅ Test completed!")

    # Wait to ensure file is written
    time.sleep(1)

    # Display Results
    try:
        df = pd.read_csv("output_stats.csv")
        st.subheader("📊 Test Results Summary")
        st.dataframe(df[df["Name"] == "Aggregated"].reset_index(drop=True))

        st.subheader("📈 Latency Metrics (ms)")
        chart_data = df[df["Name"] == "Aggregated"][['50%', '75%', '95%']].T
        chart_data.columns = ['Latency']
        st.bar_chart(chart_data)

    except Exception as e:
        st.error(f"❌ Error reading Locust output: {e}")

st.markdown("""
---
### 🔗 [📄 View Google Sheets Report](https://docs.google.com/spreadsheets/d/12JWWnXaT81N7gOeAZtRX6137LQxk734uwbVthTp83yE/edit?usp=sharing)
""")
