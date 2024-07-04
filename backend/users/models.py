from django.db import models

class User(models.Model):
    """"""
    id = models.UUIDField(primary_key=True)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)