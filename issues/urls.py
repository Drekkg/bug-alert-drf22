from django.urls import path
from issues import views
# from .views import UserCreate

urlpatterns = [
    path('issues/<int:pk>/', views.IssueDetail.as_view(), name='issue-detail'),
    path('issues/<int:project_id>/',
         views.IssueList.as_view(), name='issue-list-by-project'),
    path('issues/', views.IssueList.as_view()),
]
