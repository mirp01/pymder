import streamlit as st
from firebase_admin import firestore
from PIL import Image

#Matchmaking system
class Elo:

	def __init__(self,k,g=1,homefield = 100):
		self.ratingDict  	= {}	
		self.k 				= k
		self.g 				= g
		self.homefield		= homefield

	def addPlayer(self,name,rating = 1500):
		self.ratingDict[name] = rating
		
	def gameOver(self, winner, loser, winnerHome):
		if winnerHome:
			result = self.expectResult(self.ratingDict[winner] + self.homefield, self.ratingDict[loser])
		else:
			result = self.expectResult(self.ratingDict[winner], self.ratingDict[loser]+self.homefield)

		self.ratingDict[winner] = self.ratingDict[winner] + (self.k*self.g)*(1 - result)  
		self.ratingDict[loser] 	= self.ratingDict[loser] + (self.k*self.g)*(0 - (1 -result))
		
	def expectResult(self, p1, p2):
		exp = (p2-p1)/400.0
		return 1/((10.0**(exp))+1)

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
