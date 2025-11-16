# 📦 Installation Time Manager

## Prérequis
- Python 3.10 ou supérieur installé
- Connexion internet

## 📋 Instructions d'installation

### Windows

1. **Extraire le dossier**
   - Extraire le ZIP dans un emplacement de votre choix (ex: `C:\time_manager`)

2. **Ouvrir PowerShell dans le dossier**
   - Clic droit dans le dossier → "Ouvrir dans le terminal"
   - Ou ouvrir PowerShell et taper : `cd C:\chemin\vers\time_manager`

3. **Créer l'environnement virtuel**
   ```powershell
   python -m venv .venv
   ```

4. **Activer l'environnement virtuel**
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
   
   *Note: Si vous avez une erreur de sécurité, exécutez :*
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

5. **Installer les dépendances**
   ```powershell
   pip install -r requirements.txt
   ```

6. **Initialiser la base de données**
   ```powershell
   python manage.py migrate
   ```

7. **Lancer l'application**
   ```powershell
   python manage.py runserver
   ```

8. **Accéder à l'application**
   - Ouvrir le navigateur et aller sur : **http://127.0.0.1:8000/**
   - L'application s'ouvre automatiquement, pas besoin de créer de compte !

## 🎯 Utilisation quotidienne

### Pour lancer l'application chaque fois :

1. Ouvrir PowerShell dans le dossier
2. Activer l'environnement :
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
3. Lancer le serveur :
   ```powershell
   python manage.py runserver
   ```
4. Aller sur : **http://127.0.0.1:8000/**

### Pour arrêter l'application :
- Appuyer sur `Ctrl+C` dans le terminal

## 📧 Configuration des notifications par email (Optionnel)

Pour recevoir des notifications par email :

1. Ouvrir le fichier `time_manager/settings.py`
2. Trouver la section EMAIL (vers la ligne 110)
3. Remplacer :
   ```python
   EMAIL_HOST_USER = 'votre.email@gmail.com'
   EMAIL_HOST_PASSWORD = 'votre_mot_de_passe_app'
   ```
4. Suivre les instructions dans `CONFIGURATION_EMAIL.md`

## ❓ Problèmes courants

### "Python n'est pas reconnu"
- Installer Python depuis : https://www.python.org/downloads/
- ✅ Cocher "Add Python to PATH" pendant l'installation

### "pip n'est pas reconnu"
- Réinstaller Python avec l'option "Add to PATH"

### La page ne charge pas
- Vérifier que le serveur est bien lancé (message "Starting development server...")
- Vérifier l'URL : **http://127.0.0.1:8000/** (pas localhost)

## 🆘 Support
En cas de problème, vérifier :
1. Python est bien installé : `python --version`
2. L'environnement virtuel est activé ((.venv) apparaît dans le terminal)
3. Le serveur est lancé et affiche "Starting development server"
