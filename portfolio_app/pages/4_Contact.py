import streamlit as st
from datetime import datetime
import smtplib
import ssl

st.title("📬 Contact Me")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### Let's Connect!
    
    I'm always interested in new opportunities, collaborations, or just having a chat about technology.
    
    Baleno, Masbate
    
    #### 📧 Email
   valdemorohilary@gmail.com
    
    #### 📱 Phone
    +63 (951) 429-1174
    
    #### 🌐 Social
    - [GitHub](https://github.com/hilarykate)
    - [Instragram](https://www.instagram.com/hyy.rooo?igsh=Z25tMjFnOTl2NGV5)
    """)

with col2:
    st.markdown("### Send me a message")
    
    with st.form("contact_form"):
        name = st.text_input("Name *")
        email = st.text_input("Email *")
        subject = st.text_input("Subject")
        message = st.text_area("Message *", height=150)
        
        submitted = st.form_submit_button("Send Message", use_container_width=True)
        
        if submitted:
            if name and email and message:
                st.success("✅ Message sent successfully! I'll get back to you soon.")
                # Here you would add actual email sending logic
                # For demo purposes, we'll just show a success message
            else:
                st.error("❌ Please fill in all required fields.")
