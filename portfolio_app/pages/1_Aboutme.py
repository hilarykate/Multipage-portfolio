import streamlit as st

st.title("📖 About Me")

col1, col2 = st.columns([1, 2])

with col1:
    st.image(
        "portfolio_app/images/hyla.jpg",
        caption="Hilary Kate",
        use_container_width=True
    )

with col2:
    st.markdown("""
    ### Hi there! 👋

    I am Hilary kate a computer science student. enjoying learning how computer works and creating stsyem that can makes tasks easier and more efficient.
    #### 🎯 My Mission
    To build innovative applications that make a positive impact on people's lives
    while maintaining clean, efficient, and scalable code.
    """)

st.markdown("---")

# Personal info in columns
st.subheader("📋 Personal Information")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    - **📍 Location:** Baleno, Masbate
    - **🎓 Education:** B.S. in Computer Science
    """)

with col2:
    st.markdown("""
    - **🌐 Languages:** English, Spanish
    - **🎯 Interests:** AI, Open Source, Gaming
    - **⚡ Hobbies:** Photography, Playing vollyball, Travel
    """)
