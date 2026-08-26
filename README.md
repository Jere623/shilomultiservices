# Shilo Multi-Services – MVP

Application Django pour une entreprise de nettoyage : accueil, prestations, demande de devis, contact et administration.

## Local
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

Puis http://127.0.0.1:8000 et /admin/.

## Production
Le fichier render.yaml prévoit un service Django et PostgreSQL sur Render. Connecter le dépôt GitHub à Render et déployer le blueprint. Ajouter ensuite shilomultiservices.com dans Custom Domains et configurer le DNS du registrar.
