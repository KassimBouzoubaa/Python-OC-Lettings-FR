from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator
from django.utils.translation import gettext_lazy as _


class Address(models.Model):
    """
    Modèle représentant une adresse.

    Attributs :
        number (PositiveIntegerField): Le numéro de la maison ou du bâtiment.
        street (CharField): Le nom de la rue.
        city (CharField): La ville.
        state (CharField): L'état ou la région (deux lettres).
        zip_code (PositiveIntegerField): Le code postal.
        country_iso_code (CharField): Le code ISO du pays (trois lettres).

    Méta :
        verbose_name: Nom de l'adresse en français.
        verbose_name_plural: Nom pluriel des adresses en français.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    def __str__(self):
        """
        Retourne une représentation en chaîne de l'adresse sous le format
        'numéro rue'.

        Returns:
            str: La chaîne de caractères représentant l'adresse.
        """
        return f"{self.number} {self.street}"

    class Meta:
        verbose_name = _("adresse")
        verbose_name_plural = _("adresses")


class Letting(models.Model):
    """
    Modèle représentant une location ou un bien immobilier.

    Attributs :
        title (CharField): Le titre ou le nom de la location.
        address (OneToOneField): L'adresse associée à la location.

    Méta :
        verbose_name: Nom de la location en français.
        verbose_name_plural: Nom pluriel des locations en français.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Retourne une représentation en chaîne du titre de la location.

        Returns:
            str: Le titre de la location.
        """
        return self.title
