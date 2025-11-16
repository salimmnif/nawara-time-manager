# Structure du Projet Time Manager

```
time_manager/
│
├── manage.py                       # Script de gestion Django
├── requirements.txt                # Dépendances Python
├── README.md                       # Documentation principale
├── QUICKSTART.md                   # Guide de démarrage rapide
├── ARCHITECTURE.md                 # Documentation technique
├── .gitignore                      # Fichiers à ignorer par Git
├── db.sqlite3                      # Base de données (créée après migration)
│
├── time_manager/                   # Configuration du projet Django
│   ├── __init__.py
│   ├── settings.py                # Paramètres du projet
│   ├── urls.py                    # URLs principales du projet
│   ├── wsgi.py                    # Configuration WSGI (déploiement)
│   ├── asgi.py                    # Configuration ASGI (async)
│   │
│   └── templates/                 # Templates globaux
│       ├── base.html             # Template de base (navbar, footer)
│       │
│       └── registration/         # Templates d'authentification
│           ├── login.html
│           ├── signup.html
│           ├── profile.html
│           ├── profile_edit.html
│           ├── password_reset.html
│           ├── password_reset_done.html
│           ├── password_reset_confirm.html
│           └── password_reset_complete.html
│
└── tasks/                         # Application principale
    ├── __init__.py
    ├── apps.py                   # Configuration de l'app
    ├── models.py                 # Modèles (Task, Notification)
    ├── admin.py                  # Configuration de l'interface admin
    ├── forms.py                  # Formulaires Django
    ├── urls.py                   # URLs de l'application
    ├── urls_auth.py              # URLs d'authentification
    ├── tests.py                  # Tests unitaires
    │
    ├── views/                    # Vues organisées en modules
    │   ├── __init__.py
    │   ├── tasks.py             # CRUD des tâches
    │   ├── dashboard.py         # Tableau de bord
    │   ├── calendar.py          # Vues calendrier
    │   └── auth.py              # Authentification et profil
    │
    ├── templates/tasks/          # Templates de l'application
    │   ├── dashboard.html       # Tableau de bord principal
    │   ├── list.html            # Liste des tâches
    │   ├── detail.html          # Détails d'une tâche
    │   ├── form.html            # Formulaire création/édition
    │   ├── confirm_delete.html  # Confirmation de suppression
    │   ├── calendar.html        # Vue calendrier mensuel
    │   ├── day_view.html        # Vue journalière
    │   ├── week_view.html       # Vue hebdomadaire
    │   └── notifications.html   # Liste des notifications
    │
    ├── templatetags/             # Template tags personnalisés
    │   ├── __init__.py
    │   └── task_extras.py       # Filtres personnalisés (get_item, mul, div)
    │
    └── management/               # Commandes de gestion personnalisées
        ├── __init__.py
        └── commands/
            ├── __init__.py
            └── check_notifications.py  # Génération des notifications
```

## Détail des fichiers principaux

### Configuration (time_manager/)

**settings.py**
- Configuration générale du projet
- Base de données SQLite
- Applications installées
- Middleware
- Templates
- Internationalisation (fr-fr)
- Paramètres de sécurité

**urls.py**
- Route principale (/)
- Routes d'authentification
- Routes de l'application tasks
- Interface d'administration

### Application (tasks/)

**models.py**
- `Task` : Modèle principal des tâches
  - Champs : user, title, description, due_date, priority, category, status
  - Méthodes : is_overdue(), is_due_today(), badge helpers
- `Notification` : Modèle des notifications
  - Champs : user, message, created_at, is_read, task

**views/** (Class-Based Views)
- `tasks.py` : TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView
- `dashboard.py` : DashboardView, NotificationListView
- `calendar.py` : CalendarView, DayView, WeekView
- `auth.py` : SignUpView, ProfileView, ProfileUpdateView

**forms.py**
- `TaskForm` : Création/édition de tâches
- `TaskSearchForm` : Recherche
- `TaskFilterForm` : Filtrage
- `UserRegistrationForm` : Inscription
- `UserProfileForm` : Modification du profil

**admin.py**
- Configuration de l'interface d'administration
- TaskAdmin : Liste, filtres, recherche
- NotificationAdmin : Liste, filtres

### Templates

**Base (time_manager/templates/)**
- `base.html` : Template parent avec navbar Bootstrap 5

**Registration (time_manager/templates/registration/)**
- Templates d'authentification et profil
- Design Bootstrap 5 cohérent

**Tasks (tasks/templates/tasks/)**
- Templates de l'application
- Cards Bootstrap pour le design
- Responsive et accessible

### Commandes (tasks/management/commands/)

**check_notifications.py**
- Génère les notifications automatiques
- Tâches dues aujourd'hui
- Tâches en retard
- Options : --user pour cibler un utilisateur

## Fichiers créés après migration

```
time_manager/
├── db.sqlite3                     # Base de données SQLite
├── staticfiles/                   # Fichiers statiques collectés (production)
└── venv/                          # Environnement virtuel Python (si créé)
```

## Flux de données

```
User Request
    ↓
urls.py (routing)
    ↓
views.py (logique)
    ↓
models.py (données) ←→ db.sqlite3
    ↓
forms.py (validation)
    ↓
templates/ (affichage)
    ↓
HTML Response
```

## Nombre de fichiers

- **Fichiers Python** : ~20
- **Templates HTML** : ~20
- **Fichiers de configuration** : 5
- **Documentation** : 4
- **Total** : ~50 fichiers

## Poids approximatif

- Code Python : ~200 Ko
- Templates HTML : ~100 Ko
- Documentation : ~50 Ko
- **Total** : ~350 Ko (sans environnement virtuel)

---

**Structure propre, organisée et maintenable ! 🎯**
