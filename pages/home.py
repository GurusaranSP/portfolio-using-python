import streamlit as st
from pathlib import Path

def app():
    st.title("Welcome to My Student Portfolio")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        profile_pic = Path("assets/profile_picture.jpg")
        if profile_pic.exists():
            st.image(profile_pic, width=200)
        else:
            st.error("Profile picture not found!")
    
    with col2:
        st.markdown("## Hello! I'm [Your Name]")
        st.markdown("I'm an undergraduate student majoring in [Your Major] at [Your University].")
        st.markdown("This portfolio showcases my academic projects, skills, and achievements.")
        
    st.divider()  # This is a new Streamlit feature for adding a divider
    st.markdown("## Quick Links")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("📚 View Projects"):
            st.switch_page("pages/projects.py")  # Assumes you have a projects.py in a pages folder
    with col2:
        if st.button("👤 About Me"):
            st.switch_page("pages/about.py")  # Assumes you have an about.py in a pages folder
    with col3:
        if st.button("📧 Contact"):
            st.switch_page("pages/contact.py")  # Assumes you have a contact.py in a pages folder

if __name__ == "__main__":
    app()
