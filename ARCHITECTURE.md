# Architecture et Documentation Technique - Time Manager

## Vue d'ensemble

Time Manager est une application Django full-stack utilisant le pattern MVT (Model-View-Template).

## Architecture des modèles

### Task (Tâche)
```python
- user: ForeignKey(User) - Propriétaire de la tâche
- title: CharField - Titre de la tâche
- description: TextField - Description détaillée
- due_date: DateField - Date d'échéance
- priority: CharField - Priorité (low, medium, high)
- category: CharField - Catégorie libre
- status: CharField - Statut (todo, in_progress, done)
- created_at: DateTimeField - Date de création
- updated_at: DateTimeField - Date de modification
```

Méthodes :
- `is_overdue()` : Vérifie si la tâche est en retard
- `is_due_today()` : Vérifie si la tâche est due aujourd'hui
- `get_priority_badge_class()` : Retourne la classe CSS pour la priorité
- `get_status_badge_class()` : Retourne la classe CSS pour le statut

### Notification
```python
- user: ForeignKey(User) - Destinataire
- message: TextField - Contenu de la notification
- created_at: DateTimeField - Date de création
- is_read: BooleanField - Statut de lecture
- task: ForeignKey(Task, optional) - Tâche associée
```

## Architecture des vues

### Structure organisée en modules

```
tasks/views/
├── __init__.py
├── tasks.py       # CRUD des tâches
├── dashboard.py   # Tableau de bord et notifications
├── calendar.py    # Vues calendrier (mensuel, hebdo, jour)
└── auth.py        # Authentification et profil
```

### Vues principales

#### tasks.py
- `TaskListView` : Liste paginée avec recherche et filtres
- `TaskDetailView` : Détails d'une tâche
- `TaskCreateView` : Création d'une tâche
- `TaskUpdateView` : Modification d'une tâche
- `TaskDeleteView` : Suppression avec confirmation

#### dashboard.py
- `DashboardView` : Tableau de bord avec statistiques
- `NotificationListView` : Liste des notifications

#### calendar.py
- `CalendarView` : Vue mensuelle du calendrier
- `DayView` : Tâches d'un jour spécifique
- `WeekView` : Vue hebdomadaire

#### auth.py
- `SignUpView` : Inscription
- `ProfileView` : Affichage du profil
- `ProfileUpdateView` : Modification du profil

## Formulaires

### TaskForm
Formulaire principal pour la création et modification de tâches.
- Widgets Bootstrap 5 personnalisés
- Validation Django native

### TaskSearchForm
Recherche par mot-clé dans titre et description.

### TaskFilterForm
Filtrage par :
- Statut
- Priorité
- Catégorie

### UserRegistrationForm
Inscription avec :
- Username, email, prénom, nom
- Validation de mot de passe Django

### UserProfileForm
Modification du profil (email, prénom, nom).

## URLs

### Principales routes

```
/                           → Dashboard
/tasks/                     → Liste des tâches
/tasks/new/                 → Créer une tâche
/tasks/<id>/                → Détails d'une tâche
/tasks/<id>/edit/           → Modifier une tâche
/tasks/<id>/delete/         → Supprimer une tâche

/calendar/                  → Calendrier mensuel
/calendar/day/              → Vue journalière
/calendar/week/             → Vue hebdomadaire

/notifications/             → Liste des notifications

/login/                     → Connexion
/logout/                    → Déconnexion
/signup/                    → Inscription
/signup/profile/            → Profil
/signup/profile/edit/       → Modifier le profil

/password-reset/            → Réinitialisation de mot de passe
/admin/                     → Interface d'administration
```

## Sécurité

### Protection des vues
- `LoginRequiredMixin` : Toutes les vues nécessitent une authentification
- Filtrage par utilisateur : Chaque utilisateur ne voit que ses données
- CSRF protection : Activé sur tous les formulaires
- Password validation : Validation Django native

### Bonnes pratiques appliquées
- Pas d'exposition des données d'autres utilisateurs
- Validation côté serveur
- Messages d'erreur génériques
- Tokens CSRF sur tous les formulaires POST

## Templates

### Hiérarchie
```
time_manager/templates/
└── base.html                      # Template de base

time_manager/templates/registration/
├── login.html
├── signup.html
├── profile.html
├── profile_edit.html
└── password_reset_*.html

tasks/templates/tasks/
├── dashboard.html
├── list.html
├── detail.html
├── form.html
├── confirm_delete.html
├── calendar.html
├── day_view.html
├── week_view.html
└── notifications.html
```

