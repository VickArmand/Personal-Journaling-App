from rest_framework import serializers
from .models import Journal
class JournalSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Journal
        fields = ['id', 'title', 'content', 'category_id', 'user_id', 'created_at', 'updated_at']