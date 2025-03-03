import streamlit as st
from pathlib import Path

def app():
    st.title("Welcome to My Student Portfolio")

    col1, col2 = st.columns([1, 2])

    with col1:
        profile_pic_path = Path("assets/profile_picture.jpg")
        if profile_pic_path.exists():
            st.image(str(profile_pic_path), width=200)
        else:
            st.warning("⚠ Profile picture not found!")

    with col2:
        st.markdown("## Hello! I'm [Your Name]")
        st.markdown("I'm an undergraduate student majoring in [Your Major] at [Your University].")
        st.markdown("This portfolio showcases my academic projects, skills, and achievements.")

    st.divider()  # Streamlit feature for a horizontal divider

    st.markdown("## Quick Links")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📚 View Projects"):
            st.page_link("pages/projects.py", label="📚 View Projects")

    with col2:
        if st.button("👤 About Me"):
            st.page_link("pages/about.py", label="👤 About Me")

    with col3:
        if st.button("📧 Contact"):
            st.page_link("pages/contact.py", label="📧 Contact")

if __name__ == "__main__":
    app()
