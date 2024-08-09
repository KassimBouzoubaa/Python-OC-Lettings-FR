=======================================================
Projet Python-OC-Lettings-FR
=======================================================

Description du Projet
=====================
Python-OC-Lettings-FR est une application Django permettant la gestion de locations de logements.

Installation du Projet
=======================
1. **Cloner le dépôt :**

   .. code-block:: bash

      git clone https://github.com/KassimBouzoubaa/Python-OC-Lettings-FR.git
      cd Python-OC-Lettings-FR

2. **Créer et activer un environnement virtuel :**

   .. code-block:: bash

      python3 -m venv .venv
      source .venv/bin/activate

3. **Installer les dépendances :**

   .. code-block:: bash

      pip install -r requirements.txt

Guide de Démarrage Rapide
==========================
1. **Appliquer les migrations de la base de données :**

   .. code-block:: bash

      python manage.py migrate

2. **Lancer le serveur de développement :**

   .. code-block:: bash

      python manage.py runserver

3. **Accéder à l'application :**

   Ouvrez votre navigateur et allez à `http://127.0.0.1:8000`.

Technologies et Langages de Programmation
=========================================
- **Django** : Cadre de développement web en Python.
- **Python 3.11** : Langage de programmation principal.
- **Docker** : Conteneurisation de l'application.
- **GitHub Actions** : Intégration continue et déploiement.

Structure de la Base de Données et Modèles de Données
======================================================
L'application utilise une base de données relationnelle avec les modèles suivants :

- **Profile** : Représente un utilisateur avec une ville favorite.
- **Letting** : Représente une location, associée à une adresse.
- **Address** : Modèle représentant une adresse (numéro, rue, ville, etc.).

Interfaces de Programmation
===========================
L'application expose les interfaces suivantes :

- **Endpoints REST API** : 
  - `api/profiles/` : Gestion des profils utilisateurs.
  - `api/lettings/` : Gestion des locations.

Guide d'Utilisation
===================

Cas d'utilisation 1 : Consulter un profil utilisateur
-----------------------------------------------------

1. **Accéder à la liste des profils :**
   
   - Depuis la page d'accueil, cliquez sur l'onglet "Profils" dans le menu de navigation.
   - Vous serez redirigé vers une page affichant la liste de tous les profils utilisateurs disponibles.

2. **Sélectionner un profil à consulter :**

   - Parcourez la liste des profils et cliquez sur le nom du profil que vous souhaitez consulter.
   - Vous serez redirigé vers la page de détails de ce profil où vous pourrez voir toutes les informations associées.

Cas d'utilisation 2 : Consulter une location
--------------------------------------------

1. **Naviguer vers la section "Locations" :**
   
   - Depuis la page d'accueil, cliquez sur l'onglet "Locations" (ou "Lettings") dans le menu de navigation.
   - Vous serez redirigé vers une page affichant la liste de toutes les locations disponibles.

2. **Sélectionner une location à consulter :**

   - Parcourez la liste des locations et cliquez sur l'adresse ou le nom de la location que vous souhaitez consulter.
   - Vous serez redirigé vers la page de détails de cette location où vous pourrez voir toutes les informations pertinentes.


Procédures de Déploiement et de Gestion
=======================================
1. **Déploiement sur Render via GitHub Actions :**

   Le déploiement sur Render est automatisé en utilisant GitHub Actions. Suivez les étapes ci-dessous pour configurer et déployer votre application.

   - **Étape 1 : Configurer les Secrets GitHub**
     
     Assurez-vous que les secrets GitHub suivants sont configurés dans votre dépôt. Ces secrets sont nécessaires pour le bon fonctionnement de l'intégration et du déploiement continus.

     - `DOCKER_USERNAME` : Nom d'utilisateur Docker Hub.
     - `DOCKER_PASSWORD` : Mot de passe Docker Hub.
     - `RENDER_API_KEY` : Clé API Render.
     - `SECRET_KEY` : Clé secrète pour Django.
     - `SENTRY_DSN` : URL DSN pour Sentry (pour le suivi des erreurs).
     - `ALLOWED_HOSTS` : Hôtes autorisés pour Django (e.g., `python-oc-lettings-fr-sgwn.onrender.com`).
     - `DJANGO_ENV` : Environnement Django (`production` ou `development`).

   - **Étape 2 : Déployer l'Application**
     
     Une fois les secrets configurés et le fichier GitHub Actions en place, chaque commit poussé sur la branche `master` déclenchera automatiquement le processus de déploiement vers Render.

   - **Étape 3 : Suivi du Déploiement**
     
     Vous pouvez suivre le statut du déploiement via la page des Actions de votre dépôt GitHub. Une fois le déploiement terminé, l'application sera disponible sur l'URL configurée sur Render.

2. **Gestion de l'application :**

   - **Vérification des logs avec Sentry :**
     
     Pour suivre les erreurs et les événements de votre application en production, nous utilisons Sentry, un service de suivi des erreurs. Sentry est intégré à votre application via le SDK Sentry pour Django.

     - **Configuration :** Assurez-vous que le DSN de Sentry est correctement configuré dans vos variables d'environnement (`SENTRY_DSN`).
     - **Consultation des logs :** Rendez-vous sur le tableau de bord de Sentry pour consulter les erreurs et événements capturés par l'application. Sentry fournit une interface intuitive pour explorer les erreurs, voir leur fréquence, et identifier les causes profondes.
     - **Alertes :** Vous pouvez configurer des alertes dans Sentry pour être informé par email ou via d'autres intégrations (comme Slack) lorsque des erreurs critiques surviennent.

   - **Mise à jour de l'application :**
     
     Les mises à jour se font automatiquement via les pushes vers la branche `master` grâce à l'intégration avec GitHub Actions.