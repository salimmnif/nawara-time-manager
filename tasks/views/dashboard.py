"""
Vues pour le tableau de bord.
"""
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.db.models import Count, Q
from datetime import timedelta
from ..models import Task, Notification


class DashboardView(LoginRequiredMixin, TemplateView):
    """Vue du tableau de bord principal."""
    
    template_name = 'tasks/dashboard.html'
    
    def dispatch(self, request, *args, **kwargs):
        """Vérifie les notifications avant d'afficher le dashboard."""
        if request.user.is_authenticated:
            self.check_user_tasks_notifications(request.user)
        return super().dispatch(request, *args, **kwargs)
    
    def check_user_tasks_notifications(self, user):
        """Vérifie toutes les tâches de l'utilisateur et crée des notifications."""
        today = timezone.now().date()
        
        # Récupérer toutes les tâches non terminées
        active_tasks = Task.objects.filter(
            user=user,
            status__in=['todo', 'in_progress']
        )
        
        for task in active_tasks:
            # Tâche due aujourd'hui
            if task.due_date == today:
                existing = Notification.objects.filter(
                    user=user,
                    task=task,
                    message__contains='due aujourd\'hui',
                    created_at__date=today  # Créée aujourd'hui seulement
                ).exists()
                
                if not existing:
                    Notification.objects.create(
                        user=user,
                        task=task,
                        message=f'La tâche "{task.title}" est due aujourd\'hui !'
                    )
            
            # Tâche en retard
            elif task.due_date < today:
                existing = Notification.objects.filter(
                    user=user,
                    task=task,
                    message__contains='en retard',
                    created_at__date=today  # Créée aujourd'hui seulement
                ).exists()
                
                if not existing:
                    days_overdue = (today - task.due_date).days
                    Notification.objects.create(
                        user=user,
                        task=task,
                        message=f'La tâche "{task.title}" est en retard de {days_overdue} jour(s) !'
                    )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        today = timezone.now().date()
        
        # Récupérer toutes les tâches de l'utilisateur
        all_tasks = Task.objects.filter(user=user)
        
        # Tâches en retard (non terminées et date échue)
        overdue_tasks = all_tasks.filter(
            due_date__lt=today,
            status__in=['todo', 'in_progress']
        )
        
        # Tâches du jour
        today_tasks = all_tasks.filter(due_date=today)
        
        # Tâches complétées (total)
        completed_tasks = all_tasks.filter(status='done')
        
        # Répartition par statut
        status_counts = all_tasks.values('status').annotate(count=Count('id'))
        status_distribution = {
            'todo': 0,
            'in_progress': 0,
            'done': 0,
        }
        for item in status_counts:
            status_distribution[item['status']] = item['count']
        
        # Progression de la semaine (tâches de cette semaine)
        week_start = today - timedelta(days=today.weekday())
        week_end = week_start + timedelta(days=6)
        
        week_tasks = all_tasks.filter(
            due_date__gte=week_start,
            due_date__lte=week_end
        )
        week_completed = week_tasks.filter(status='done').count()
        week_total = week_tasks.count()
        week_progress_percentage = (week_completed / week_total * 100) if week_total > 0 else 0
        
        # Notifications non lues
        unread_notifications = Notification.objects.filter(
            user=user,
            is_read=False
        )[:5]  # Les 5 dernières
        
        # Tâches par priorité
        priority_counts = all_tasks.values('priority').annotate(count=Count('id'))
        priority_distribution = {
            'low': 0,
            'medium': 0,
            'high': 0,
        }
        for item in priority_counts:
            priority_distribution[item['priority']] = item['count']
        
        context.update({
            'overdue_count': overdue_tasks.count(),
            'today_count': today_tasks.count(),
            'completed_count': completed_tasks.count(),
            'total_count': all_tasks.count(),
            'status_distribution': status_distribution,
            'priority_distribution': priority_distribution,
            'week_tasks': week_tasks,
            'week_completed': week_completed,
            'week_total': week_total,
            'week_progress_percentage': round(week_progress_percentage, 1),
            'overdue_tasks': overdue_tasks[:5],  # Top 5 des tâches en retard
            'today_tasks': today_tasks[:5],  # Top 5 des tâches du jour
            'recent_completed': completed_tasks[:5],  # 5 dernières complétées
            'unread_notifications': unread_notifications,
        })
        
        return context


class NotificationListView(LoginRequiredMixin, TemplateView):
    """Vue pour afficher toutes les notifications."""
    
    template_name = 'tasks/notifications.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        notifications = Notification.objects.filter(user=self.request.user)
        context['notifications'] = notifications
        return context
