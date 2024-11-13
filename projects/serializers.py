from rest_framework import serializers
from .models import Project
from django.contrib.auth.models import User


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'projectURL',
                  'githubURL', 'created_on',  'owner']
