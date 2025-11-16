"""
URLs pour l'authentification.
"""
from django.urls import path
from .views.auth import SignUpView, ProfileView, ProfileUpdateView

urlpatterns = [
    path('', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
]
