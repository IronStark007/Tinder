from distutils.command.config import config
import pyrebase

from app.config import get_config

config = get_config()

class FireBase:
    firebaseConfig = {
        "apiKey": config.api_key,
        "authDomain": config.auth_domain,
        "databaseURL": config.database_url,
        "projectId": config.project_id,
        "storageBucket": config.storage_bucket,
        "messagingSenderId": config.messaging_sender_id,
        "appId": config.app_id,
        "measurementId": config.measurement_id
    }

    def __init__(self):
        firebase = pyrebase.initialize_app(self.firebaseConfig)
        self.auth = firebase.auth()
        self.database = firebase.database()
        self.storage = firebase.storage()


firebase = FireBase()