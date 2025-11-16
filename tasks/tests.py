"""
Tests pour l'application tasks.
"""
from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from .models import Task, Notification


class TaskModelTest(TestCase):
    """Tests pour le modèle Task."""
    
    def setUp(self):
        """Créer un utilisateur de test."""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
    
    def test_task_creation(self):
        """Tester la création d'une tâche."""
        task = Task.objects.create(
            user=self.user,
            title='Test Task',
            description='Test Description',
            due_date=timezone.now().date(),
            priority='high',
            category='Test',
            status='todo'
        )
        self.assertEqual(task.title, 'Test Task')
        self.assertEqual(task.priority, 'high')
        self.assertEqual(task.status, 'todo')
    
    def test_task_is_overdue(self):
        """Tester si une tâche est en retard."""
        past_date = timezone.now().date() - timedelta(days=1)
        task = Task.objects.create(
            user=self.user,
            title='Overdue Task',
            due_date=past_date,
            status='todo'
        )
        self.assertTrue(task.is_overdue())
    
    def test_task_is_due_today(self):
        """Tester si une tâche est due aujourd'hui."""
        today = timezone.now().date()
        task = Task.objects.create(
            user=self.user,
            title='Today Task',
            due_date=today,
            status='todo'
        )
        self.assertTrue(task.is_due_today())


class NotificationModelTest(TestCase):
    """Tests pour le modèle Notification."""
    
    def setUp(self):
        """Créer un utilisateur de test."""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
    
    def test_notification_creation(self):
        """Tester la création d'une notification."""
        notification = Notification.objects.create(
            user=self.user,
            message='Test notification'
        )
        self.assertEqual(notification.message, 'Test notification')
        self.assertFalse(notification.is_read)


class TaskViewsTest(TestCase):
    """Tests pour les vues de Task."""
    
    def setUp(self):
        """Créer un utilisateur et se connecter."""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')
    
    def test_dashboard_view(self):
        """Tester l'accès au tableau de bord."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Tableau de bord')
    
    def test_task_list_view(self):
        """Tester l'accès à la liste des tâches."""
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Mes tâches')
    
    def test_task_create_view(self):
        """Tester la création d'une tâche."""
        response = self.client.post('/tasks/new/', {
            'title': 'New Task',
            'description': 'Test description',
            'due_date': timezone.now().date(),
            'priority': 'medium',
            'category': 'Test',
            'status': 'todo'
        })
        self.assertEqual(response.status_code, 302)  # Redirection après succès
        self.assertTrue(Task.objects.filter(title='New Task').exists())
