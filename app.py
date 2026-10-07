import sqlite3
import streamlit as st

# 1. डेटाबेस सेटअप (SQLite Database Connection)
conn = sqlite3.connect('dreams.db', check_same_thread=False)
cursor = conn.cursor()

# टेबल बनाना अगर पहले से न हो
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS dreams (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        category TEXT,
        mood TEXT,
        intensity REAL,
        description TEXT
    )
"""
)
conn.commit()

st.set_page_config(
    page_title="Dream-Log: Neuroscience + AI", page_icon="🌙", layout="centered"
)

st.markdown(
    """
    <div style='text-align: center;'>
        <h1>🌙 Dream-Log: Neuroscience + AI</h1>
        <p><b>Welcome to your personal dream journal, neural analytics & AI platform.</b></p>
    </div>
""",
    unsafe_allow_html=True,
)

# मुख्य इनपुट फॉर्म
st.markdown("### 📝 Log Your Dream")
dreamer_name = st.text_input("Dreamer's Name", value="Abu Shad")
dream_category = st.selectbox(
    "Dream Category", ["Lucid", "Nightmare", "Recurring", "Surreal", "Cosmic"]
)
dream_mood = st.selectbox(
    "Current Sleep & Mood State",
    ["Calm & Rested", "Anxious", "Excited", "Tired", "Euphoric"],
)

dream_desc = st.text_area(
    "Describe your dream in detail...",
    placeholder="Write what you saw in your dream...",
)

if st.button("Analyze, Save & Generate AI Prompt"):
  if dream_desc.strip() == "":
    st.warning("कृपया पहले अपने सपने का विवरण दर्ज करें!")
  else:
    # न्यूरोलॉजिकल इंटेंसिटी स्कोर कैलकुलेशन
    base_score = min(
        10.0, round(float(len(dream_desc.split())) / 5.0 + 5.0, 1)
    )

    # डेटाबेस में सेव करना
    cursor.execute(
        """
        INSERT INTO dreams (name, category, mood, intensity, description) 
        VALUES (?, ?, ?, ?, ?)
    """,
        (dreamer_name, dream_category, dream_mood, base_score, dream_desc),
    )
    conn.commit()

    st.success("✨ Dream Logged Successfully & Saved to Database!")

    st.markdown("---")
    st.markdown("### 📊 Dream Insights & Neural Analytics")
    st.write(f"**Dreamer:** {dreamer_name}")
    st.write(f"**Category:** {dream_category}")
    st.write(f"**Mood State:** {dream_mood}")
    st.write(f"**Neurological Intensity Score:** {base_score} / 10")

    # AI इमेज प्रॉम्प्ट जनरेशन
    ai_prompt = f"Cinematic 8k resolution, surreal representation of a {dream_category.lower()} dream involving {dream_desc[:100]}..., highly detailed, ethereal neural lighting, trending on artstation."
    st.info(f"**AI Image Prompt:** {ai_prompt}")

# 2. सपनों का इतिहास और स्लीप/मूड एनालिटिक्स ग्राफ
st.markdown("---")
st.markdown("### 📈 Sleep & Mood Analytics Dashboard")

# डेटाबेस से सभी सपने फेच करना
cursor.execute("SELECT category, intensity, mood FROM dreams")
all_dreams = cursor.fetchall()

if all_dreams:
  intensities = [row[1] for row in all_dreams]
  st.write(f"कुल दर्ज किए गए सपने: **{len(all_dreams)}**")
  st.bar_chart(intensities)
  st.caption("सपनों के न्यूरोलॉजिकल इंटेंसिटी स्कोर का विजुअल ग्राफ")
else:
  st.info("अभी तक कोई डेटा मौजूद नहीं है। ऊपर फॉर्म भरकर अपना पहला सपना सेव करें!")
