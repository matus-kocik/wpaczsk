from django.db import models
from taggit.managers import TaggableManager


class TimeStampedModel(models.Model):
    """
    EN: An abstract base class model that provides timestamp fields to track the creation, update, and potential deletion of an instance. This model is intended to be inherited by other models to ensure they all include standard timestamp fields, which aids in maintaining the integrity and traceability of data.
    SK: Abstraktná základná trieda modelu, ktorá poskytuje polia s časovými údajmi na sledovanie vytvorenia, aktualizácie a potenciálneho zmazania inštancie. Tento model je určený na dedenie inými modelmi, aby sa zabezpečilo, že všetky zahrnujú štandardné polia s časovými údajmi, čo pomáha udržiavať integritu a vysledovateľnosť dát.

    Attributes:
        created_at (DateTimeField):
            EN: Timestamp when the record was initially created. This field is automatically set to the current date and time when the record is first saved.
            SK: Časový údaj, keď bol záznam pôvodne vytvorený. Toto pole je automaticky nastavené na aktuálny dátum a čas pri prvom uložení záznamu.
        updated_at (DateTimeField):
            EN: Timestamp of the last update to the record. This field is automatically updated to the current date and time every time the record is saved after its initial creation.
            SK: Časový údaj poslednej aktualizácie záznamu. Toto pole je automaticky aktualizované na aktuálny dátum a čas pri každom uložení záznamu po jeho pôvodnom vytvorení.
        deleted_at (DateTimeField):
            EN: Timestamp of when the record was soft deleted, if soft deletion is implemented. This field is used to mark a record as deleted without actually removing it from the database.
            SK: Časový údaj, keď bol záznam mäkko zmazaný, ak je implementované mäkké mazanie. Toto pole sa používa na označenie záznamu ako zmazaného bez jeho skutočného odstránenia z databázy.
    """

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
    """
    EN: An abstract model that provides SEO (Search Engine Optimization) fields to enhance the visibility and searchability of content on search engines.
    SK: Abstraktný model, ktorý poskytuje polia pre SEO (optimalizáciu pre vyhľadávače), zvyšujúce viditeľnosť a vyhľadávateľnosť obsahu na vyhľadávačoch.

    Attributes:
        meta_title (CharField):
            EN: The SEO title of the webpage to enhance search engine rankings.
            SK: SEO titulok webovej stránky pre zlepšenie pozície vo vyhľadávačoch.
        meta_description (TextField):
            EN: A brief description of the webpage content for search engine snippets.
            SK: Stručný popis obsahu webovej stránky pre snippet vyhľadávača.
        meta_keywords (CharField):
            EN: Keywords related to the content of the webpage, used to improve search visibility.
            SK: Kľúčové slová súvisiace s obsahom webovej stránky, používané na zlepšenie viditeľnosti vo vyhľadávaní.
    """

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
    """
    EN: An abstract model that provides tagging functionality using django-taggit.
    SK: Abstraktná trieda modelu, ktorá poskytuje funkciu označovania pomocou django-taggit.
    """

    tags = TaggableManager()

    class Meta:
        abstract = True
