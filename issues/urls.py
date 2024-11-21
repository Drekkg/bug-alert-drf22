from django.urls import path
from issues import views
# from .views import UserCreate

urlpatterns = [
    path('isssues/<int:pk>', views.IssueList.as_view()),
    path('issues/<int:pk>/',
         views.IssueList.as_view(), name='issue-list-by-project'),
    path('issues/', views.IssueList.as_view()),
]
