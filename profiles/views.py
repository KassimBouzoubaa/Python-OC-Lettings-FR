from django.shortcuts import render, get_object_or_404
from .models import Profile
from django.http import Http404
from sentry_sdk import capture_exception


def index(request):
    """
    Affiche la liste des profils.

    Essaie de récupérer tous les profils depuis la base de données et
    de les afficher sur la page index. En cas d'erreur serveur,
    renvoie une page d'erreur 500.

    Args:
        request (HttpRequest): La requête HTTP reçue.

    Returns:
        HttpResponse: La réponse HTTP avec le rendu du template 'index.html'
                      ou la page d'erreur 500 en cas d'exception.
    """
    try:
        profiles_list = Profile.objects.all()
        context = {"profiles_list": profiles_list}
        return render(request, "profiles/index.html", context)

    except Exception as e:
        capture_exception(e)
        # En cas d'erreur serveur, afficher une page d'erreur 500
        return render(request, "profiles/500.html", status=500)


def profile(request, username):
    """
    Affiche les détails d'un profil basé sur le nom d'utilisateur.

    Essaie de récupérer le profil de l'utilisateur correspondant au nom
    d'utilisateur fourni. En cas de profil introuvable, renvoie une page
    d'erreur 404. En cas d'erreur serveur, renvoie une page d'erreur 500.

    Args:
        request (HttpRequest): La requête HTTP reçue.
        username (str): Le nom d'utilisateur dont le profil doit être affiché.

    Returns:
        HttpResponse: La réponse HTTP avec le rendu du template 'profile.html'
                      ou la page d'erreur 500 en cas d'exception.
    """
    try:
        profile = get_object_or_404(Profile, user__username=username)
        context = {"profile": profile}
        return render(request, "profiles/profile.html", context)

    except Http404 as e:
        # Envoyer l'exception à Sentry
        capture_exception(e)
        # Gestion spécifique des erreurs 404
        return render(request, "profiles/404.html", status=404)
    except Exception as e:
        # Gestion des autres erreurs internes du serveur
        capture_exception(e)
        return render(request, "profiles/500.html", status=500)
