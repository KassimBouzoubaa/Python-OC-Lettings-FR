from .models import Letting
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from sentry_sdk import capture_exception


def index(request):
    """
    Vue pour afficher la liste des locations.

    Cette vue récupère toutes les instances du modèle `Letting` et les passe au template `index.html`.

    En cas d'erreur serveur, la vue renvoie une page d'erreur 500.

    Args:
        request (HttpRequest): L'objet de requête HTTP.

    Returns:
        HttpResponse: La réponse contenant le rendu du template `index.html` avec la liste des locations.
    """
    try:
        lettings_list = Letting.objects.all()
    except Exception as e:
        capture_exception(e)
        # En cas d'erreur serveur, afficher une page d'erreur 500
        return render(request, "lettings/500.html", status=500)

    context = {"lettings_list": lettings_list}

    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    Vue pour afficher les détails d'une location spécifique.

    Cette vue récupère une instance du modèle `Letting` par son identifiant (`letting_id`).
    Si l'objet n'existe pas, une erreur 404 est renvoyée. En cas d'erreur serveur, une page d'erreur 500 est affichée.

    Args:
        request (HttpRequest): L'objet de requête HTTP.
        letting_id (int): L'identifiant de la location à récupérer.

    Returns:
        HttpResponse: La réponse contenant le rendu du template `letting.html` avec les détails de la location.
    """
    try:
        letting = get_object_or_404(Letting, id=letting_id)
        context = {
            "title": letting.title,
            "address": letting.address,
        }
        return render(request, "lettings/letting.html", context)

    except Http404:
        # Envoyer l'exception à Sentry
        capture_exception(Http404)
        # Gestion spécifique des erreurs 404
        return render(request, "lettings/404.html", status=404)
    except Exception as e:
        capture_exception(e)
        # Gestion des autres erreurs internes du serveur
        return render(request, "lettings/500.html", status=500)
