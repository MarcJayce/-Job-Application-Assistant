import os
from firebase_admin import credentials, initialize_app

FIREBASE_KEY_PATH = os.getenv("FIREBASE_KEY")

if FIREBASE_KEY_PATH:
    cred = credentials.Certificate(FIREBASE_KEY_PATH)
    default_app = initialize_app(cred)
