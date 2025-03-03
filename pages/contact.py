import streamlit as st

def app():
    st.title("Contact Me")
    
    st.write("I'm always open to new opportunities and collaborations. Feel free to reach out!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("## Contact Information")
        st.write("📧 Email: your.email@example.com")
        st.write("📱 Phone: (123) 456-7890")
        st.write("🌐 LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/in/yourprofile)")
        st.write("🐙 GitHub: [Your GitHub Profile](https://github.com/yourusername)")
    
    with col2:
        st.write("## Send me a message")
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        if st.button("Send"):
            st.success("Message sent successfully!")
