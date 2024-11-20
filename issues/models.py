from django.db import models
from django.contrib.auth.models import User
from projects.models import Project

from django.db.models.signals import post_save


PRIORITY_CHOICES = {
    ("Low", "low"),
    ("Medium", "medium"),
    ("High", "high"),
    ("Critical", "critical"),
}


class Issue(models.Model):
    """
    Model representing the list of issues to track.
    Attributes:
        issue (str): A brief description of the issue.
        console_error (str): The console error message associated with the issue.
        owner (User): The user who reported the issue.
        repeatable (bool): Indicates whether the issue is repeatable. Defaults to False.
        created_on (datetime): The date and time when the issue was created. Automatically set on creation.
        priority (str): The priority level of the issue. Choices are defined in PRIORITY_CHOICES. Defaults to "low".
        issue_project_id (Project): The project associated with the issue. Can be null.
        resolved (bool): Indicates whether the issue has been resolved. Defaults to False.
    Meta:
        ordering (list): Orders the issues by creation date in descending order.
    Methods:
        __str__(): Returns a string representation of the issue, showing the owner's username and the word 'issues'.
    """

    issue = models.CharField(max_length=200)
    console_error = models.CharField(max_length=300)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    repeatable = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, default="low")
    issue_project_id = models.ForeignKey(
        Project, on_delete=models.CASCADE, null=True)
    resolved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.owner.username}'s issues"
