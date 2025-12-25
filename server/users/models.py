from django.contrib.auth.models import AbstractUser
from django.db import models

# Abstract user gives us all the default fields (username, email, password, first_name, last_name, etc.)
class CustomUser(AbstractUser):
    # Store Firebase UID separately
    firebase_uid = models.CharField(max_length=128, unique=True)
  