import streamlit as st
from firebase_admin import firestore

def app():
    st.subheader(st.session.username)
    st.subheader('share their valuable thoughts with the world.')
    st.markdown('Created by: [Ashwani Siwach](https://github.com/Ashwani132003)')
    st.markdown('Contact via mail: [siwachsahab1@gmail.com]')
    