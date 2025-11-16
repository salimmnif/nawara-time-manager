"""
Modèles pour l'application de gestion des tâches.
"""
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Task(models.Model):
    """
    Modèle représentant une tâche.
    Chaque tâche appartient à un utilisateur unique.
    """
    
    PRIORITY_CHOICES = [
        ('low', 'Faible'),
        ('medium', 'Moyenne'),
        ('high', 'Haute'),
    ]
    
    STATUS_CHOICES = [
        ('todo', 'À faire'),
        ('in_progress', 'En cours'),
        ('done', 'Terminée'),
    ]
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name='Utilisateur'
    )
    title = models.CharField(
        max_length=200,
        verbose_name='Titre'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Description'
    )
    due_date = models.DateField(
        verbose_name='Date d\'échéance'
    )
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='medium',
        verbose_name='Priorité'
    )
    category = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Catégorie'
    )
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='todo',
        verbose_name='Statut'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date de création'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Date de modification'
    )
    
    class Meta:
        ordering = ['-due_date', '-priority']
        verbose_name = 'Tâche'
        verbose_name_plural = 'Tâches'
    
    def __str__(self):
        return self.title
    
    def is_overdue(self):
        """Vérifie si la tâche est en retard."""
        if self.status != 'done' and self.due_date < timezone.now().date():
            return True
        return False
    
    def is_due_today(self):
        """Vérifie si la tâche est due aujourd'hui."""
        return self.due_date == timezone.now().date()
    
    def get_priority_badge_class(self):
        """Retourne la classe CSS Bootstrap pour la priorité."""
        priority_classes = {
            'low': 'bg-success',
            'medium': 'bg-warning',
            'high': 'bg-danger',
        }
        return priority_classes.get(self.priority, 'bg-secondary')
    
    def get_status_badge_class(self):
        """Retourne la classe CSS Bootstrap pour le statut."""
        status_classes = {
            'todo': 'bg-secondary',
            'in_progress': 'bg-primary',
            'done': 'bg-success',
        }
        return status_classes.get(self.status, 'bg-secondary')
    
    def check_and_create_notification(self):
        """Vérifie si une notification doit être créée pour cette tâche."""
        today = timezone.now().date()
        
        # Si la tâche n'est pas terminée
        if self.status != 'done':
            # Tâche due aujourd'hui
            if self.due_date == today:
                # Vérifier si la notification existe déjà
                existing = Notification.objects.filter(
                    user=self.user,
                    task=self,
                    message__contains='due aujourd\'hui'
                ).exists()
                
                if not existing:
                    Notification.objects.create(
                        user=self.user,
                        task=self,
                        message=f'La tâche "{self.title}" est due aujourd\'hui !'
                    )
            
            # Tâche en retard
            elif self.due_date < today:
                # Vérifier si la notification existe déjà
                existing = Notification.objects.filter(
                    user=self.user,
                    task=self,
                    message__contains='en retard'
                ).exists()
                
                if not existing:
                    days_overdue = (today - self.due_date).days
                    Notification.objects.create(
                        user=self.user,
                        task=self,
                        message=f'La tâche "{self.title}" est en retard de {days_overdue} jour(s) !'
                    )
    
    def save(self, *args, **kwargs):
        """Override save pour vérifier les notifications à chaque sauvegarde."""
        super().save(*args, **kwargs)
        # Vérifier et créer une notification si nécessaire
        self.check_and_create_notification()


class Notification(models.Model):
    """
    Modèle représentant une notification pour un utilisateur.
    """
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notifications',
        verbose_name='Utilisateur'
    )
    message = models.TextField(
        verbose_name='Message'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date de création'
    )
    is_read = models.BooleanField(
        default=False,
        verbose_name='Lu'
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='notifications',
        verbose_name='Tâche associée'
    )
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
    
    def __str__(self):
        return f"Notification pour {self.user.username}: {self.message[:50]}"
