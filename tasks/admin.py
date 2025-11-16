from django.contrib import admin
from .models import Task, Notification


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """Configuration de l'interface d'administration pour Task."""
    list_display = ['title', 'user', 'status', 'priority', 'due_date', 'created_at']
    list_filter = ['status', 'priority', 'category', 'created_at']
    search_fields = ['title', 'description', 'user__username']
    date_hierarchy = 'due_date'
    ordering = ['-created_at']
    
    fieldsets = (
        ('Informations principales', {
            'fields': ('user', 'title', 'description')
        }),
        ('Planification', {
            'fields': ('due_date', 'priority', 'category', 'status')
        }),
    )


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    """Configuration de l'interface d'administration pour Notification."""
    list_display = ['user', 'message', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['message', 'user__username']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
