from django.urls import path
from issues import views
# from .views import UserCreate

urlpatterns = [
    path('issues/project/<int:project_id>/',
         views.IssueList.as_view(), name='issue-list-by-project'),
    path('issues/<int:pk>', views.IssueList.as_view()),
]
