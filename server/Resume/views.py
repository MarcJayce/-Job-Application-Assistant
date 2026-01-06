import pdfplumber
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Resume

@csrf_exempt
def upload_resume(request):
    if request.method == "POST":
        if not request.user:
            return JsonResponse({"error": "Unauthorized"}, status=401)

        pdf_file = request.FILES["resume"]
        resume = Resume.objects.create(
            user=request.user,
            file=pdf_file,
            name=pdf_file.name
        )

        text = ""
        with pdfplumber.open(resume.file.path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

        resume.content = text
        resume.save()

        return JsonResponse({
            "id": resume.id,
            "name": resume.name,
            "user_id": request.user.id,
            "firebase_uid": request.user.firebase_uid,
            "uploaded_at": resume.uploaded_at,
        }, status=201)

    return JsonResponse({"error": "POST method required"}, status=405)