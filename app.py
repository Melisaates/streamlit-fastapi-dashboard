import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Mini Dashboard",
    page_icon="📊",
    layout="centered"
)

st.title("📋 Mini Dashboard")
st.write("Simple Streamlit application with a text list and scatter plot.")

# -------------------------------------------------
# SESSION STATE
# -------------------------------------------------
if "items" not in st.session_state:
    st.session_state["items"] = []

if "points" not in st.session_state:
    st.session_state["points"] = [
        {"x": 1, "y": 2},
        {"x": 3, "y": 5},
        {"x": 5, "y": 1},
    ]

# =================================================
# FEATURE 1 - TEXT ENTRY LIST
# =================================================

st.header("📝 Text Entry List")

text = st.text_input("Enter a new item")

col1, col2 = st.columns(2)

with col1:
    if st.button("➕ Add Item", use_container_width=True):
        if text.strip():
            st.session_state["items"].append(text.strip())

with col2:
    if st.button("🗑 Clear All", use_container_width=True):
        st.session_state["items"].clear()

st.write(f"**Total Items:** {len(st.session_state['items'])}")

if len(st.session_state["items"]) == 0:
    st.info("No items added yet.")
else:

    for index, item in enumerate(st.session_state["items"]):

        left, right = st.columns([8, 1])

        with left:
            st.write(f"• {item}")

        with right:
            if st.button("❌", key=f"delete_{index}"):
                st.session_state["items"].pop(index)
                st.rerun()

    items_df = pd.DataFrame({
        "Item": st.session_state["items"]
    })

    st.download_button(
        label="⬇ Download Items CSV",
        data=items_df.to_csv(index=False),
        file_name="items.csv",
        mime="text/csv"
    )

st.divider()

# =================================================
# FEATURE 2 - SCATTER PLOT
# =================================================

st.header("📈 Scatter Plot")

st.write("Add your own data points.")

colx, coly = st.columns(2)

with colx:
    x_value = st.number_input("X Value", value=0.0)

with coly:
    y_value = st.number_input("Y Value", value=0.0)

if st.button("Add Point"):
    st.session_state["points"].append(
        {
            "x": x_value,
            "y": y_value
        }
    )

points_df = pd.DataFrame(st.session_state["points"])

fig, ax = plt.subplots(figsize=(6, 4))

ax.scatter(
    points_df["x"],
    points_df["y"],
    s=80
)

ax.set_title("Scatter Plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.grid(True)

st.pyplot(fig)

st.write(f"**Total Points:** {len(points_df)}")

st.download_button(
    label="⬇ Download Scatter Data",
    data=points_df.to_csv(index=False),
    file_name="scatter_data.csv",
    mime="text/csv"
)