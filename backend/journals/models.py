from django.db import models
from django.contrib.auth.models import User
from backend.categories.models import Category

class Journal(models.Model):
    """"""
    id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=2000)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
