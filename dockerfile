# Utilise une image de base Python officielle
FROM python:3.11-slim

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie les fichiers de l'application dans le conteneur
COPY . /app

# Installe les dépendances Python
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Expose le port sur lequel l'application va écouter
EXPOSE 8000

# Collecter les fichiers statiques
RUN python manage.py collectstatic --noinput

# Commande à exécuter pour démarrer le serveur Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
