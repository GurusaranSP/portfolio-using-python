import streamlit as st
from typing import Literal

def app() -> None:
    st.title("Contact Me")
    
    st.write("I'm always open to new opportunities and collaborations. Feel free to reach out!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("## Contact Information")
        contact_info: dict[Literal["Email", "Phone", "LinkedIn", "GitHub"], str] = {
            "Email": "your.email@example.com",
            "Phone": "(123) 456-7890",
            "LinkedIn": "[Your LinkedIn Profile](https://www.linkedin.com/in/yourprofile)",
            "GitHub": "[Your GitHub Profile](https://github.com/yourusername)"
        }
        for method, info in contact_info.items():
            st.write(f"{method}: {info}")
    
    with col2:
        st.write("## Send me a message")
        name: str = st.text_input("Name")
        email: str = st.text_input("Email")
        message: str = st.text_area("Message")
        if st.button("Send"):
            st.success("Message sent successfully!")

if __name__ == "__main__":
    app()
