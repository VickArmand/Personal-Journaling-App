from django.db import models

class Category(models.Model):
    """"""
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
