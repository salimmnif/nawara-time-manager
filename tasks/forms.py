"""
Formulaires pour l'application de gestion des tâches.
"""
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Task, Notification


class TaskForm(forms.ModelForm):
    """Formulaire pour créer et modifier une tâche."""
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'category', 'status']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Titre de la tâche'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Description détaillée (optionnel)'
            }),
            'due_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'priority': forms.Select(attrs={
                'class': 'form-select'
            }),
            'category': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Travail, Personnel, Études...'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
        }
        labels = {
            'title': 'Titre',
            'description': 'Description',
            'due_date': 'Date d\'échéance',
            'priority': 'Priorité',
            'category': 'Catégorie',
            'status': 'Statut',
        }


class TaskSearchForm(forms.Form):
    """Formulaire de recherche de tâches."""
    
    search_query = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Rechercher une tâche...'
        }),
        label='Recherche'
    )


class TaskFilterForm(forms.Form):
    """Formulaire de filtrage des tâches."""
    
    status = forms.ChoiceField(
        required=False,
        choices=[('', 'Tous les statuts')] + Task.STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Statut'
    )
    
    priority = forms.ChoiceField(
        required=False,
        choices=[('', 'Toutes les priorités')] + Task.PRIORITY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Priorité'
    )
    
    category = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Filtrer par catégorie'
        }),
        label='Catégorie'
    )


class UserRegistrationForm(UserCreationForm):
    """Formulaire d'inscription d'un nouvel utilisateur."""
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        })
    )
    
    first_name = forms.CharField(
        required=False,
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Prénom (optionnel)'
        })
    )
    
    last_name = forms.CharField(
        required=False,
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nom (optionnel)'
        })
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nom d\'utilisateur'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Mot de passe'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirmation du mot de passe'
        })


class UserProfileForm(forms.ModelForm):
    """Formulaire pour modifier le profil utilisateur."""
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Prénom'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
        }
        labels = {
            'first_name': 'Prénom',
            'last_name': 'Nom',
            'email': 'Email',
        }
