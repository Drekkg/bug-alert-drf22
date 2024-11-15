from django.urls import path
from comments import views


urlpatterns = [
    path('comments/', views.CommentList.as_view()),
    #     path('issues/', views.IssueList.as_view()),
]
