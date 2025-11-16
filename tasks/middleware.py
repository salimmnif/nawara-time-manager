"""
Middleware pour connexion automatique d'un utilisateur unique.
"""
from django.contrib.auth import login
from django.contrib.auth.models import User


class AutoLoginMiddleware:
    """
    Connecte automatiquement l'utilisateur principal si non authentifié.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Si l'utilisateur n'est pas connecté et qu'on n'est pas sur la page admin
        if not request.user.is_authenticated and not request.path.startswith('/admin/'):
            # Chercher ou créer l'utilisateur principal
            user, created = User.objects.get_or_create(
                username='utilisateur',
                defaults={
                    'email': 'user@timemanager.com',
                    'first_name': 'Utilisateur',
                    'is_staff': False,
                    'is_superuser': False,
                }
            )
            
            # Si l'utilisateur a été créé, définir un mot de passe
            if created:
                user.set_password('timemanager2024')
                user.save()
            
            # Connecter automatiquement l'utilisateur
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        
        response = self.get_response(request)
        return response
