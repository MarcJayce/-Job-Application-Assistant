# resume/models.py
from django.db import models
from users.models import CustomUser  # adjust import if needed

class Resume(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="resumes")
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to="resumes/")
    content = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.name}"