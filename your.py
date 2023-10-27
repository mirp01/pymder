import streamlit as st
from firebase_admin import firestore
from initialize import firebase_app  # Import the Firebase app instance
from firebase_admin import storage
import datetime

# Function to display images from Firebase Storage
def display_images():
    st.title("Image gallery")
    st.markdown("Here you can see the images you have uploaded")
    bucket = storage.bucket(app=firebase_app)  # Specify the pre-initialized Firebase app
    blobs = bucket.list_blobs(prefix="images/")
    for blob in blobs:
        url = blob.generate_signed_url(datetime.timedelta(hours=1))
        st.image(url, caption=blob.name)

def app():
    db=firestore.client()


    try:
        if st.session_state.username=='':
            st.title("Nothing in here")
            st.text("It is pretty Lonely in here")
            
        else:
            display_images()
        
            st.title('Posted by: '+st.session_state['username'] )

            
        result = db.collection('Posts').document(st.session_state['username']).get()
        r=result.to_dict()
        content = r['Content']
            
        
        def delete_post(k):
            c=int(k)
            h=content[c]
            try:
                db.collection('Posts').document(st.session_state['username']).update({"Content": firestore.ArrayRemove([h])})
                st.warning('Post deleted')
            except:
                st.write('Something went wrong..')
                
        for c in range(len(content)-1,-1,-1):
            st.text_area(label='',value=content[c])
            st.button('Delete Post', on_click=delete_post, args=([c] ), key=c)        

        
    except:
        if st.session_state.username=='':
            st.text('Please Login first')        