# 📂 Guide des Fichiers - Nawara Time Manager

## 📋 Structure du Projet

```
time_manager/
├── 📁 time_manager/           # Configuration principale du projet Django
├── 📁 tasks/                  # Application principale (gestion des tâches)
├── 📁 .venv/                  # Environnement virtuel Python (ne pas modifier)
├── 📄 manage.py               # Commandes Django
├── 📄 db.sqlite3              # Base de données
└── 📄 requirements.txt        # Liste des dépendances Python
```

---

## 🔧 Fichiers de Configuration Racine

### `manage.py`
**Utilité** : Script principal pour exécuter des commandes Django  
**Commandes courantes** :
```bash
python manage.py runserver    # Lancer le serveur
python manage.py migrate       # Mettre à jour la base de données
python manage.py createsuperuser  # Créer un admin
```
**⚠️ Ne pas modifier**

### `db.sqlite3`
**Utilité** : Base de données contenant toutes les tâches et données  
**Contenu** : Utilisateurs, tâches, notifications  
**⚠️ Ne pas supprimer** (vous perdriez toutes les données)

### `requirements.txt`
**Utilité** : Liste des dépendances Python nécessaires  
**Contenu** : `Django==5.2.8`  
**Quand modifier** : Si vous ajoutez de nouvelles bibliothèques Python

### `.gitignore`
**Utilité** : Indique à Git quels fichiers ignorer  
**Contenu** : `.venv/`, `db.sqlite3`, `__pycache__/`, etc.  
**⚠️ Ne pas modifier** sauf si vous savez ce que vous faites

---

## 📁 Dossier `time_manager/` (Configuration)

### `time_manager/settings.py` ⭐
**Utilité** : Configuration principale de l'application  
**Sections importantes** :
```python
DEBUG = False                    # Mode développement/production
ALLOWED_HOSTS = [...]           # Domaines autorisés
DATABASES = {...}               # Configuration base de données
STATIC_ROOT = ...               # Dossier des fichiers statiques
MIDDLEWARE = [...]              # Middlewares (dont AutoLoginMiddleware)
```
**Quand modifier** :
- Changer les couleurs/thème
- Ajouter des domaines autorisés
- Configurer les emails

### `time_manager/urls.py`
**Utilité** : Routes principales du site  
**Contenu** :
```python
path('admin/', admin.site.urls)    # Interface admin Django
path('', include('tasks.urls'))    # Routes de l'app tasks
```
**Quand modifier** : Rarement, sauf pour ajouter de nouvelles apps

### `time_manager/wsgi.py`
**Utilité** : Configuration pour le serveur web (production)  
**⚠️ Ne pas modifier** (utilisé par PythonAnywhere)

### `time_manager/asgi.py`
**Utilité** : Configuration pour serveur asynchrone  
**⚠️ Ne pas modifier** (non utilisé actuellement)

---

## 📁 Dossier `tasks/` (Application Principale)

### 📄 Fichiers Python Principaux

#### `tasks/models.py` ⭐
**Utilité** : Définit la structure des données  
**Contenu** :
- **`Task`** : Modèle de tâche (titre, description, priorité, statut, etc.)
- **`Notification`** : Modèle de notification

**Exemple** :
```python
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    priority = models.CharField(choices=PRIORITY_CHOICES)
    # ... autres champs
```

**Quand modifier** : Pour ajouter des champs aux tâches (ex: tags, pièces jointes)

#### `tasks/forms.py`
**Utilité** : Formulaires pour créer/modifier des tâches  
**Contenu** :
- `TaskForm` : Formulaire principal de tâche
- `TaskSearchForm` : Formulaire de recherche
- `TaskFilterForm` : Formulaire de filtrage

**Quand modifier** : Pour personnaliser les champs du formulaire

#### `tasks/signals.py` ⭐
**Utilité** : Automatisations (notifications automatiques)  
**Contenu** :
```python
@receiver(post_save, sender=Task)
def check_task_notification(sender, instance, created, **kwargs):
    # Crée automatiquement des notifications
    # Envoie des emails si configuré
```

**Quand modifier** : Pour changer la logique des notifications

#### `tasks/middleware.py`
**Utilité** : Connexion automatique de l'utilisateur  
**Contenu** : `AutoLoginMiddleware` - connecte automatiquement "utilisateur"  
**Quand modifier** : Pour changer le système de connexion

#### `tasks/admin.py`
**Utilité** : Configuration de l'interface admin Django  
**Contenu** : Enregistrement des modèles Task et Notification  
**Accès** : `/admin/` (créer un superuser avec `manage.py createsuperuser`)

---

### 📁 `tasks/views/` (Logique des Pages)

#### `tasks/views/tasks.py` ⭐
**Utilité** : Vues pour gérer les tâches (CRUD)  
**Contenu** :
- `TaskListView` : Liste des tâches avec filtres
- `TaskDetailView` : Détail d'une tâche
- `TaskCreateView` : Créer une tâche
- `TaskUpdateView` : Modifier une tâche
- `TaskDeleteView` : Supprimer une tâche

#### `tasks/views/dashboard.py`
**Utilité** : Page d'accueil avec statistiques  
**Contenu** : `DashboardView` - calcule les stats et affiche le tableau de bord

#### `tasks/views/checklist.py`
**Utilité** : Vue checklist organisée  
**Contenu** : `ChecklistView` - organise les tâches par statut

#### `tasks/views/calendar.py`
**Utilité** : Vues calendrier  
**Contenu** :
- `CalendarView` : Vue mensuelle
- `WeekView` : Vue hebdomadaire
- `DayView` : Vue journalière

