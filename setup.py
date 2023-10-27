import streamlit as st
from initialize import firebase_app  # Import the Firebase app instance
from firebase_admin import storage
import datetime
from firebase_admin import firestore

# Function to upload an image to Firebase Storage
def upload_image():
    st.header("Upload an Image so that everyone can see how cool you are")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])
    if uploaded_file is not None:
        bucket = storage.bucket(app=firebase_app)  # Specify the pre-initialized Firebase app
        blob = bucket.blob(f"images/{st.session_state['username']}/{uploaded_file.name}")
        blob.upload_from_file(uploaded_file)
        st.markdown("Image succesfully uploaded!")

def cuidadNTags():
    db=firestore.client()
    option = st.selectbox(
    'Where is your bussiness located?',
    ('Pueblo paleta', 'Machupichu', 'El reino de muy muy lejano', 'Guadalajara', 'Jocotepec'),placeholder='Select one form the options')
    if st.button('Set Cuidad',use_container_width=20):
        if option!='':
                    
            info = db.collection('Cuidad').document(st.session_state.username).get()
            if info.exists:
                info = info.to_dict()
                if 'Content' in info.keys():
                
                    pos=db.collection('Cuidad').document(st.session_state.username)
                    pos.update({u'Content': firestore.ArrayUnion([u'{}'.format(option)])})
        st.write('Cuidad uploaded')

# Main function to run the app
def app():
    st.title('This is were you set up your business account')
    if st.session_state.username=='':
        st.header('Please log in or create an account')
    else:
        st.subheader('Start uploading to your profile')
        upload_image()
        cuidadNTags()
    