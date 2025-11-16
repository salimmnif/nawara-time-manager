"""
URLs pour l'application tasks.
"""
from django.urls import path
from .views.tasks import (
    TaskListView, TaskDetailView, TaskCreateView, 
    TaskUpdateView, TaskDeleteView
)
from .views.dashboard import DashboardView, NotificationListView
from .views.calendar import CalendarView, DayView, WeekView
from .views.quick_actions import (
    TaskMarkDoneView, TaskMarkInProgressView, 
    TaskMarkTodoView, TaskToggleStatusView
)
from .views.checklist import ChecklistView

urlpatterns = [
    # Tableau de bord
    path('', DashboardView.as_view(), name='dashboard'),
    
    # Checklist (vue principale des tâches)
    path('checklist/', ChecklistView.as_view(), name='checklist'),
    
    # Gestion des tâches (CRUD)
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('tasks/new/', TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('tasks/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    
    # Actions rapides sur les tâches
    path('tasks/<int:pk>/mark-done/', TaskMarkDoneView.as_view(), name='task_mark_done'),
    path('tasks/<int:pk>/mark-progress/', TaskMarkInProgressView.as_view(), name='task_mark_progress'),
    path('tasks/<int:pk>/mark-todo/', TaskMarkTodoView.as_view(), name='task_mark_todo'),
    path('tasks/<int:pk>/toggle/', TaskToggleStatusView.as_view(), name='task_toggle_status'),
    
    # Calendrier et vues temporelles
    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('calendar/day/', DayView.as_view(), name='day_view'),
    path('calendar/week/', WeekView.as_view(), name='week_view'),
    
    # Notifications
    path('notifications/', NotificationListView.as_view(), name='notifications'),
]
