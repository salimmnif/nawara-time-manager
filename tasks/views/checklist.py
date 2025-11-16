from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from datetime import datetime

from ..models import Task


class ChecklistView(LoginRequiredMixin, TemplateView):
    """Vue de checklist avec des checkboxes pour marquer les tâches"""
    template_name = 'tasks/checklist.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        today = timezone.now().date()
        
        # Tâches du jour (toutes, pas seulement non terminées)
        context['today_tasks'] = Task.objects.filter(
            user=user,
            due_date=today
        ).order_by('status', 'priority')
        
        # Tâches en cours (toutes dates confondues)
        context['in_progress_tasks'] = Task.objects.filter(
            user=user,
            status='in_progress'
        ).exclude(due_date=today).order_by('due_date', 'priority')[:20]
        
        # Tâches à faire (toutes dates confondues)
        context['todo_tasks'] = Task.objects.filter(
            user=user,
            status='todo'
        ).exclude(due_date=today).order_by('due_date', 'priority')[:20]
        
        # Tâches terminées (les plus récentes)
        context['completed_tasks'] = Task.objects.filter(
            user=user,
            status='done'
        ).order_by('-updated_at')
        
        # Compteur total pour debug
        context['total_tasks'] = Task.objects.filter(user=user).count()
        
        return context
