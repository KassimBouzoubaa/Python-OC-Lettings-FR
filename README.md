## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

### Configurer les variables d'environnement

1. **Créer un fichier `.env` à la racine du projet**. Ce fichier doit contenir les variables d'environnement suivantes :

    ```env
    SECRET_KEY=your_secret_key_here
    SENTRY_DSN=your_sentry_dsn_here
    ```

2. Remplacez `your_secret_key_here` par une clé secrète générée pour votre projet.
3. Remplacez `your_sentry_dsn_here` par l'URL de votre DSN Sentry.

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

### Vue d'ensemble

Le déploiement de l'application est automatisé grâce à GitHub Actions et Render. Le processus CI/CD gère la compilation, les tests, la conteneurisation, et le déploiement de l'application.

1. **Compilation et Tests** : Lors d'un push ou d'une pull request sur la branche `master`, GitHub Actions vérifie le code en exécutant des tests et des vérifications de qualité.
2. **Conteneurisation** : Si les tests passent, une image Docker est construite et poussée vers Docker Hub.
3. **Déploiement** : L'image Docker est ensuite déployée sur Render pour mise en production.

### Configuration Requise

1. **Secrets GitHub** :
   - `DOCKER_USERNAME` : Nom d'utilisateur Docker Hub.
   - `DOCKER_PASSWORD` : Mot de passe Docker Hub.
   - `RENDER_API_KEY` : Clé API Render.
   - `SECRET_KEY` : Clé secrète pour Django.
   - `SENTRY_DSN` : Le DSN (Data Source Name) fourni par Sentry pour la configuration de la surveillance des erreurs.
   - `ALLOWED_HOSTS`: Les noms de domaine ou adresses IP autorisés à accéder à votre application Django, séparés par des virgules (par exemple : python-oc-lettings-fr-sgwn.onrender.com,127.0.0.1).


2. **Dockerfile** : Assurez-vous qu'il est configuré pour construire l'image Docker de l'application.

3. **Fichier `requirements.txt`** : Incluez toutes les dépendances nécessaires, comme `black`, `flake8`, et `pytest`.

4. **Configuration Render** :
   - Créez un service web sur Render.
   - Configurez-le pour utiliser Docker et exposez le port approprié (par défaut 8000).
   - Notez l'ID du service pour le workflow GitHub Actions.

### Étapes de Déploiement

1. **Configurer les Secrets GitHub** :
   - Ajoutez les secrets `DOCKER_USERNAME`, `DOCKER_PASSWORD`, `RENDER_API_KEY` , `ALLOWED_HOSTS`, et `SECRET_KEY` dans les paramètres de votre dépôt GitHub.

2. **Configurer Dockerfile** :
   - Assurez-vous qu'il est correctement configuré pour construire l'image Docker.

3. **Configurer GitHub Actions** :
   - Vérifiez que le fichier `.github/workflows/main.yml` est présent et correctement configuré.

4. **Déployer l'Application** :
   - Faites un push ou créez une pull request sur la branche `master`.
   - GitHub Actions exécutera le workflow automatiquement.

5. **Vérifier le Déploiement** :
   - Accédez à l'URL fournie par Render pour vérifier que l'application fonctionne correctement.

### Remarques

- Testez votre configuration Docker et votre application localement avant le déploiement.
- Gardez les secrets sécurisés et ne les exposez pas dans le code source.

