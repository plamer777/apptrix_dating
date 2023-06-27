"""This file contains urls for participant app"""
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)
from participant import views
# -------------------------------------------------------------------------

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('create/', views.CreateClientView.as_view()),
]
