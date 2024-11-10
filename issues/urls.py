from django.urls import path
from issues import views
# from .views import UserCreate


urlpatterns = [
    path('issues/<int:project_id', views.IssueList.as_view()),
    
]