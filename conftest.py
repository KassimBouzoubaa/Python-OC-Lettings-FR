import os
import django

# Définir la variable d'environnement DJANGO_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")

# Configurer Django
django.setup()
