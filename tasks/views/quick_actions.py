"""
Vues pour les actions rapides sur les tâches.
"""
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from ..models import Task


class TaskMarkDoneView(LoginRequiredMixin, View):
    """Marque une tâche comme terminée rapidement."""
    
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task.status = 'done'
        task.save()
        messages.success(request, f'✓ Tâche "{task.title}" marquée comme terminée !')
        
        # Rediriger vers la page précédente ou le dashboard
        next_url = request.POST.get('next', request.META.get('HTTP_REFERER', 'dashboard'))
        return redirect(next_url)


class TaskMarkInProgressView(LoginRequiredMixin, View):
    """Marque une tâche comme en cours."""
    
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task.status = 'in_progress'
        task.save()
        messages.success(request, f'Tâche "{task.title}" marquée comme en cours.')
        
        next_url = request.POST.get('next', request.META.get('HTTP_REFERER', 'dashboard'))
        return redirect(next_url)


class TaskMarkTodoView(LoginRequiredMixin, View):
    """Marque une tâche comme à faire."""
    
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task.status = 'todo'
        task.save()
        messages.success(request, f'Tâche "{task.title}" marquée comme à faire.')
        
        next_url = request.POST.get('next', request.META.get('HTTP_REFERER', 'dashboard'))
        return redirect(next_url)


class TaskToggleStatusView(LoginRequiredMixin, View):
    """Change le statut de la tâche (todo → in_progress → done → todo)."""
    
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        
        # Cycle de statuts
        if task.status == 'todo':
            task.status = 'in_progress'
            messages.info(request, f'Tâche "{task.title}" en cours...')
        elif task.status == 'in_progress':
            task.status = 'done'
            messages.success(request, f'✓ Tâche "{task.title}" terminée !')
        else:  # done
            task.status = 'todo'
            messages.info(request, f'Tâche "{task.title}" réouverte.')
        
        task.save()
        
        next_url = request.POST.get('next', request.META.get('HTTP_REFERER', 'dashboard'))
        return redirect(next_url)
