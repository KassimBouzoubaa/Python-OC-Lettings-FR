from django.shortcuts import render

def index(request):
    """
    Affiche la page d'accueil du site.

    Cette vue tente de rendre le template `index.html`. En cas d'exception
    non prévue (erreur serveur), elle renvoie le template `500.html` pour
    afficher une page d'erreur 500.

    Args:
        request: L'objet HttpRequest contenant les données de la requête.

    Returns:
        HttpResponse: La réponse HTTP contenant le rendu du template approprié.
    """
    try:
        # Code normal pour rendre la page d'accueil
        return render(request, "index.html")
    
    except Exception as e:
        # En cas d'erreur serveur, afficher une page d'erreur 500
        return render(request, "500.html", status=500)
