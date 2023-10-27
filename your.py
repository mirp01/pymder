import streamlit as st
from firebase_admin import firestore
from initialize import firebase_app  # Import the Firebase app instance
from firebase_admin import storage
import datetime

# Function to display images from Firebase Storage
def display_images(username):
    st.title("Image gallery")
    st.markdown("Here you can see the images you have uploaded")
    bucket = storage.bucket(app=firebase_app)  # Specify the pre-initialized Firebase app
    blobs = bucket.list_blobs(prefix=f"images/{username}")
    for blob in blobs:
        url = blob.generate_signed_url(datetime.timedelta(hours=1))
        st.image(url, caption=blob.name)

def app():
    db = firestore.client()

    # Retrieve usernames from Firestore and store them in a list
    usernames = []
    docs = db.collection('Posts').stream()
    for doc in docs:
        usernames.append(doc.id)

    option = st.selectbox(
        'Whose profile are you going to see?',
        usernames
    )

    try:
        display_images(option)
        st.title('Posted by: ' + option)

        result = db.collection('Posts').document(option).get()
        r = result.to_dict()
        content = r.get('Content', [])

        def delete_post(k):
            c = int(k)
            h = content[c]
            try:
                db.collection('Posts').document(option).update({"Content": firestore.ArrayRemove([h])})
                st.warning('Post deleted')
            except:
                st.write('Something went wrong..')

        for c in range(len(content) - 1, -1, -1):
            st.text_area(label='', value=content[c])
            st.button('Delete Post', on_click=delete_post, args=([c]), key=c)

    except:
        if st.session_state.username == '':
            st.text('Please login first')