from rest_framework import serializers
from .models import Project
from django.contrib.auth.models import User


# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']

#     def create(self, validated_data):
#         user = User.objects.create_user(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             password=validated_data['password']
#         )
#         return user



class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'projectURL', 'created_on', 'image', 'owner']