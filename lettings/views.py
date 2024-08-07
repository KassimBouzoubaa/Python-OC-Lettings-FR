from .models import Letting
from django.shortcuts import render, get_object_or_404

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
        # En cas d'erreur serveur, afficher une page d'erreur 500
        return render(request, "500.html", status=500)
    
    context = {"lettings_list": lettings_list}
    return render(request, "index.html", context)


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
        # Utiliser get_object_or_404 pour gérer les erreurs 404
        letting = get_object_or_404(Letting, id=letting_id)
        
        context = {
            "title": letting.title,
            "address": letting.address,
        }
        return render(request, "letting.html", context)
    
    except Exception as e:
        # En cas d'erreur serveur, afficher une page d'erreur 500
        return render(request, "500.html", status=500)
