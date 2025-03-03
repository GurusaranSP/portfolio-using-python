import streamlit as st
from streamlit_option_menu import option_menu
from pages import home, about, projects, contact

st.set_page_config(page_title="Your Name - Student Portfolio", layout="wide")

class MultiApp:
    def __init__(self):
        self.apps: list[dict[str, str | callable]] = []

    def add_app(self, title: str, func: callable) -> None:
        self.apps.append({"title": title, "function": func})

    def run(self) -> None:
        with st.sidebar:
            app = option_menu(
                menu_title="Navigation",
                options=["Home", "About", "Projects", "Contact"],
                icons=["house-fill", "person-fill", "code-slash", "envelope-fill"],
                menu_icon="mortarboard-fill",
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": "#f0f2f6"},
                    "icon": {"color": "#0083B8", "font-size": "25px"}, 
                    "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#e1e1e1"},
                    "nav-link-selected": {"background-color": "#0083B8"},
                }
            )

        match app:
            case "Home":
                home.app()
            case "About":
                about.app()
            case "Projects":
                projects.app()
            case "Contact":
                contact.app()

if __name__ == "__main__":
    multi_app = MultiApp()
    multi_app.run()
