from django.db import models


class MediaBase(models.Model):
    """
    EN: Abstract base class for media entities. Provides common fields for tracking creation, update, and deletion times of media items such as images and videos.
    SK: Abstraktná základná trieda pre mediálne entity. Poskytuje spoločné polia na sledovanie času vytvorenia, aktualizácie a zmazania mediálnych položiek, ako sú obrázky a videá.

    Attributes:
        created_at (DateTimeField):
            EN: Timestamp when the media item was created.
            SK: Časová pečiatka vytvorenia mediálnej položky.
        updated_at (DateTimeField):
            EN: Timestamp of the last update of the media item.
            SK: Časová pečiatka poslednej aktualizácie mediálnej položky.
        deleted_at (DateTimeField):
            EN: Timestamp of deletion if soft deletion is implemented.
            SK: Časová pečiatka zmazania, ak je implementované mäkké zmazanie.
    """

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Vytvorenie",
        help_text="Dátum a čas vytvorenia záznamu",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Aktualizácia",
        help_text="Dátum a čas poslednej aktualizácie",
    )
    deleted_at = models.DateTimeField(
        null=True, blank=True, verbose_name="Zmazanie", help_text="Dátum a čas zmazania"
    )

    class Meta:
        abstract = True


class Image(MediaBase):
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


class Movie(MediaBase):
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
