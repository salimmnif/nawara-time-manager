"""
Management command pour vérifier et créer des notifications automatiques.
Usage: python manage.py check_notifications
"""
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth.models import User
from tasks.models import Task, Notification


class Command(BaseCommand):
    help = 'Vérifie les tâches et crée des notifications pour les tâches dues ou en retard'

    def add_arguments(self, parser):
        parser.add_argument(
            '--user',
            type=str,
            help='Vérifier uniquement pour un utilisateur spécifique (username)',
        )

    def handle(self, *args, **options):
        today = timezone.now().date()
        username = options.get('user')
        
        # Filtrer les utilisateurs
        if username:
            users = User.objects.filter(username=username)
            if not users.exists():
                self.stdout.write(
                    self.style.ERROR(f'Utilisateur "{username}" non trouvé')
                )
                return
        else:
            users = User.objects.all()
        
        total_notifications = 0
        
        for user in users:
            user_notifications = 0
            
            # 1. Tâches dues aujourd'hui (non terminées)
            today_tasks = Task.objects.filter(
                user=user,
                due_date=today,
                status__in=['todo', 'in_progress']
            )
            
            for task in today_tasks:
                # Vérifier si une notification n'existe pas déjà
                existing = Notification.objects.filter(
                    user=user,
                    task=task,
                    message__contains='due aujourd\'hui'
                ).exists()
                
                if not existing:
                    Notification.objects.create(
                        user=user,
                        task=task,
                        message=f'La tâche "{task.title}" est due aujourd\'hui !'
                    )
                    user_notifications += 1
                    self.stdout.write(
                        self.style.SUCCESS(
                            f'✓ Notification créée pour {user.username}: tâche "{task.title}" due aujourd\'hui'
                        )
                    )
            
            # 2. Tâches en retard (date dépassée et non terminées)
            overdue_tasks = Task.objects.filter(
                user=user,
                due_date__lt=today,
                status__in=['todo', 'in_progress']
            )
            
            for task in overdue_tasks:
                # Vérifier si une notification n'existe pas déjà
                existing = Notification.objects.filter(
                    user=user,
                    task=task,
                    message__contains='en retard'
                ).exists()
                
                if not existing:
                    days_overdue = (today - task.due_date).days
                    Notification.objects.create(
                        user=user,
                        task=task,
                        message=f'La tâche "{task.title}" est en retard de {days_overdue} jour(s) !'
                    )
                    user_notifications += 1
                    self.stdout.write(
                        self.style.WARNING(
                            f'⚠ Notification créée pour {user.username}: tâche "{task.title}" en retard de {days_overdue} jour(s)'
                        )
                    )
            
            if user_notifications > 0:
                total_notifications += user_notifications
                self.stdout.write(
                    self.style.SUCCESS(
                        f'\n{user_notifications} notification(s) créée(s) pour {user.username}\n'
                    )
                )
        
        # Résumé final
        if total_notifications > 0:
            self.stdout.write(
                self.style.SUCCESS(
                    f'\n✓ Total: {total_notifications} notification(s) créée(s)'
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS('\nℹ Aucune nouvelle notification à créer')
            )
