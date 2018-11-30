import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
from config import firebase_database_url

cred = credentials.Certificate('credentials/firebase_service_key.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': firebase_database_url
})

def get_firebase_data():
    ref = db.reference('/')
    snapshot = ref.get()
    return json.dumps(snapshot, indent=2)
