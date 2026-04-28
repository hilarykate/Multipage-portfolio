import streamlit as st

st.title("🛠️ Skills & Expertise")

# Technical Skills with progress bars
st.subheader("💻 Technical Skills")

skills_data = {
    "Python": 85,
    "JavaScript": 50,
    "Node.js": 75,
    "SQL": 85,
    "HTML/CSS": 88,
    "Git": 82,
}

for skill, level in skills_data.items():
    st.markdown(f"**{skill}**")
    st.progress(level / 100)
    st.caption(f"Level: {level}%")

