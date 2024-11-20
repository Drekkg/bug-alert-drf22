from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Issue
from .serializers import IssueSerializer


class IssueList(APIView):
    def get(self, request, project_id):
        issues = Issue.objects.all()
        serializer = IssueSerializer(issues, many=True)
        return Response(serializer.data)

    def post(self, request, project_id):
        data = request.data
        data['issue_project_id'] = project_id
        serializer = IssueSerializer(data=data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        issue = Issue.objects.get(pk=pk)
        serializer = IssueSerializer(issue, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
