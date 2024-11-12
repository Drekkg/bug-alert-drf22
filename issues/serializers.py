from rest_framework import serializers
from .models import Issue
from django.contrib.auth.models import User


class IssueSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Issue
        fields = [
            'id',
            'issue',
            # 'console_error',
            # 'owner',
            # 'repeatable',
            # 'created_on',
            # 'priority',
            # 'issue_project',
        ]
