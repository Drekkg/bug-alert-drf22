from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    projectURL = models.URLField(max_length=200, blank=True, null=True)
    githubURL = models.URLField(max_length=200, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.owner.username}'s projects"
