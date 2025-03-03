import streamlit as st

def app():
    st.title("Welcome to My Student Portfolio")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("assets/profile_picture.jpg", width=200)
    
    with col2:
        st.write("## Hello! I'm [Your Name]")
        st.write("I'm an undergraduate student majoring in [Your Major] at [Your University].")
        st.write("This portfolio showcases my academic projects, skills, and achievements.")
        
    st.write("---")
    st.write("## Quick Links")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("📚 View Projects")
    with col2:
        st.button("👤 About Me")
    with col3:
        st.button("📧 Contact")
