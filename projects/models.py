from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Project(models.Model):
    """
    Project model representing a project created by a user.

    Attributes:
        title (CharField): The title of the project, with a maximum
        length of 100 characters.
        description (TextField): A brief description of the project,
        with a maximum length of 200 characters.
        owner (ForeignKey): A reference to the User who owns the project. 
        If the user is deleted, the project is also deleted.
        projectURL (URLField): An optional URL field for the project's URL, 
        with a maximum length of 200 characters.
        githubURL (URLField): An optional URL field for the project's 
        GitHub URL, with a maximum length of 200 characters.
        created_on (DateTimeField): The date and time when the project was 
        created, automatically set on creation.

    Meta:
        ordering (list): Orders the projects by creation date in descending
        order.

    Methods:
        __str__(): Returns a string representation of the project, showing
        the owner's username and the word 'projects'.
    """
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