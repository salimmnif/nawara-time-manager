"""
URL configuration for time_manager project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # URLs de l'application tasks
    path('', include('tasks.urls')),
]
