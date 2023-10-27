import firebase_admin
from firebase_admin import credentials

#Initialize Firebase and save the Firebase app instance
cred = credentials.Certificate("pymder-f3a04-firebase-adminsdk-pjpfq-049f9c9856.json")
firebase_app = firebase_admin.initialize_app(cred, {
    'storageBucket': 'pymder-f3a04.appspot.com',
})
