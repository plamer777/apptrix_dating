"""This file contains urls for participant app"""
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)
from participant import views
# -------------------------------------------------------------------------

urlpatterns = [
    path('clients/login/', TokenObtainPairView.as_view()),
    path('clients/token/refresh/', TokenRefreshView.as_view()),
    path('clients/create/', views.CreateClientView.as_view()),
    path('clients/<int:favorite_id>/match/', views.UpdateClientView.as_view()),
    path('list/', views.ClientListView.as_view()),
]
