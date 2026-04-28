import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Portfolio | Hilary Kate",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    /* Main styling */
    .main {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: white;
    }
    
    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Hero section */
    .hero-container {
        text-align: center;
        padding: 4rem 2rem;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        margin: 2rem 0;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .hero-title {
        font-size: 4rem;
        font-weight: 800;
        background: linear-gradient(45deg, #00f5ff, #ff00ff, #00f5ff);
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradient 3s ease infinite;
        margin-bottom: 1rem;
    }
    
    @keyframes gradient {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    
    .hero-subtitle {
        font-size: 1.5rem;
        color: #a0a0a0;
        margin-bottom: 2rem;
    }
    
    .hero-description {
        font-size: 1.1rem;
        color: #c0c0c0;
        max-width: 600px;
        margin: 0 auto 2rem auto;
        line-height: 1.6;
    }
    
    /* Navigation cards */
    .nav-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
        cursor: pointer;
        height: 100%;
    }
    
    .nav-card:hover {
        transform: translateY(-10px);
        background: rgba(255, 255, 255, 0.1);
        border-color: #00f5ff;
        box-shadow: 0 10px 30px rgba(0, 245, 255, 0.2);
    }
    
    .nav-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .nav-title {
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
        color: white;
    }
    
    .nav-desc {
        font-size: 0.9rem;
        color: #a0a0a0;
    }
    
    /* Social links */
    .social-links {
        display: flex;
        justify-content: center;
        gap: 1.5rem;
        margin-top: 2rem;
    }
    
    .social-link {
        font-size: 1.5rem;
        color: #a0a0a0;
        text-decoration: none;
        transition: color 0.3s ease;
    }
    
    .social-link:hover {
        color: #00f5ff;
    }
    
    /* CTA Button */
    .cta-button {
        background: linear-gradient(45deg, #00f5ff, #ff00ff);
        color: white;
        padding: 1rem 2rem;
        border-radius: 50px;
        border: none;
        font-size: 1.1rem;
        font-weight: 600;
        cursor: pointer;
        transition: transform 0.3s ease;
        text-decoration: none;
        display: inline-block;
    }
    
    .cta-button:hover {
        transform: scale(1.05);
    }
    
    /* Stats section */
    .stats-container {
        display: flex;
        justify-content: center;
        gap: 3rem;
        margin: 3rem 0;
        flex-wrap: wrap;
    }
    
    .stat-item {
        text-align: center;
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 800;
        color: #00f5ff;
    }
    
    .stat-label {
        font-size: 0.9rem;
        color: #a0a0a0;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Typing effect */
    .typing-text {
        overflow: hidden;
        border-right: 3px solid #00f5ff;
        white-space: nowrap;
        animation: typing 3.5s steps(40, end), blink-caret 0.75s step-end infinite;
        display: inline-block;
    }
    
    @keyframes typing {
        from { width: 0 }
        to { width: 100% }
    }
    
    @keyframes blink-caret {
        from, to { border-color: transparent }
        50% { border-color: #00f5ff }
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-container">
    <div class="hero-title">Hilary Kate</div>
    <div class="hero-description">
        Passionate about creating elegant solutions to complex problems. 
        I specialize in building modern web applications with cutting-edge technologies.
        Let's build something amazing together!
    </div>
    <a href="/Contact" target="_self" class="cta-button">Get In Touch</a>
</div>
""", unsafe_allow_html=True)

# Navigation Cards
st.markdown("<h2 style='text-align: center; margin: 3rem 0 2rem 0;'>Explore My Portfolio</h2>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <a href="/Aboutme" target="_self" style="text-decoration: none;">
        <div class="nav-card">
            <div class="nav-icon">👤</div>
            <div class="nav-title">About Me</div>
            <div class="nav-desc">Learn about my background, experience, and journey</div>
    </a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <a href="/Skills" target="_self" style="text-decoration: none;">
        <div class="nav-card">
            <div class="nav-icon">⚡</div>
            <div class="nav-title">Skills</div>
            <div class="nav-desc">Discover my technical expertise and capabilities</div>
    </a>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <a href="/Project" target="_self" style="text-decoration: none;">
        <div class="nav-card">
            <div class="nav-icon">🚀</div>
            <div class="nav-title">Projects</div>
            <div class="nav-desc">Check out my latest work and case studies</div>
    </a>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <a href="/Contact" target="_self" style="text-decoration: none;">
        <div class="nav-card">
            <div class="nav-icon">📬</div>
            <div class="nav-title">Contact</div>
            <div class="nav-desc">Get in touch and let's work together</div>
    </a>
    """, unsafe_allow_html=True)


service_col1, service_col2, service_col3 = st.columns(3)


# Footer
st.markdown("""
<div style="text-align: center; margin-top: 4rem; padding: 2rem; color: #666;">
    <p>© 2026 Hilary Kate. Built with Streamlit ❤️</p>
</div>
""", unsafe_allow_html=True)
