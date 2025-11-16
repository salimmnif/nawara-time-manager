# 🌐 Déploiement de Nawara Time Manager sur PythonAnywhere

## 📋 Prérequis
- Un compte PythonAnywhere (gratuit)
- Votre projet Time Manager

---

## 🚀 Étape 1 : Créer un compte PythonAnywhere

1. Aller sur : **https://www.pythonanywhere.com**
2. Cliquer sur **"Start running Python online in less than a minute!"**
3. Choisir le plan **"Beginner (Free)"**
4. Créer un compte avec votre email
5. Confirmer votre email

---

## 📤 Étape 2 : Préparer les fichiers

### Sur votre ordinateur :

1. **Créer un fichier `.gitignore`** dans le dossier `time_manager` :
   ```
   *.pyc
   __pycache__/
   db.sqlite3
   .venv/
   .env
   *.log
   ```

2. **Créer un compte GitHub** (si vous n'en avez pas) : https://github.com

3. **Installer Git** : https://git-scm.com/downloads

4. **Initialiser le dépôt Git** :
   - Ouvrir PowerShell dans le dossier `time_manager`
   - Exécuter :
   ```powershell
   git init
   git add .
   git commit -m "Initial commit - Nawara Time Manager"
   ```

5. **Créer un dépôt sur GitHub** :
   - Aller sur GitHub → "New repository"
   - Nom : `nawara-time-manager`
   - Visibilité : **Private** (recommandé)
   - Ne pas initialiser avec README
   - Cliquer sur "Create repository"

6. **Pousser le code vers GitHub** :
   ```powershell
   git remote add origin https://github.com/VOTRE_USERNAME/nawara-time-manager.git
   git branch -M main
   git push -u origin main
   ```

---

## 🔧 Étape 3 : Configuration sur PythonAnywhere

### 3.1 Ouvrir une console Bash

1. Se connecter à PythonAnywhere
2. Aller dans l'onglet **"Consoles"**
3. Cliquer sur **"Bash"** pour ouvrir une nouvelle console

### 3.2 Cloner le projet

Dans la console Bash, taper :
```bash
git clone https://github.com/VOTRE_USERNAME/nawara-time-manager.git
cd nawara-time-manager
```

### 3.3 Créer l'environnement virtuel

```bash
python3.10 -m venv .venv
source .venv/bin/activate
pip install django
```

### 3.4 Configurer la base de données

```bash
python manage.py migrate
```

### 3.5 Collecter les fichiers statiques

Modifier `settings.py` avant :
```bash
nano time_manager/settings.py
```

Ajouter à la fin du fichier :
```python
STATIC_ROOT = '/home/VOTRE_USERNAME/nawara-time-manager/staticfiles'
```

Sauvegarder : `Ctrl+X` → `Y` → `Enter`

Ensuite :
```bash
python manage.py collectstatic --noinput
```

---

## 🌍 Étape 4 : Créer l'application Web

### 4.1 Configuration de l'application

1. Aller dans l'onglet **"Web"**
2. Cliquer sur **"Add a new web app"**
3. Cliquer sur **"Next"** (confirmer le domaine gratuit)
4. Choisir **"Manual configuration"**
5. Choisir **"Python 3.10"**
6. Cliquer sur **"Next"**

### 4.2 Configuration du code

Dans la section **"Code"** :

1. **Source code** : `/home/VOTRE_USERNAME/nawara-time-manager`
2. **Working directory** : `/home/VOTRE_USERNAME/nawara-time-manager`
3. **Virtualenv** : `/home/VOTRE_USERNAME/nawara-time-manager/.venv`

### 4.3 Configuration WSGI

1. Cliquer sur le lien **"WSGI configuration file"**
2. **Supprimer tout le contenu** du fichier
3. Copier-coller ce code :

```python
import os
import sys

# Ajouter le chemin du projet
path = '/home/VOTRE_USERNAME/nawara-time-manager'
if path not in sys.path:
    sys.path.append(path)

# Configuration de Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'time_manager.settings'

# Importer l'application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

4. **Remplacer** `VOTRE_USERNAME` par votre nom d'utilisateur PythonAnywhere
5. Sauvegarder : Cliquer sur le bouton **"Save"**

### 4.4 Configuration des fichiers statiques

Dans la section **"Static files"** :

| URL | Directory |
|-----|-----------|
| /static/ | /home/VOTRE_USERNAME/nawara-time-manager/staticfiles |

---

## 🔒 Étape 5 : Sécurité (Important !)

### 5.1 Modifier settings.py pour la production

Retourner dans la console Bash :
```bash
nano time_manager/settings.py
```

Modifier ces lignes :
```python
# AVANT
DEBUG = True
ALLOWED_HOSTS = []

# APRÈS
DEBUG = False
ALLOWED_HOSTS = ['VOTRE_USERNAME.pythonanywhere.com']
```

Sauvegarder et fermer.

### 5.2 Mettre à jour le secret key

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copier la clé générée et la mettre dans `settings.py` :
```python
SECRET_KEY = 'LA_CLE_GENEREE'
```

---

## ✅ Étape 6 : Lancer l'application

1. Retourner dans l'onglet **"Web"**
2. Cliquer sur le gros bouton vert **"Reload VOTRE_USERNAME.pythonanywhere.com"**
3. Attendre quelques secondes
4. Cliquer sur le lien de votre application : **https://VOTRE_USERNAME.pythonanywhere.com**

🎉 **Votre application est en ligne !**

---

## 📧 Partager avec Nawara

Envoyez simplement le lien :
**https://VOTRE_USERNAME.pythonanywhere.com**

L'application :
- ✅ Est accessible 24/7
- ✅ Fonctionne sur ordinateur, tablette et smartphone
- ✅ Se connecte automatiquement (pas besoin de compte)
- ✅ Sauvegarde toutes les données

---

## 🔄 Mettre à jour l'application

Si vous modifiez le code plus tard :

1. Sur votre ordinateur :
   ```powershell
   git add .
   git commit -m "Description des modifications"
   git push
   ```

2. Sur PythonAnywhere (console Bash) :
   ```bash
   cd nawara-time-manager
   git pull
   source .venv/bin/activate
   python manage.py migrate
   python manage.py collectstatic --noinput
   ```

3. Onglet "Web" → Cliquer sur **"Reload"**

---

## ❓ Problèmes courants

### Page "Something went wrong"
1. Onglet "Web" → "Error log" → Vérifier les erreurs
2. Vérifier que `ALLOWED_HOSTS` contient bien votre domaine
3. Vérifier que les chemins dans WSGI sont corrects

### Erreur 502
- Vérifier que le virtualenv est bien configuré
- Vérifier que Django est installé dans le virtualenv

### Les fichiers statiques ne s'affichent pas
- Vérifier la section "Static files" dans l'onglet "Web"
- Re-exécuter `python manage.py collectstatic`

---

## 💡 Alternative sans Git (Plus simple mais moins pro)

Si Git est trop compliqué, vous pouvez :

1. **Uploader directement** :
   - Onglet "Files" sur PythonAnywhere
   - Cliquer sur "Upload a file"
   - Uploader tous les fichiers un par un (long !)

2. Ou utiliser le **ZIP** :
   - Créer un ZIP du projet (sans .venv)
   - Upload le ZIP
   - Dans la console Bash :
   ```bash
   unzip nawara-time-manager.zip
   ```

---

## 🆘 Support

En cas de problème :
1. Vérifier les logs dans l'onglet "Web" → "Error log"
2. Consulter la documentation PythonAnywhere : https://help.pythonanywhere.com
3. Forum PythonAnywhere : https://www.pythonanywhere.com/forums/
