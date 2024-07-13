from django.db import models
from taggit.managers import TaggableManager


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        verbose_name="Vytvorenie",
        help_text="Dátum a čas vytvorenia záznamu",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        verbose_name="Aktualizácia",
        help_text="Dátum a čas poslednej aktualizácie",
    )
    deleted_at = models.DateTimeField(
        null=True,
        verbose_name="Zmazanie",
        help_text="Dátum a čas zmazania, ak ide o mäkké zmazanie",
    )

    class Meta:
        abstract = True


class SEOModel(models.Model):
    meta_title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Meta Titulok",
        help_text="Titulok stránky pre SEO.",
    )
    meta_description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Meta Popis",
        help_text="Popis stránky pre SEO.",
    )
    meta_keywords = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Meta Kľúčové Slová",
        help_text="Kľúčové slová pre SEO, oddeľované čiarkami.",
    )

    class Meta:
        abstract = True


class TaggableModel(models.Model):
    tags = TaggableManager()

    class Meta:
        abstract = True
