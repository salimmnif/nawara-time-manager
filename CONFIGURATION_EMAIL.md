# Configuration Email pour Time Manager 📧💕

## 🎯 Configuration Gmail

### Étape 1: Activer l'authentification à 2 facteurs
1. Allez sur https://myaccount.google.com/security
2. Activez la "Validation en deux étapes"

### Étape 2: Créer un mot de passe d'application
1. Allez sur https://myaccount.google.com/apppasswords
2. Sélectionnez "Autre (nom personnalisé)"
3. Tapez "Time Manager"
4. Cliquez sur "Générer"
5. Copiez le mot de passe de 16 caractères

### Étape 3: Modifier settings.py
Ouvrez `time_manager/settings.py` et modifiez :

```python
EMAIL_HOST_USER = 'votre.email@gmail.com'  # Votre email Gmail
EMAIL_HOST_PASSWORD = 'xxxx xxxx xxxx xxxx'  # Le mot de passe d'application (16 caractères)
DEFAULT_FROM_EMAIL = 'votre.email@gmail.com'  # Votre email Gmail
```

---

## 📧 Configuration pour d'autres services

### Outlook/Hotmail
```python
EMAIL_HOST = 'smtp-mail.outlook.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'votre.email@outlook.com'
EMAIL_HOST_PASSWORD = 'votre_mot_de_passe'
```

### Yahoo Mail
```python
EMAIL_HOST = 'smtp.mail.yahoo.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'votre.email@yahoo.com'
EMAIL_HOST_PASSWORD = 'votre_mot_de_passe_app'
```

---

## 🧪 Mode Test (Console)

Pour tester sans configurer d'email, dans `settings.py` :

```python
# Décommentez cette ligne pour afficher les emails dans la console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

Les emails s'afficheront dans le terminal au lieu d'être envoyés.

---

## ✨ Fonctionnalités Email

### Quand les emails sont envoyés:
- ✅ Tâche due aujourd'hui
- ❌ Tâche en retard
- 📅 Automatiquement au changement de date
- 💾 À la création/modification de tâche

### Format des emails:
- 💕 Design rose assorti à l'application
- 📱 Responsive (mobile-friendly)
- 🔗 Lien direct vers la tâche
- 📊 Détails complets (titre, date, priorité, description)

---

## 🔒 Sécurité

⚠️ **Important**: Ne partagez JAMAIS vos identifiants email !

Pour la production, utilisez des variables d'environnement :

```python
import os

EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
```

---

## 🐛 Résolution de problèmes

### Les emails ne s'envoient pas:
1. Vérifiez que l'utilisateur a un email dans son profil
2. Vérifiez les identifiants dans `settings.py`
3. Vérifiez que l'authentification 2FA est activée (Gmail)
4. Regardez les erreurs dans la console Django

### Tester l'envoi d'email:
```bash
python manage.py shell
```

```python
from django.core.mail import send_mail
send_mail(
    'Test',
    'Message de test',
    'votre.email@gmail.com',
    ['destinataire@example.com'],
)
```

---

## 📝 Notes

- Les emails sont envoyés en HTML avec fallback texte
- `fail_silently=True` : L'app continue même si l'email échoue
- Les notifications sont toujours créées même si l'email échoue
- Design rose cohérent avec l'interface web 💕✨
