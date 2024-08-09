# Utilise une image de base Python officielle
FROM python:3.11-slim

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie les fichiers de l'application dans le conteneur
COPY . /app

# Installe les dépendances Python
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

ENV SENTRY_DSN="https://fdfd0be163a43504a8e8a54335a8c0bd@o4507488574767104.ingest.de.sentry.io/4507737680379984"

# Collecter les fichiers statiques
RUN python manage.py collectstatic --noinput

# Expose le port sur lequel l'application va écouter
EXPOSE 8000

# Commande à exécuter pour démarrer le serveur Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
