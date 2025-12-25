from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .Services.firebase_service import create_firebase_user

@csrf_exempt  # Disable CSRF for simplicity (use proper tokens in production)
def firebase_signup_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get("email")
            password = data.get("password")

            if not email or not password:
                return JsonResponse({"error": "Email and password required"}, status=400)

            user = create_firebase_user(email, password)
            return JsonResponse({
                "id": user.id,
                "email": user.email,
                "firebase_uid": user.firebase_uid
            }, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "POST method required"}, status=405)