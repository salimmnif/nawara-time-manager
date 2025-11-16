# Time Manager - Plateforme de Gestion du Temps

Une application web Django complète pour la gestion du temps et l'organisation des tâches.

## 📋 Fonctionnalités

- **Authentification complète** : Inscription, connexion, déconnexion, réinitialisation de mot de passe
- **Gestion des tâches** : CRUD complet avec recherche et filtrage
- **Tableau de bord** : Statistiques, progression, aperçu des tâches
- **Calendrier** : Vues mensuelle, hebdomadaire et journalière
- **Notifications** : Alertes automatiques pour les tâches dues ou en retard
- **Profil utilisateur** : Gestion des informations personnelles

## 🚀 Technologies utilisées

- **Framework** : Django 5.0+
- **Base de données** : SQLite
- **Frontend** : Bootstrap 5, Bootstrap Icons
- **Python** : 3.8+

## 📦 Installation

### Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Cloner ou télécharger le projet**
   ```powershell
   cd C:\Users\ASUS\Desktop\time_manager
   ```

2. **Créer un environnement virtuel (recommandé)**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Installer les dépendances**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Effectuer les migrations de base de données**
   ```powershell
   python manage.py migrate
   ```

5. **Créer un superutilisateur (administrateur)**
   ```powershell
   python manage.py createsuperuser
   ```
   Suivez les instructions pour créer votre compte administrateur.

6. **Lancer le serveur de développement**
   ```powershell
   python manage.py runserver
   ```

7. **Accéder à l'application**
   - Application : http://127.0.0.1:8000/
   - Interface d'administration : http://127.0.0.1:8000/admin/

## 📁 Structure du projet

```
time_manager/
├── time_manager/              # Configuration du projet
│   ├── settings.py           # Paramètres Django
│   ├── urls.py               # URLs principales
│   ├── wsgi.py               # Configuration WSGI
│   ├── asgi.py               # Configuration ASGI
│   └── templates/            # Templates globaux
│       └── base.html         # Template de base
│
├── tasks/                    # Application principale
│   ├── models.py            # Modèles (Task, Notification)
│   ├── forms.py             # Formulaires Django
│   ├── admin.py             # Configuration admin
│   ├── urls.py              # URLs de l'app
│   ├── urls_auth.py         # URLs d'authentification
│   │
│   ├── views/               # Vues organisées
│   │   ├── tasks.py        # CRUD des tâches
│   │   ├── dashboard.py    # Tableau de bord
│   │   ├── calendar.py     # Vues calendrier
│   │   └── auth.py         # Authentification
│   │
│   ├── templates/tasks/     # Templates de l'app
│   │   ├── dashboard.html
│   │   ├── list.html
│   │   ├── detail.html
│   │   ├── form.html
│   │   ├── calendar.html
│   │   ├── day_view.html
│   │   ├── week_view.html
│   │   └── notifications.html
│   │
│   └── management/          # Commandes personnalisées
│       └── commands/
│           └── check_notifications.py
│
├── manage.py                # Script de gestion Django
├── requirements.txt         # Dépendances Python
├── README.md               # Ce fichier
└── .gitignore              # Fichiers à ignorer par Git
```

## 🎯 Utilisation

### Créer une tâche

1. Connectez-vous à votre compte
2. Cliquez sur "Nouvelle tâche" dans la navbar
3. Remplissez les informations :
   - Titre (obligatoire)
   - Description (optionnel)
   - Date d'échéance (obligatoire)
   - Priorité : Faible, Moyenne, Haute
   - Catégorie (optionnel)
   - Statut : À faire, En cours, Terminée
4. Cliquez sur "Créer"

### Filtrer les tâches

Sur la page "Mes tâches", utilisez les filtres disponibles :
- Recherche par titre ou description
- Filtrage par statut
- Filtrage par priorité
- Filtrage par catégorie

### Vues calendrier

- **Vue mensuelle** : Aperçu des tâches du mois
- **Vue hebdomadaire** : Détail des tâches de la semaine
- **Vue journalière** : Toutes les tâches d'un jour spécifique

### Notifications automatiques

Exécutez la commande suivante pour générer les notifications :

```powershell
python manage.py check_notifications
```

Cette commande crée automatiquement des notifications pour :
- Les tâches dues aujourd'hui
- Les tâches en retard

**Conseil** : Configurez cette commande en tâche planifiée (cron/Task Scheduler) pour l'exécuter quotidiennement.

### Interface d'administration

Accédez à l'interface d'administration Django :
- URL : http://127.0.0.1:8000/admin/
- Utilisez les identifiants du superutilisateur créé

Depuis l'admin, vous pouvez :
- Gérer tous les utilisateurs
- Voir toutes les tâches
- Gérer les notifications
- Effectuer des opérations en masse

## 🔧 Configuration avancée

### Modifier la clé secrète (PRODUCTION)

Dans `time_manager/settings.py`, changez la valeur de `SECRET_KEY` :

```python
SECRET_KEY = 'votre-nouvelle-clé-secrète-aléatoire'
```

### Configurer l'envoi d'emails

Pour utiliser un vrai serveur email en production, modifiez dans `settings.py` :

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.votre-serveur.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'votre-email@exemple.com'
EMAIL_HOST_PASSWORD = 'votre-mot-de-passe'
```

### Changer la langue et le fuseau horaire

Dans `settings.py` :

```python
LANGUAGE_CODE = 'fr-fr'  # Français
TIME_ZONE = 'Europe/Paris'  # Fuseau horaire de Paris
```

## 🧪 Tests et développement

### Lancer les tests (si implémentés)

```powershell
python manage.py test
```

### Créer des données de test

Vous pouvez créer des tâches de test via l'interface d'administration ou directement dans l'application.

## 📝 Commandes utiles

```powershell
# Créer un superutilisateur
python manage.py createsuperuser

# Effectuer les migrations
python manage.py makemigrations
python manage.py migrate

# Collecter les fichiers statiques (pour production)
python manage.py collectstatic

# Lancer le serveur
python manage.py runserver

# Vérifier les notifications
python manage.py check_notifications

# Vérifier les notifications pour un utilisateur spécifique
python manage.py check_notifications --user nom_utilisateur
```

## 🔒 Sécurité

⚠️ **Important pour la production** :

1. Changez la `SECRET_KEY`
2. Définissez `DEBUG = False`
3. Configurez `ALLOWED_HOSTS`
4. Utilisez HTTPS
5. Configurez un vrai serveur email
6. Utilisez PostgreSQL ou MySQL au lieu de SQLite
7. Configurez un serveur web (Nginx, Apache) avec Gunicorn/uWSGI

## 🤝 Support

Pour toute question ou problème :
- Consultez la documentation Django : https://docs.djangoproject.com/
- Vérifiez les logs de Django pour les erreurs

## 📄 Licence

Projet éducatif - Utilisation libre

## 👨‍💻 Auteur

Développé avec Django et Bootstrap 5

---

**Bon développement ! 🚀**
