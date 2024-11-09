from rest_framework import APIview
from rest_framework.response import Response
from .models import Project

# Create your views here.
class ProjectList(APIview):
    def get(self, request):
        projects = Project.objects.all()
        return Response(projects)
    