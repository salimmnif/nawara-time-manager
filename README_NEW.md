# 🌸 Nawara Time Manager

Application web de gestion de tâches élégante et moderne avec thème rose.

![Version](https://img.shields.io/badge/version-1.0.0-pink)
![Django](https://img.shields.io/badge/Django-5.2.8-green)
![Python](https://img.shields.io/badge/Python-3.10-blue)

## ✨ Fonctionnalités

- 📝 **Gestion de tâches** : Créer, modifier, supprimer des tâches
- ✅ **Checklist intelligente** : Vue organisée par statut (Aujourd'hui, En cours, À faire, Terminées)
- 📅 **Calendrier** : Visualisation mensuelle, hebdomadaire et journalière
- 🔔 **Notifications** : Alertes automatiques pour les tâches dues
- 📧 **Emails** : Notifications par email (optionnel)
- 🎨 **Design moderne** : Interface rose élégante et responsive
- 🔓 **Connexion automatique** : Pas besoin de créer de compte

## 🚀 Déploiement en ligne

**Suivez le guide** : [`DEPLOIEMENT_FACILE.md`](DEPLOIEMENT_FACILE.md)

Temps estimé : **30-40 minutes**  
Coût : **Gratuit** (PythonAnywhere Free Tier)

## 💻 Installation locale

**Suivez le guide** : [`INSTALLATION.md`](INSTALLATION.md)

### Rapide :

```powershell
# 1. Créer l'environnement
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2. Installer Django
pip install -r requirements.txt

# 3. Initialiser la base de données
python manage.py migrate

# 4. Lancer
python manage.py runserver
```

Puis ouvrez : http://127.0.0.1:8000/

### Encore plus rapide :

Double-cliquez sur **`LANCER_APP.bat`** 🎉

## 📚 Documentation

- 📖 [`DEPLOIEMENT_FACILE.md`](DEPLOIEMENT_FACILE.md) - Guide de déploiement simplifié
- 🌐 [`DEPLOIEMENT_PYTHONANYWHERE.md`](DEPLOIEMENT_PYTHONANYWHERE.md) - Guide détaillé PythonAnywhere
- 📥 [`INSTALLATION.md`](INSTALLATION.md) - Installation locale
- 📧 [`CONFIGURATION_EMAIL.md`](CONFIGURATION_EMAIL.md) - Configuration des notifications email
- 🏗️ [`ARCHITECTURE.md`](ARCHITECTURE.md) - Architecture du projet
- 📂 [`STRUCTURE.md`](STRUCTURE.md) - Structure des fichiers

## 🎯 Utilisation

### Connexion

L'application se connecte **automatiquement** - pas besoin de créer de compte !

### Créer une tâche

1. Cliquez sur "Nouvelle" dans le menu
2. Remplissez le formulaire
3. Enregistrez

### Organiser vos tâches

- **Dashboard** : Vue d'ensemble avec statistiques
- **Liste tâches** : Vue complète avec filtres et recherche
- **Mes Tâches (Checklist)** : Vue organisée avec cases à cocher
- **Calendrier** : Visualisation temporelle

### Actions rapides

- ✅ Marquer comme terminée
- ▶️ Démarrer une tâche
- ⏸️ Mettre en pause
- 🔄 Réouvrir une tâche

## 🛠️ Technologies

- **Framework** : Django 5.2.8
- **Base de données** : SQLite
- **Frontend** : Bootstrap 5 + Bootstrap Icons
- **Python** : 3.10+

## 🎨 Thème

- **Couleur principale** : Rose (`#f06292`)
- **Design** : Moderne, épuré, féminin
- **Responsive** : Adapté mobile, tablette, desktop

## 📧 Configuration email (Optionnel)

Pour recevoir des notifications par email, suivez [`CONFIGURATION_EMAIL.md`](CONFIGURATION_EMAIL.md)

## 🔒 Sécurité

- Connexion automatique pour utilisateur unique
- Admin Django accessible via `/admin/`
- CSRF protection activée
- Middleware de sécurité configuré

## 📝 License

Ce projet est développé pour un usage personnel.

## 💖 À propos

**Nawara Time Manager** - Une application élégante pour organiser votre vie ! 🌸

---

Made with 💗 and Django
