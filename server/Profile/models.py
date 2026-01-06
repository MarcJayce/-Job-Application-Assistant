from django.db import models
from django.conf import settings
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, blank=True)
    contact = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    links = models.JSONField(default=dict, blank=True)
    preferences = models.JSONField(default=dict, blank=True)