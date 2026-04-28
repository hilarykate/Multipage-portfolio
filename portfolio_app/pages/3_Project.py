import streamlit as st

st.title("My Projects")


st.markdown("---")

# Project 1
with st.container():
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("images/cert1.jpg", use_container_width=True)
    
    with col2:
        st.subheader("introduction to Cyber Security")
        

st.markdown("---")

# Project 2
with st.container():
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("images/cert2.jpg", use_container_width=True)
    
    with col2:
        st.subheader("Python for beginners")
       
        col_a, col_b, col_c = st.columns(3)
        
st.markdown("---")

# Project 3
with st.container():
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("images/cert3.jpg", use_container_width=True)
    
    with col2:
        st.subheader("Python Essentials 1")
        
        col_a, col_b, col_c = st.columns(3)
        
# Add more projects button
st.markdown("---")
if st.button("Load More Projects", use_container_width=True):
    st.info("More projects coming soon! 🚀")

