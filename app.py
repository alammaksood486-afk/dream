
import streamlit as st

st.set_page_config(page_title="Dream-Log", page_icon="🌙", layout="centered")

st.title("🌙 Dream-Log: Neuroscience + AI")
st.write("Welcome to your personal dream journal and AI analysis platform.")

dreamer_name = st.text_input("Dreamer's Name", value="Abu Shad")
category = st.selectbox("Dream Category", ["Lucid", "Nightmare", "Prophetic", "Surreal", "Vivid"])
dream_text = st.text_area("Describe your dream in detail...")

if st.button("Analyze & Generate AI Prompt"):
    if dream_text:
        st.success("Dream Logged Successfully!")
        st.subheader("📊 Dream Insights")
        st.write(f"**Dreamer:** {dreamer_name}")
        st.write(f"**Category:** {category}")
        st.write(f"**Intensity Score:** 8.5 / 10")
        
        ai_prompt = f"Cinematic 8k resolution, surreal representation of a {category.lower()} dream: {dream_text}, highly detailed, ethereal lighting."
        st.info(f"**AI Image Prompt:** {ai_prompt}")
    else:
        st.warning("Please enter your dream description first.")
