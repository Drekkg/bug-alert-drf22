from rest_framework import serializers
from .models import Comment
from django.contrib.auth.models import User


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = [
            'id',
            'comment',
            'resolved',
            'created_on',
            'owner',
            'comment-id',
        ]

        
