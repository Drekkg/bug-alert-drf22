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
            'owner',
            'console_error',
            'repeatable',
            'created_on',
            'priority',
            'issue_project_id'

        ]