### Template tags personnalisés

Fichier : `tasks/templatetags/task_extras.py`

- `get_item` : Accès aux dictionnaires avec clé variable
- `mul` : Multiplication dans les templates
- `div` : Division dans les templates

Usage :
```django
{% load task_extras %}
{{ dictionary|get_item:key }}
{{ value|mul:100|div:total }}
```

## Management Commands

### check_notifications

Commande pour générer les notifications automatiques.

```powershell
# Toutes les notifications
python manage.py check_notifications

# Pour un utilisateur spécifique
python manage.py check_notifications --user username
```

Logique :
1. Tâches dues aujourd'hui → Notification si non terminée
2. Tâches en retard → Notification avec nombre de jours

## Base de données

### SQLite (Développement)
- Fichier : `db.sqlite3`
- Léger et simple
- Parfait pour le développement

### Migration vers production
Pour PostgreSQL/MySQL :
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'timemanager_db',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## Frontend

### Technologies
- **Bootstrap 5** : Framework CSS
- **Bootstrap Icons** : Icônes
- **CSS personnalisé** : Dans base.html

### Design patterns
- Cards pour les conteneurs
- Badges pour les statuts et priorités
- Progress bars pour les statistiques
- Responsive design (Mobile-first)

## Tests

### Structure des tests
Fichier : `tasks/tests.py`

- Tests unitaires des modèles
- Tests des méthodes métier
- Tests des vues (authentification, CRUD)
- Tests des permissions

Exécution :
```powershell
python manage.py test
```

## Performance

### Optimisations appliquées
- Pagination (10 items par page)
- Indexation automatique (ForeignKey, DateField)
- Requêtes filtrées par utilisateur
- select_related pour éviter les N+1 queries

### Améliorations possibles
- Cache Redis pour les statistiques
- Celery pour les notifications asynchrones
- Compression des assets statiques
- CDN pour Bootstrap

## Déploiement

### Checklist pour la production

1. **Settings**
   - `DEBUG = False`
   - `SECRET_KEY` sécurisée
   - `ALLOWED_HOSTS` configuré

2. **Base de données**
   - PostgreSQL ou MySQL
   - Backups automatiques

3. **Serveur web**
   - Nginx + Gunicorn
   - HTTPS avec Let's Encrypt

4. **Fichiers statiques**
   - `python manage.py collectstatic`
   - Servir via Nginx ou CDN

5. **Email**
   - SMTP configuré
   - SendGrid, Mailgun, ou autre

6. **Monitoring**
   - Sentry pour les erreurs
   - Logs centralisés

## Évolutions futures possibles

### Fonctionnalités
- [ ] Tags multiples par tâche
- [ ] Sous-tâches (checklist)
- [ ] Pièces jointes
- [ ] Partage de tâches entre utilisateurs
- [ ] Export PDF/CSV
- [ ] API REST (DRF)
- [ ] Application mobile
- [ ] Rappels par email
- [ ] Intégration calendrier (Google, Outlook)
- [ ] Mode dark/light

### Technique
- [ ] Cache Redis
- [ ] Celery pour tâches asynchrones
- [ ] WebSockets pour notifications en temps réel
- [ ] ElasticSearch pour recherche avancée
- [ ] Docker pour déploiement
- [ ] CI/CD (GitHub Actions)
- [ ] Tests E2E (Selenium)

## Contribution

### Standards de code
- PEP 8 pour Python
- Docstrings sur toutes les fonctions/classes
- Type hints quand pertinent
- Tests unitaires pour nouvelle fonctionnalité

### Git workflow
```bash
# Créer une branche
git checkout -b feature/nouvelle-fonctionnalite

# Développer et commiter
git add .
git commit -m "feat: ajout de..."

# Push et Pull Request
git push origin feature/nouvelle-fonctionnalite
```

## Documentation

- **README.md** : Guide complet
- **QUICKSTART.md** : Démarrage rapide
- **ARCHITECTURE.md** : Ce fichier
- **Docstrings** : Dans le code

## Support et ressources

- Documentation Django : https://docs.djangoproject.com/
- Bootstrap 5 : https://getbootstrap.com/
- Django Best Practices : https://django-best-practices.readthedocs.io/

---

**Développé avec ❤️ et Django**
