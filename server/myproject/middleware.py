# job_app/middleware.py
from django.http import JsonResponse
from firebase_admin import auth as firebase_auth
from users.models import CustomUser

class FirebaseAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Extract token from Authorization header
        id_token = request.headers.get("Authorization")
        if id_token:
            try:
                decoded_token = firebase_auth.verify_id_token(id_token)
                firebase_uid = decoded_token["uid"]

                # Attach CustomUser to request
                try:
                    user = CustomUser.objects.get(firebase_uid=firebase_uid)
                    request.user = user
                except CustomUser.DoesNotExist:
                    request.user = None
            except Exception as e:
                # Invalid token → treat as unauthenticated
                request.user = None
        else:
            request.user = None

        return self.get_response(request)