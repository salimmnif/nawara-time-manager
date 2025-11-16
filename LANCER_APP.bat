@echo off
echo ====================================
echo   Time Manager - Lancement rapide
echo ====================================
echo.

echo [1/2] Activation de l'environnement virtuel...
call .venv\Scripts\activate.bat

echo [2/2] Demarrage du serveur...
echo.
echo L'application sera accessible sur : http://127.0.0.1:8000/
echo.
echo Appuyez sur Ctrl+C pour arreter le serveur
echo.

python manage.py runserver

pause
