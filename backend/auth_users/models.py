from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

class CustomUser(AbstractUser, PermissionsMixin):
    username = None
    email = models.EmailField(max_length=200, unique=True, null=False)
    password = models.CharField(max_length=500, null=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
