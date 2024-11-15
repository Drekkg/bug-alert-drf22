from django.urls import path
from comments import views


urlpatterns = [
    path('comments/<int:project_id>/', views.CommentList.as_view()),

]
