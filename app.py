import streamlit as st
import requests
import matplotlib.pyplot as plt

BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Full Stack Dashboard", layout="centered")

st.title("📋 Full Stack Dashboard (Streamlit + FastAPI)")

# =========================
# FEATURE 1 - ITEMS
# =========================

st.header("📝 Items (API Powered)")

# GET items
try:
    items = requests.get(f"{BASE_URL}/items").json()
except:
    items = []

text = st.text_input("Enter item")

col1, col2 = st.columns(2)

with col1:
    if st.button("➕ Add Item"):
        if text.strip():
            requests.post(
                f"{BASE_URL}/items",
                json={"text": text}
            )
            st.rerun()

with col2:
    if st.button("🔄 Refresh"):
        st.rerun()

st.write(f"Total Items: {len(items)}")

if items:
    for item in items:
        st.write(f"• {item}")
else:
    st.info("No items yet.")

st.divider()

# =========================
# FEATURE 2 - SCATTER PLOT
# =========================

st.header("📈 Scatter Plot (API Data)")

x = st.number_input("X Value", value=0.0)
y = st.number_input("Y Value", value=0.0)

if st.button("➕ Add Point"):
    requests.post(
        f"{BASE_URL}/points",
        json={"x": x, "y": y}
    )
    st.rerun()

# GET points
try:
    points = requests.get(f"{BASE_URL}/points").json()
except:
    points = []

if points:
    xs = [p["x"] for p in points]
    ys = [p["y"] for p in points]

    fig, ax = plt.subplots(figsize=(6, 4))

    # Scatter
    ax.scatter(xs, ys, s=80, alpha=0.8, label="Points")

    # Line connection
    if len(xs) > 1:
        ax.scatter(xs, ys, s=80, alpha=0.8)

    # Styling
    ax.set_title("Scatter Plot (FastAPI Data)")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.legend()

    st.pyplot(fig)

    st.write(f"Total Points: {len(points)}")
else:
    st.info("No points yet.")