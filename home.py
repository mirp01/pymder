import streamlit as st
from firebase_admin import firestore
from PIL import Image
import datetime
from firebase_admin import storage
from initialize import firebase_app  # Import the Firebase app instance

def display_images(username):
    st.title(f"{st.session_state['username']} Image gallery")
    st.markdown(f"This are the images {username} has uploaded")
    bucket = storage.bucket(app=firebase_app)  # Specify the pre-initialized Firebase app
    blobs = bucket.list_blobs(prefix=f"images/{username}")
    for blob in blobs:
        url = blob.generate_signed_url(datetime.timedelta(hours=1))
        st.image(url, caption=blob.name)

#operaciones del matchmaking
def colEloCollab():
    return

def app():
    
    if 'db' not in st.session_state:
        st.session_state.db = ''

    db=firestore.client()
    st.session_state.db=db
    st.title('  :red[Pymder]  :moneybag:')
    
    ph = ''
    if st.session_state.username=='':
        st.header(' Please login or create an account')
        ph = 'Login to Start collaborating!!'
        image = Image.open('C:/Users/edosa/Documents/Pymder app/firabaseDB/pymder_logo.png')
        st.image(image, caption= "Posible collaborations will show here!")
    else:
        ph='Looking good'
        image = Image.open('C:/Users/edosa/Documents/Pymder app/firabaseDB/Pymder.png')
        st.image(image, caption= "Posible collaborations will show here!")
        
    post=st.text_area(label=' :orange[+ New Post]',placeholder=ph,height=None, max_chars=500)
    if st.button('Post',use_container_width=20):
        if post!='':
                    
            info = db.collection('Posts').document(st.session_state.username).get()
            if info.exists:
                info = info.to_dict()
                if 'Content' in info.keys():
                
                    pos=db.collection('Posts').document(st.session_state.username)
                    pos.update({u'Content': firestore.ArrayUnion([u'{}'.format(post)])})
                    # st.write('Post uploaded!!')
                else:
                    
                    data={"Content":[post],'Username':st.session_state.username}
                    db.collection('Posts').document(st.session_state.username).set(data)    
            else:
                    
                data={"Content":[post],'Username':st.session_state.username}
                db.collection('Posts').document(st.session_state.username).set(data)
                
            st.success('Post uploaded!!')
    
            st.header(' :violet[Latest Posts] ')
            
            
            docs = db.collection('Posts').get()
                    
            for doc in docs:
                d=doc.to_dict()
                try:
                    st.text_area(label=':green[Posted by:] '+':orange[{}]'.format(d['Username']),value=d['Content'][-1],height=20)
                except: pass
