import streamlit as st

def app():
    st.title("About Me")

    # Education Section
    st.header("Education")
    st.write("🎓 Bachelor's in [Your Major], [Your University], Expected Graduation: [Year]")

    # Skills Section
    st.header("Skills")
    skills = ["Python", "Data Analysis", "Machine Learning", "Web Development", "Git"]
    st.write("\n".join(f"- {skill}" for skill in skills))

    # Coursework Section
    st.header("Coursework")
    courses = [
        "Introduction to Computer Science",
        "Data Structures and Algorithms",
        "Database Systems",
        "Artificial Intelligence"
    ]
    st.write("\n".join(f"- {course}" for course in courses))

    # Extracurricular Activities Section
    st.header("Extracurricular Activities")
    activities = [
        "Member of Computer Science Club",
        "Volunteer at local coding bootcamp for high school students"
    ]
    st.write("\n".join(f"- {activity}" for activity in activities))

if __name__ == "__main__":
    app()
