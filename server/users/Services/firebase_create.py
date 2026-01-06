from firebase_admin import auth as firebase_auth
from ..models import CustomUser  # or from job_app.models if outside the app

def create_firebase_user(email, password):
    # Create user in Firebase
    user_record = firebase_auth.create_user(
        email=email,
        password=password
    )
    # Mirror user in Django SQL database
    user, created = CustomUser.objects.get_or_create(
        firebase_uid=user_record.uid,
        defaults={'email': email}
    )
    return user