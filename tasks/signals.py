"""
Signaux Django pour la vérification automatique des tâches.
"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from .models import Task, Notification


def send_notification_email(user, task, message):
    """Envoie un email de notification à l'utilisateur."""
    try:
        subject = f'Time Manager - Notification: {task.title}'
        html_message = f"""
        <html>
            <body style="font-family: Arial, sans-serif; padding: 20px; background-color: #fafafa;">
                <div style="max-width: 600px; margin: 0 auto; background-color: white; padding: 30px; border-radius: 8px; border: 2px solid #f06292;">
                    <h2 style="color: #f06292; margin-bottom: 20px;">
                        📌 Notification de tâche
                    </h2>
                    <div style="background-color: #fce4ec; padding: 15px; border-radius: 6px; margin-bottom: 20px;">
                        <p style="margin: 0; color: #ec407a; font-size: 16px; font-weight: 500;">
                            {message}
                        </p>
                    </div>
                    <div style="margin-bottom: 15px;">
                        <strong style="color: #333;">Tâche:</strong> {task.title}
                    </div>
                    <div style="margin-bottom: 15px;">
                        <strong style="color: #333;">Date d'échéance:</strong> {task.due_date.strftime('%d/%m/%Y')}
                    </div>
                    <div style="margin-bottom: 15px;">
                        <strong style="color: #333;">Priorité:</strong> 
                        <span style="background-color: #f06292; color: white; padding: 3px 10px; border-radius: 4px; font-size: 12px;">
                            {task.get_priority_display()}
                        </span>
                    </div>
                    {f'<div style="margin-bottom: 15px;"><strong style="color: #333;">Description:</strong><br>{task.description}</div>' if task.description else ''}
                    <div style="margin-top: 30px; padding-top: 20px; border-top: 1px solid #f0f0f0; text-align: center;">
                        <a href="http://127.0.0.1:8000/tasks/{task.pk}/" 
                           style="background-color: #f06292; color: white; padding: 12px 30px; text-decoration: none; border-radius: 6px; font-weight: 500; display: inline-block;">
                            Voir la tâche
                        </a>
                    </div>
                    <div style="margin-top: 20px; text-align: center; color: #757575; font-size: 12px;">
                        <p>Time Manager - Gestion de vos tâches 💕</p>
                    </div>
                </div>
            </body>
        </html>
        """
        
        plain_message = f"""
        {message}
        
        Tâche: {task.title}
        Date d'échéance: {task.due_date.strftime('%d/%m/%Y')}
        Priorité: {task.get_priority_display()}
        {'Description: ' + task.description if task.description else ''}
        
        Voir la tâche: http://127.0.0.1:8000/tasks/{task.pk}/
        
        ---
        Time Manager
        """
        
        send_mail(
            subject=subject,
            message=plain_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            html_message=html_message,
            fail_silently=True,  # Continue même si l'email échoue
        )
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email: {e}")


@receiver(post_save, sender=Task)
def check_task_notification(sender, instance, created, **kwargs):
    """
    Signal déclenché après chaque sauvegarde de tâche.
    Vérifie si une notification doit être créée et envoie un email.
    """
    today = timezone.now().date()
    task = instance
    
    # Ne vérifier que si la tâche n'est pas terminée
    if task.status != 'done':
        # Tâche due aujourd'hui
        if task.due_date == today:
            existing = Notification.objects.filter(
                user=task.user,
                task=task,
                message__contains='due aujourd\'hui',
                created_at__date=today
            ).exists()
            
            if not existing:
                message = f'La tâche "{task.title}" est due aujourd\'hui !'
                Notification.objects.create(
                    user=task.user,
                    task=task,
                    message=message
                )
                # Envoyer l'email
                if task.user.email:
                    send_notification_email(task.user, task, message)
        
        # Tâche en retard
        elif task.due_date < today:
            existing = Notification.objects.filter(
                user=task.user,
                task=task,
                message__contains='en retard',
                created_at__date=today
            ).exists()
            
            if not existing:
                days_overdue = (today - task.due_date).days
                message = f'La tâche "{task.title}" est en retard de {days_overdue} jour(s) !'
                Notification.objects.create(
                    user=task.user,
                    task=task,
                    message=message
                )
                # Envoyer l'email
                if task.user.email:
                    send_notification_email(task.user, task, message)
    else:
        # Si la tâche est terminée, supprimer les notifications associées
        Notification.objects.filter(
            user=task.user,
            task=task,
            is_read=False
        ).delete()
