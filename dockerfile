# Utilise une image de base Python officielle
FROM python:3.11-slim

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie les fichiers de l'application dans le conteneur
COPY . /app

# Copier le fichier .env
COPY .env /app/.env
COPY .env.production /app/.env.production

# Installe les dépendances Python
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt


# Collecter les fichiers statiques
RUN python manage.py collectstatic --noinput

# Expose le port sur lequel l'application va écouter
EXPOSE 8000

# Commande à exécuter pour démarrer le serveur Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
