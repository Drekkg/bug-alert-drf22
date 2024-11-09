from rest_framework import serializers
from .models import Project



class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'owner', 'projectURL', 'created_on', 'image']