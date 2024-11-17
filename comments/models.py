from django.db import models
from django.contrib.auth.models import User
from issues.models import Issue
from projects.models import Project

from django.db.models.signals import post_save

# Create your models here.


class Comment(models.Model):
    """
    Model representing a comment on an issue.

    Attributes:
        comment (CharField): The text content of the comment.
        resolved (BooleanField): Indicates whether the comment has been resolved. Defaults to False.
        created_on (DateTimeField): The date and time when the comment was created. Automatically set on creation.
        owner (ForeignKey): The user who created the comment. References the User model.
        issue_id (ForeignKey): The issue to which the comment is related. References the Issue model. Can be null.

    Meta:
        ordering (list): Orders the comments by creation date in descending order.

    Methods:
        __str__(): Returns a string representation of the comment, including the owner's username.
    """
    comment = models.CharField(max_length=200)
    resolved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_id = models.ForeignKey(Issue, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.owner.username}'s comments"
