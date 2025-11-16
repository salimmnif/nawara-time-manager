"""
Vues pour l'authentification et la gestion du profil.
"""
from django.views.generic import CreateView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from ..forms import UserRegistrationForm, UserProfileForm


class SignUpView(CreateView):
    """Vue pour l'inscription d'un nouvel utilisateur."""
    
    form_class = UserRegistrationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    
    def dispatch(self, request, *args, **kwargs):
        """Redirige les utilisateurs déjà connectés."""
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        messages.success(
            self.request,
            'Compte créé avec succès ! Vous pouvez maintenant vous connecter.'
        )
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, TemplateView):
    """Vue pour afficher le profil de l'utilisateur."""
    
    template_name = 'registration/profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        # Statistiques utilisateur
        from ..models import Task
        total_tasks = Task.objects.filter(user=user).count()
        completed_tasks = Task.objects.filter(user=user, status='done').count()
        
        context.update({
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
        })
        
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """Vue pour modifier le profil de l'utilisateur."""
    
    model = User
    form_class = UserProfileForm
    template_name = 'registration/profile_edit.html'
    success_url = reverse_lazy('profile')
    
    def get_object(self, queryset=None):
        """Retourne l'utilisateur connecté."""
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, 'Profil mis à jour avec succès !')
        return super().form_valid(form)
