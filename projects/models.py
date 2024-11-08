from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    projectURL = models.URLField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='projects/images/', blank=True, null=True)

    def __str__(self):
        return f"{self.owner}'s projects"
