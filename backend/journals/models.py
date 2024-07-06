from django.db import models
from backend.auth_users.models import CustomUser
from backend.categories.models import Category

class Journal(models.Model):
    """"""
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=2000)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
