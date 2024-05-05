from django.db import models

from common_models.models import SEOModel, TimeStampedModel


class Image(SEOModel, TimeStampedModel):
    """
    EN: Represents an image with a title, description, and file location. This model is used to manage images stored in the system.
    SK: Reprezentuje obrázok s názvom, popisom a umiestnením súboru. Tento model sa používa na správu obrázkov uložených v systéme.

    Attributes:
        title (CharField):
            EN: The title of the image.
            SK: Názov obrázka.
        description (TextField):
            EN: A brief description of the image.
            SK: Stručný popis obrázka.
        image_file (ImageField):
            EN: The file of the image stored in the system.
            SK: Súbor obrázka uloženého v systéme.
    """

    title = models.CharField(
        max_length=64, verbose_name="Názov obrázka", help_text="Názov obrázka"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Popis obrázka", help_text="Popis obrázka"
    )
    image_file = models.ImageField(
        upload_to="images/", verbose_name="Súbor obrázka", help_text="Súbor obrázka"
    )


class Movie(SEOModel, TimeStampedModel):
    """
    EN: Represents a movie with a title, description, and file location. This model is used to manage videos stored in the system.
    SK: Reprezentuje film s názvom, popisom a umiestnením súboru. Tento model sa používa na správu videí uložených v systéme.

    Attributes:
        title (CharField):
            EN: The title of the movie.
            SK: Názov filmu.
        description (TextField):
            EN: A brief description of the movie.
            SK: Stručný popis filmu.
        movie_file (FileField):
            EN: The file of the movie stored in the system.
            SK: Súbor filmu uloženého v systéme.
    """

    title = models.CharField(
        max_length=64, verbose_name="Názov filmu", help_text="Názov filmu"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Popis filmu", help_text="Popis filmu"
    )
    movie_file = models.FileField(
        upload_to="videos/", verbose_name="Súbor videa", help_text="Súbor videa"
    )
