from django.db import models


class ClassificationBase(models.Model):
    """
    EN: Abstract base class for classification entities like categories and tags. This class provides common fields for tracking the creation, update, and deletion times.
    SK: Abstraktná základná trieda pre klasifikačné entity ako sú kategórie a tagy. Táto trieda poskytuje spoločné polia pre sledovanie času vytvorenia, aktualizácie a zmazania.

    Attributes:
        created_at (DateTimeField):
            EN: Timestamp when the entity was created.
            SK: Časová pečiatka vytvorenia entity.
        updated_at (DateTimeField):
            EN: Timestamp of the last update of the entity.
            SK: Časová pečiatka poslednej aktualizácie entity.
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


class Category(ClassificationBase):
    """
    EN: Represents a category for classifying items. Categories help organize entities into hierarchical structures.
    SK: Reprezentuje kategóriu na klasifikáciu položiek. Kategórie pomáhajú organizovať entity do hierarchických štruktúr.

    Attributes:
        name (CharField):
            EN: The name of the category.
            SK: Názov kategórie.
        description (TextField):
            EN: A brief description of the category.
            SK: Stručný popis kategórie.
    """

    name = models.CharField(
        max_length=32, verbose_name="Názov kategórie", help_text="Názov kategórie."
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Popis", help_text="Popis kategórie."
    )

    class Meta:
        verbose_name = "Kategória"
        verbose_name_plural = "Kategórie"


class Tag(ClassificationBase):
    """
    EN: Represents a tag for labeling and categorizing items. Tags are used to associate keywords with entities to facilitate searching and filtering.
    SK: Reprezentuje tag na označovanie a kategorizáciu položiek. Tagy sa používajú na priradenie kľúčových slov k entitám za účelom uľahčenia vyhľadávania a filtrovania.

    Attributes:
        name (CharField):
            EN: The name of the tag.
            SK: Názov tagu.
        description (TextField):
            EN: A brief description of the tag.
            SK: Stručný popis tagu.
    """

    name = models.CharField(
        max_length=32, verbose_name="Názov tagu", help_text="Názov tagu."
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Popis", help_text="Popis tagu."
    )

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tagy"
