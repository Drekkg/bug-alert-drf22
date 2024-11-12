from django.db import models
from django.contrib.auth.models import User
from projects.models import Project

from django.db.models.signals import post_save


PRIORITY_CHOICES = {
    ("low", "low"),
    ("medium", "medium"),
    ("high", "high"),
    ("critical", "critical"),
}


class Issue(models.Model):
    issue = models.CharField(max_length=200)
    console_error = models.TextField(max_length=300)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    repeatable = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, default="low")
    issue_project = models.ForeignKey(
        Project, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.owner.username}'s issues"
