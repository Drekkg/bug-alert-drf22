"""
URL configuration for bug_alert_drf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from .views import root_route, logout_route


urlpatterns = [
    path('', root_route),
    path('admin/', admin.site.urls),
    path('dj-rest-auth/logout/', logout_route),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('', include('projects.urls')),
    path('', include('issues.urls')),
    path('', include('comments.urls')),



]


# Login: /api/auth/login/
# Logout: /api/auth/logout/
# Password Change: /api/auth/password/change/
# Password Reset: /api/auth/password/reset/
# Password Reset Confirm: /api/auth/password/reset/confirm/
# User Registration: /api/auth/registration/
# User Details: /api/auth/user/
