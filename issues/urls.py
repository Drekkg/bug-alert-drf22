from django.urls import path
from issues import views
# from .views import UserCreate

urlpatterns = [
    path('issues/', views.IssueList.as_view(), name='issue-list-by-project'),
]