#### `tasks/views/quick_actions.py`
**Utilité** : Actions rapides sur les tâches  
**Contenu** :
- `TaskMarkDoneView` : Marquer comme terminée
- `TaskMarkInProgressView` : Marquer en cours
- `TaskMarkTodoView` : Marquer à faire

---

### 📁 `tasks/templates/` (Interface Utilisateur)

#### `time_manager/templates/base.html` ⭐⭐⭐
**Utilité** : Template de base (navbar, footer, CSS)  
**Contenu** :
```html
<style>
    :root {
        --primary-color: #f06292;  /* Couleur rose principale */
        /* ... autres variables CSS ... */
    }
</style>
```

**Quand modifier** : 
- ✨ Changer les couleurs (ligne 8-18)
- 📝 Modifier le nom dans la navbar (ligne 317)
- 🎨 Ajuster les styles CSS

#### `tasks/templates/tasks/dashboard.html`
**Utilité** : Page d'accueil avec statistiques  
**Contenu** : Cartes de stats, graphiques de progression

#### `tasks/templates/tasks/list.html`
**Utilité** : Liste complète des tâches  
**Contenu** : Filtres, recherche, cartes de tâches

#### `tasks/templates/tasks/checklist.html`
**Utilité** : Vue checklist avec cases à cocher  
**Contenu** : Tâches organisées par statut (Aujourd'hui, En cours, À faire, Terminées)

#### `tasks/templates/tasks/detail.html`
**Utilité** : Page de détail d'une tâche  
**Contenu** : Informations complètes, actions rapides

#### `tasks/templates/tasks/form.html`
**Utilité** : Formulaire de création/modification  
**Contenu** : Champs de saisie pour les tâches

#### `tasks/templates/tasks/calendar.html`
**Utilité** : Vue calendrier mensuel  
**Contenu** : Grille calendrier avec tâches

#### `tasks/templates/tasks/notifications.html`
**Utilité** : Liste des notifications  
**Contenu** : Notifications triées par date

---

### 📁 `tasks/migrations/`
**Utilité** : Historique des modifications de la base de données  
**Contenu** : Fichiers Python générés automatiquement  
**⚠️ Ne jamais modifier ou supprimer**

---

### 📁 `tasks/management/commands/`

#### `check_notifications.py`
**Utilité** : Commande pour vérifier les notifications  
**Usage** : `python manage.py check_notifications`  
**Contenu** : Génère des notifications pour les tâches dues

---

## 📁 Dossier `staticfiles/` (Production)
**Utilité** : Fichiers CSS/JS/Images collectés pour production  
**Création** : `python manage.py collectstatic`  
**⚠️ Généré automatiquement, ne pas modifier**

---

## 📄 Fichiers de Documentation

### `README.md` ⭐
**Utilité** : Documentation principale du projet  
**Contenu** : Présentation, fonctionnalités, installation

### `PRET_A_DEPLOYER.md`
**Utilité** : Vue d'ensemble et checklist  
**Contenu** : Résumé de ce qui a été fait

### `DEPLOIEMENT_FACILE.md`
**Utilité** : Guide pas à pas pour déployer sur PythonAnywhere  
**Contenu** : Instructions détaillées étape par étape

### `INSTALLATION.md`
**Utilité** : Guide d'installation locale  
**Contenu** : Instructions pour installer sur PC

### `CONFIGURATION_EMAIL.md`
**Utilité** : Configurer les notifications email  
**Contenu** : Setup Gmail, tokens, SMTP

### `LANCER_APP.bat`
**Utilité** : Script Windows de lancement rapide  
**Usage** : Double-clic pour lancer l'application

---

## 🎨 Comment Personnaliser

### Changer les Couleurs
**Fichier** : `time_manager/templates/base.html`  
**Lignes** : 8-18 (variables CSS)
```css
--primary-color: #f06292;        /* Rose principal */
--primary-light: #fce4ec;        /* Rose clair */
--primary-dark: #ec407a;         /* Rose foncé */
```

### Modifier le Nom de l'App
**Fichiers à modifier** :
- `time_manager/templates/base.html` (ligne 317 - navbar)
- `time_manager/templates/base.html` (ligne 6 - titre)
- `time_manager/templates/base.html` (ligne 384 - footer)

### Ajouter un Champ aux Tâches
1. **Modifier** `tasks/models.py` - ajouter le champ
2. **Exécuter** :
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
3. **Modifier** `tasks/forms.py` - ajouter au formulaire
4. **Modifier** les templates pour afficher le nouveau champ

### Changer la Logique des Notifications
**Fichier** : `tasks/signals.py`  
**Fonction** : `check_task_notification()`  
Modifiez les conditions pour changer quand les notifications sont créées

---

## 🔍 Fichiers à NE PAS Modifier

❌ `manage.py`  
❌ `time_manager/wsgi.py`  
❌ `time_manager/asgi.py`  
❌ Dossier `migrations/`  
❌ Dossier `.venv/`  
❌ `db.sqlite3` (sauf backup)

---

## ✅ Fichiers Fréquemment Modifiés

✏️ `time_manager/templates/base.html` - Design et couleurs  
✏️ `tasks/templates/tasks/*.html` - Contenu des pages  
✏️ `tasks/models.py` - Structure des données  
✏️ `tasks/views/*.py` - Logique métier  
✏️ `tasks/signals.py` - Notifications  
✏️ `time_manager/settings.py` - Configuration

---

## 💡 Conseils

- 📝 **Toujours tester** localement avant de déployer
- 💾 **Sauvegarder** `db.sqlite3` régulièrement
- 🔄 **Commiter** après chaque modification importante
- 📖 **Commenter** votre code pour vous rappeler plus tard
- 🧪 **Créer des tâches test** pour vérifier vos modifications

---

**Besoin d'aide ?** Consultez les autres fichiers de documentation ! 🌸
