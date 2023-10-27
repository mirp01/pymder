import streamlit as st

from streamlit_option_menu import option_menu


import pages.home as home, pages.test as test, pages.your as your, pages.about as about, pages.setup as setup
st.set_page_config(
        page_title="PYMDER",
)

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='Pymder app ',
                options=['Home','Account','Set up','Your Preview','about'],
                icons=['house-fill','person-circle','trophy-fill','chat-fill','info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

        
        if app == "Home":
            home.app()
        if app == "Account":
            test.app()
        if app == 'Set up':
            setup.app()         
        if app == 'Your Preview':
            your.app()
        if app == 'about':
            about.app()    
             
          
             
    run()            