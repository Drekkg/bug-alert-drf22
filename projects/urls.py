from django.urls import path
from projects import views
# from .views import UserCreate


urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    
]