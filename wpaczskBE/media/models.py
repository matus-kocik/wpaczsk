from django.db import models


class MediaBase(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Vytvorenie",
        help_text="Dátum a čas vytvorenia záznamu",
    )  # Record creation time. // Čas vytvorenia záznamu.
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Aktualizácia",
        help_text="Dátum a čas poslednej aktualizácie",
    )  # Record last update time. // Čas poslednej aktualizácie záznamu.
    deleted_at = models.DateTimeField(
        null=True, blank=True, verbose_name="Zmazanie", help_text="Dátum a čas zmazania"
    )  # Record deletion time, if soft deleted. // Čas zmazania záznamu, ak ide o mäkké zmazanie.

    class Meta:
        abstract = True


class Image(MediaBase):
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
    title = models.CharField(
        max_length=64, verbose_name="Názov filmu", help_text="Názov filmu"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Popis filmu", help_text="Popis filmu"
    )
    movie_file = models.FileField(
        upload_to="videos/", verbose_name="Súbor videa", help_text="Súbor videa"
    )
