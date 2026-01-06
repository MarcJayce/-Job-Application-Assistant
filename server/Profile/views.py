# profile/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import json

from .models import Profile

@csrf_exempt
@login_required
def update_profile(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))

        profile, created = Profile.objects.get_or_create(user=request.user)

        # Update fields one by one if present in request
        if "full_name" in data:
            profile.full_name = data["full_name"]
        if "contact" in data:
            profile.contact = data["contact"]
        if "location" in data:
            profile.location = data["location"]
        if "links" in data:
            profile.links = data["links"]
        if "preferences" in data:
            profile.preferences = data["preferences"]

        profile.save()

        return JsonResponse({
            "message": "Profile updated successfully",
            "profile": {
                "full_name": profile.full_name,
                "contact": profile.contact,
                "location": profile.location,
                "links": profile.links,
                "preferences": profile.preferences,
            }
        })
    return JsonResponse({"error": "Invalid request"}, status=400)