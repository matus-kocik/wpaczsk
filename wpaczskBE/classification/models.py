from django.db import models

from common_models.models import (SEOModel, TimeStampedModel)


class Category(SEOModel, TimeStampedModel):
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


class Tag(SEOModel, TimeStampedModel):
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
