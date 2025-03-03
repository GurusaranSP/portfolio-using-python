import streamlit as st

def app():
    st.title("My Projects")
    
    projects = [
        {
            "title": "Machine Learning Classification Model",
            "description": "Developed a classification model to predict customer churn using scikit-learn.",
            "technologies": ["Python", "scikit-learn", "pandas", "matplotlib"],
            "github_link": "https://github.com/yourusername/project1"
        },
        {
            "title": "Web Scraping and Data Visualization",
            "description": "Created a web scraper to collect data from e-commerce websites and visualized pricing trends.",
            "technologies": ["Python", "BeautifulSoup", "requests", "matplotlib", "seaborn"],
            "github_link": "https://github.com/yourusername/project2"
        },
        # Add more projects here
    ]
    
    for project in projects:
        st.write(f"## {project['title']}")
        st.write(project['description'])
        st.write("**Technologies used:**")
        for tech in project['technologies']:
            st.write(f"- {tech}")
        st.write(f"[View on GitHub]({project['github_link']})")
        st.write("---")
