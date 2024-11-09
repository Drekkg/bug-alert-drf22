from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    projectURL = models.URLField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='projects/images/', blank=True, null=True)

    def __str__(self):
        return f"{self.owner}'s projects"
   
# This signal will create a project for every new user that is created 
# post_save.connect(create_project, sender=User)  
# def create_project(sender, instance, created, **kwargs):
#     if created:
#         Project.objects.create(owner=instance)
