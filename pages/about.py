import streamlit as st

def app():
    st.title("About Me")
    
    st.write("## Education")
    st.write("🎓 Bachelor's in [Your Major], [Your University], Expected Graduation: [Year]")
    
    st.write("## Skills")
    skills = ["Python", "Data Analysis", "Machine Learning", "Web Development", "Git"]
    for skill in skills:
        st.write(f"- {skill}")
    
    st.write("## Coursework")
    courses = ["Introduction to Computer Science", "Data Structures and Algorithms", "Database Systems", "Artificial Intelligence"]
    for course in courses:
        st.write(f"- {course}")
    
    st.write("## Extracurricular Activities")
    activities = ["Member of Computer Science Club", "Volunteer at local coding bootcamp for high school students"]
    for activity in activities:
        st.write(f"- {activity}")
