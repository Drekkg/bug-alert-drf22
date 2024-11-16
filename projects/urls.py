from django.urls import path
from projects import views
# from .views import UserCreate


urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
     path('projects/<int:pk>/', views.ProjectList.as_view(), name='project-detail'),
    
]