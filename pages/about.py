import streamlit as st
from firebase_admin import firestore

def app():
    db=firestore.client()

    try:
        st.subheader(st.session_state['username'])
        st.markdown('Contact via mail: [pymder@gmail.com]')
    except:
        if st.session.state.username=='':
            st.text('Please Login first')
    