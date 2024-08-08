import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_index_view():
    # Créez une instance de client pour simuler des requêtes HTTP
    client = Client()

    # Effectuez une requête GET vers l'URL de la vue index
    response = client.get(reverse("index"))

    # Vérifiez que la réponse a le code de statut 200 OK
    assert response.status_code == 200

    # Vérifiez que le contenu de la réponse contient une partie attendue (assurez-vous que cela correspond à ce qui est dans votre template index.html)
    assert (
        "Welcome to Holiday Homes" in response.content.decode()
    )  # Remplacez par un texte spécifique à votre template
