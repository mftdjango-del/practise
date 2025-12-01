from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(upload_to="users/avatar", null=True, blank=True)
    phone = models.CharField(max_length=15, unique=True)
    full_name = models.CharField(max_length=50)

