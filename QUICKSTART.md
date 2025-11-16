# Guide de Démarrage Rapide - Time Manager

## Installation en 5 minutes

### 1. Prérequis
- Python 3.8+ installé
- pip installé

### 2. Installation rapide

```powershell
# Naviguer vers le dossier du projet
cd C:\Users\ASUS\Desktop\time_manager

# Créer un environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
.\venv\Scripts\Activate.ps1

# Installer Django
pip install -r requirements.txt

# Créer la base de données
python manage.py migrate

# Créer un compte admin
python manage.py createsuperuser

# Lancer le serveur
python manage.py runserver
```

### 3. Première connexion

1. Ouvrez votre navigateur
2. Allez à : http://127.0.0.1:8000/
3. Cliquez sur "Inscription" ou utilisez le compte admin créé
4. Commencez à créer vos tâches !

## Fonctionnalités principales

### Créer une tâche
1. Navbar → "Nouvelle tâche"
2. Remplir le formulaire
3. Cliquer sur "Créer"

### Voir le calendrier
1. Navbar → "Calendrier"
2. Naviguer entre les mois
3. Cliquer sur un jour pour voir ses tâches

### Tableau de bord
- Vue d'ensemble de vos tâches
- Statistiques et progression
- Tâches en retard et du jour

### Notifications
1. Exécuter : `python manage.py check_notifications`
2. Navbar → "Notifications"
3. Voir les alertes automatiques

## Résolution de problèmes

### Django n'est pas installé
```powershell
pip install Django
```

### Erreur de migration
```powershell
python manage.py migrate --run-syncdb
```

### Le serveur ne démarre pas
- Vérifiez que le port 8000 est libre
- Ou utilisez : `python manage.py runserver 8080`

## Utilisation avancée

### Planifier les notifications (Windows)

Créer une tâche planifiée Windows :
1. Ouvrir "Planificateur de tâches"
2. Créer une tâche de base
3. Déclencheur : Quotidien à 8h00
4. Action : Démarrer un programme
5. Programme : `C:\Users\ASUS\Desktop\time_manager\venv\Scripts\python.exe`
6. Argument : `C:\Users\ASUS\Desktop\time_manager\manage.py check_notifications`

### Interface d'administration

URL : http://127.0.0.1:8000/admin/

Fonctionnalités :
- Gestion complète des utilisateurs
- Modification en masse des tâches
- Création de notifications manuelles
- Statistiques détaillées

## Astuces

### Recherche rapide
- Utilisez les filtres sur la page "Mes tâches"
- Recherchez par mot-clé dans le titre/description

### Organisation
- Utilisez des catégories cohérentes (Travail, Personnel, Études, etc.)
- Définissez les priorités correctement
- Mettez à jour le statut régulièrement

### Vues calendrier
- **Vue mensuelle** : Planification à long terme
- **Vue hebdomadaire** : Organisation de la semaine
- **Vue journalière** : Focus sur aujourd'hui

## Support

En cas de problème :
1. Vérifiez que l'environnement virtuel est activé
2. Vérifiez les logs dans le terminal
3. Consultez le README.md complet
4. Documentation Django : https://docs.djangoproject.com/

---

**Bon travail avec Time Manager ! 📅✨**
