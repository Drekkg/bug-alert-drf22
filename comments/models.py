from django.db import models
from django.contrib.auth.models import User
from issues.models import Issue

# Create your models here.


class Comment(models.Model):
    comment = models.CharField(max_length=200)
    resolved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_id = models.ForeignKey(Issue, on_delete=models.CASCADE, null=True)


class Meta:
    ordering = ['-created_on']


def __str__(self):
    return f"{self.owner.username}'s comments"
