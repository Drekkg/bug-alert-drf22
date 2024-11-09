from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project

# Create your views here.
class ProjectList(APIView):
    def get(self, request):
        projects = Project.objects.all()
        return Response(projects)
    