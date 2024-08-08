from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Représente le profil d'un utilisateur avec des informations supplémentaires.

    Attributs:
        user (OneToOneField): L'utilisateur associé à ce profil.
        favorite_city (CharField): La ville préférée de l'utilisateur (optionnelle).
    """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, help_text="L'utilisateur associé à ce profil."
    )
    favorite_city = models.CharField(
        max_length=64,
        blank=True,
        help_text="La ville préférée de l'utilisateur (optionnelle).",
    )

    def __str__(self):
        """
        Retourne une chaîne de caractères représentant ce profil.

        La chaîne retournée est le nom d'utilisateur associé au profil.
        """
        return self.user.username
