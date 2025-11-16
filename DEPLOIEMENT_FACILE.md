# 🚀 Guide Rapide - Déploiement Nawara Time Manager

## ✅ Étape 1 : Créer un compte PythonAnywhere (5 min)

1. **Allez sur** : https://www.pythonanywhere.com
2. **Cliquez** sur "Start running Python online in less than a minute!"
3. **Choisissez** le plan "Beginner (Free)" - C'est gratuit ! 
4. **Créez votre compte** avec un email et mot de passe
5. **Confirmez votre email** (vérifiez votre boîte de réception)

✅ **Vous avez maintenant votre compte !**

---

## 📤 Étape 2 : Créer un compte GitHub (5 min)

1. **Allez sur** : https://github.com
2. **Cliquez** sur "Sign up"
3. **Créez votre compte** (email, mot de passe, nom d'utilisateur)
4. **Confirmez votre email**

✅ **GitHub est prêt !**

---

## 📦 Étape 3 : Mettre le code sur GitHub (10 min)

### Sur votre ordinateur :

1. **Télécharger Git** si pas déjà installé : https://git-scm.com/downloads
   - Pendant l'installation, laissez toutes les options par défaut
   - Redémarrez PowerShell après l'installation

2. **Ouvrir PowerShell** dans le dossier `time_manager`
   - Naviguez vers : `C:\Users\ASUS\Desktop\time_manager`

3. **Configurer Git** (première fois seulement) :
   ```powershell
   git config --global user.name "Votre Nom"
   git config --global user.email "votre.email@example.com"
   ```

4. **Vérifier que Git est initialisé** :
   ```powershell
   git status
   ```
   - Vous devriez voir "On branch master" ✅

5. **Sur GitHub.com** :
   - Cliquez sur "+" en haut à droite → "New repository"
   - **Nom du dépôt** : `nawara-time-manager`
   - **Visibilité** : Choisissez "Private" (recommandé pour garder privé)
   - **NE PAS** cocher "Initialize this repository with a README"
   - Cliquez sur "Create repository"

6. **GitHub vous affiche des commandes**, copiez l'URL qui ressemble à :
   ```
   https://github.com/VOTRE_USERNAME/nawara-time-manager.git
   ```

7. **Dans PowerShell**, exécutez (remplacez VOTRE_USERNAME) :
   ```powershell
   git remote add origin https://github.com/VOTRE_USERNAME/nawara-time-manager.git
   git branch -M main
   git push -u origin main
   ```

8. **GitHub va demander vos identifiants** :
   - Si ça ne marche pas, vous devrez créer un "Personal Access Token" :
     - Sur GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
     - Generate new token → Cochez "repo" → Generate
     - **Copiez le token** (vous ne le reverrez plus!)
     - Utilisez ce token comme mot de passe

✅ **Votre code est maintenant sur GitHub !**

---

## 🌐 Étape 4 : Déployer sur PythonAnywhere (15 min)

### 4.1 - Cloner le projet

1. **Connectez-vous** à PythonAnywhere
2. **Allez dans** l'onglet "Consoles"
3. **Cliquez** sur "Bash" (nouvelle console Bash)

4. **Dans la console**, tapez (remplacez VOTRE_USERNAME_GITHUB) :
   ```bash
   git clone https://github.com/VOTRE_USERNAME_GITHUB/nawara-time-manager.git
   cd nawara-time-manager
   ```

### 4.2 - Installer Django

```bash
python3.10 -m venv .venv
source .venv/bin/activate
pip install django
```

### 4.3 - Préparer la base de données

```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

✅ **Le code est installé !**

---

## 🌍 Étape 5 : Créer l'application Web (10 min)

1. **Allez dans** l'onglet "Web"
2. **Cliquez** sur "Add a new web app"
3. **Cliquez** sur "Next" (acceptez le domaine gratuit)
4. **Choisissez** "Manual configuration"
5. **Choisissez** "Python 3.10"
6. **Cliquez** sur "Next"

### 5.1 - Configurer les chemins

Dans la section **"Code"** sur la page Web :

1. **Source code** : Cliquez sur le crayon et écrivez :
   ```
   /home/VOTRE_USERNAME_PA/nawara-time-manager
   ```
   (Remplacez VOTRE_USERNAME_PA par votre nom d'utilisateur PythonAnywhere)

2. **Working directory** : Pareil :
   ```
   /home/VOTRE_USERNAME_PA/nawara-time-manager
   ```

3. **Virtualenv** : Cliquez sur le crayon et écrivez :
   ```
   /home/VOTRE_USERNAME_PA/nawara-time-manager/.venv
   ```

### 5.2 - Configurer WSGI

1. **Dans la section "Code"**, cliquez sur le lien **"WSGI configuration file"** (lien bleu)

2. **SUPPRIMEZ TOUT** le contenu du fichier

3. **Copiez-collez ce code** (remplacez VOTRE_USERNAME_PA) :

```python
import os
import sys

# Ajouter le chemin du projet
path = '/home/VOTRE_USERNAME_PA/nawara-time-manager'
if path not in sys.path:
    sys.path.append(path)

# Configuration de Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'time_manager.settings'

# Importer l'application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

4. **Cliquez** sur le bouton "Save" en haut

### 5.3 - Configurer les fichiers statiques

1. **Revenez** à l'onglet "Web"
2. **Dans la section "Static files"**, cliquez sur "Enter URL" :
   - **URL** : `/static/`
   - **Directory** : `/home/VOTRE_USERNAME_PA/nawara-time-manager/staticfiles`
   - Cliquez sur le ✓ (coche verte)

---

## 🔒 Étape 6 : Configuration de sécurité (5 min)

### Retournez dans la console Bash :

```bash
cd /home/VOTRE_USERNAME_PA/nawara-time-manager
nano time_manager/settings.py
```

**Trouvez et modifiez ces lignes** (utilisez les flèches pour naviguer) :

```python
# Ligne ~16
DEBUG = False

# Ligne ~18  
ALLOWED_HOSTS = ['VOTRE_USERNAME_PA.pythonanywhere.com']
```

**Pour sauvegarder** :
- Appuyez sur `Ctrl+X`
- Appuyez sur `Y`
- Appuyez sur `Enter`

---

## ✅ Étape 7 : LANCER L'APPLICATION !

1. **Retournez** dans l'onglet "Web"
2. **Cliquez** sur le **gros bouton vert "Reload"** en haut
3. **Attendez** 5-10 secondes
4. **Cliquez** sur le lien de votre application (en haut) :
   ```
   https://VOTRE_USERNAME_PA.pythonanywhere.com
   ```

🎉 **C'EST EN LIGNE !** 🎉

---

## 📧 Partager avec Nawara

Envoyez-lui simplement le lien :
**https://VOTRE_USERNAME_PA.pythonanywhere.com**

✅ Elle pourra y accéder de n'importe où  
✅ Sur téléphone, tablette, ordinateur  
✅ Pas besoin de créer de compte (connexion automatique)  
✅ Toutes les données sont sauvegardées  

---

## ❓ Problèmes ?

### "Something went wrong" quand j'ouvre le site

1. Allez dans l'onglet "Web"
2. Cliquez sur "Error log" (en haut)
3. Cherchez les lignes en rouge
4. Vérifiez que vous avez bien changé `DEBUG = False` et `ALLOWED_HOSTS`

### Les couleurs/images ne s'affichent pas

1. Console Bash :
   ```bash
   cd nawara-time-manager
   source .venv/bin/activate
   python manage.py collectstatic --noinput
   ```
2. Onglet "Web" → Cliquez sur "Reload"

---

## 🔄 Mettre à jour plus tard

Si vous modifiez le code :

1. **Sur votre PC** :
   ```powershell
   git add .
   git commit -m "Mes modifications"
   git push
   ```

2. **Sur PythonAnywhere** (console Bash) :
   ```bash
   cd nawara-time-manager
   git pull
   source .venv/bin/activate
   python manage.py collectstatic --noinput
   ```

3. **Onglet "Web"** → "Reload"

---

## 💡 Conseils

- **Bookmarkez** le lien PythonAnywhere pour y accéder facilement
- **Notez** vos identifiants GitHub quelque part
- Le plan gratuit est **suffisant** pour une utilisation personnelle
- **Pas de limite** de tâches ou d'utilisateurs

---

Bon déploiement ! 🚀🌸
