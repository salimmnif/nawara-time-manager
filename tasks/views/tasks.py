"""
Vues pour la gestion des tâches (CRUD + liste).
"""
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import Q
from ..models import Task
from ..forms import TaskForm, TaskSearchForm, TaskFilterForm


class TaskListView(LoginRequiredMixin, ListView):
    """Vue pour lister les tâches de l'utilisateur."""
    
    model = Task
    template_name = 'tasks/list.html'
    context_object_name = 'tasks'
    paginate_by = 10
    
    def get_queryset(self):
        """Retourne uniquement les tâches de l'utilisateur connecté."""
        queryset = Task.objects.filter(user=self.request.user)
        
        # Recherche par titre
        search_query = self.request.GET.get('search_query', '')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | 
                Q(description__icontains=search_query)
            )
        
        # Filtrage par statut
        status = self.request.GET.get('status', '')
        if status:
            queryset = queryset.filter(status=status)
        
        # Filtrage par priorité
        priority = self.request.GET.get('priority', '')
        if priority:
            queryset = queryset.filter(priority=priority)
        
        # Filtrage par catégorie
        category = self.request.GET.get('category', '')
        if category:
            queryset = queryset.filter(category__icontains=category)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        """Ajoute les formulaires de recherche et filtrage au contexte."""
        context = super().get_context_data(**kwargs)
        context['search_form'] = TaskSearchForm(self.request.GET)
        context['filter_form'] = TaskFilterForm(self.request.GET)
        return context


class TaskDetailView(LoginRequiredMixin, DetailView):
    """Vue pour afficher les détails d'une tâche."""
    
    model = Task
    template_name = 'tasks/detail.html'
    context_object_name = 'task'
    
    def get_queryset(self):
        """S'assure que l'utilisateur ne peut voir que ses propres tâches."""
        return Task.objects.filter(user=self.request.user)


class TaskCreateView(LoginRequiredMixin, CreateView):
    """Vue pour créer une nouvelle tâche."""
    
    model = Task
    form_class = TaskForm
    template_name = 'tasks/form.html'
    success_url = reverse_lazy('task_list')
    
    def form_valid(self, form):
        """Associe la tâche à l'utilisateur connecté."""
        form.instance.user = self.request.user
        messages.success(self.request, 'Tâche créée avec succès !')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Créer une tâche'
        context['button_text'] = 'Créer'
        return context


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    """Vue pour modifier une tâche existante."""
    
    model = Task
    form_class = TaskForm
    template_name = 'tasks/form.html'
    success_url = reverse_lazy('task_list')
    
    def get_queryset(self):
        """S'assure que l'utilisateur ne peut modifier que ses propres tâches."""
        return Task.objects.filter(user=self.request.user)
    
    def form_valid(self, form):
        messages.success(self.request, 'Tâche modifiée avec succès !')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Modifier la tâche'
        context['button_text'] = 'Mettre à jour'
        return context


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    """Vue pour supprimer une tâche."""
    
    model = Task
    template_name = 'tasks/confirm_delete.html'
    success_url = reverse_lazy('task_list')
    context_object_name = 'task'
    
    def get_queryset(self):
        """S'assure que l'utilisateur ne peut supprimer que ses propres tâches."""
        return Task.objects.filter(user=self.request.user)
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Tâche supprimée avec succès !')
        return super().delete(request, *args, **kwargs)
