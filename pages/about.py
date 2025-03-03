import streamlit as st

def app():
    st.title("About Me")
    
    st.markdown("## Education")
    st.markdown("🎓 Bachelor's in [Your Major], [Your University], Expected Graduation: [Year]")
    
    st.markdown("## Skills")
    skills = ["Python", "Data Analysis", "Machine Learning", "Web Development", "Git"]
    st.markdown("\n".join(f"- {skill}" for skill in skills))
    
    st.markdown("## Coursework")
    courses = ["Introduction to Computer Science", "Data Structures and Algorithms", "Database Systems", "Artificial Intelligence"]
    st.markdown("\n".join(f"- {course}" for course in courses))
    
    st.markdown("## Extracurricular Activities")
    activities = ["Member of Computer Science Club", "Volunteer at local coding bootcamp for high school students"]
    st.markdown("\n".join(f"- {activity}" for activity in activities))

if __name__ == "__main__":
    app()
