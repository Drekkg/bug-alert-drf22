from django.urls import path
from projects import views
# from .views import UserCreate


urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    # path('register/', UserCreate.as_view(), name='user-create'),
]