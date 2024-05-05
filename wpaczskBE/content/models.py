from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from account.models import Profile
from geography.models import Location


class ContentBase(models.Model):
    """
    EN: Abstract base class for content-related entities. Provides common fields for tracking creation, update, and deletion times of content items.
    SK: Abstraktná základná trieda pre obsahovo súvisiace entity. Poskytuje spoločné polia na sledovanie času vytvorenia, aktualizácie a zmazania obsahových položiek.

    Attributes:
        created_at (DateTimeField):
            EN: Timestamp when the content item was created.
            SK: Časová pečiatka vytvorenia obsahovej položky.
        updated_at (DateTimeField):
            EN: Timestamp of the last update of the content item.
            SK: Časová pečiatka poslednej aktualizácie obsahovej položky.
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


class Article(ContentBase):
    """
    EN: Represents an article with metadata for publication. Articles can contain text, images, and PDFs relevant to the content.
    SK: Reprezentuje článok s metadátami na publikovanie. Články môžu obsahovať text, obrázky a PDF súbory relevantné pre obsah.

    Attributes:
        title (CharField):
            EN: The title of the article.
            SK: Titulok článku.
        pdf_file (FileField):
            EN: PDF file of the article.
            SK: PDF súbor článku.
        main_image (ImageField):
            EN: Main image of the article if available.
            SK: Hlavný obrázok článku, ak je k dispozícii.
        publication_date (DateField):
            EN: Publication date of the article.
            SK: Dátum publikácie článku.
        info (CharField):
            EN: Short info or description of the article.
            SK: Krátke info alebo popis článku.
    """

    title = models.CharField(
        max_length=128,
        verbose_name="Titulok článku",
        help_text="Zadajte titulok článku.",
    )
    pdf_file = models.FileField(
        upload_to="articles/",
        verbose_name="PDF súbor článku",
        help_text="Nahrajte PDF súbor článku.",
    )
    main_image = models.ImageField(
        upload_to="article_image/",
        blank=True,
        null=True,
        verbose_name="Titulný obrázok",
        help_text="Nahrajte hlavný obrázok článku, ak je k dispozícii.",
    )
    publication_date = models.DateField(
        verbose_name="Dátum publikácie článku",
        help_text="Zadajte dátum publikácie článku.",
    )
    # TODO Riesit vyber alebo napisanie mena ... author = models.CharField(max_length=128, verbose_name="Autor článku", help_text="Zadajte meno autora článku.") # Reference to the article's author. // Odkaz na autora článku.
    info = models.CharField(
        max_length=128,
        blank=True,
        null=True,
        verbose_name="Krátke info k článku",
        help_text="Zadajte krátky popis alebo informácie o článku.",
    )
    # TODO description = models.TextField() ...
    # TODO gallery = models.ManytoManyFields(Image)...

    class Meta:
        verbose_name = "Článok"
        verbose_name_plural = "Články"

    def __str__(self):
        return self.title


class Event(ContentBase):
    """
    EN: Represents an event with details including dates and related media. Events can be linked to specific locations and have associated images or PDFs.
    SK: Reprezentuje udalosť s detailami vrátane dátumov a súvisiacich médií. Udalosti môžu byť prepojené s konkrétnymi miestami a môžu mať priradené obrázky alebo PDF súbory.

    Attributes:
        title (CharField):
            EN: The title of the event.
            SK: Titulok udalosti.
        pdf_file (FileField):
            EN: Optional PDF file for the event.
            SK: Voliteľný PDF súbor pre udalosť.
        main_image (ImageField):
            EN: Main image of the event if available.
            SK: Hlavný obrázok udalosti, ak je k dispozícii.
        date_from (DateField):
            EN: Start date of the event.
            SK: Dátum začiatku udalosti.
        date_to (DateField):
            EN: End date of the event.
            SK: Dátum konca udalosti.
        url (URLField):
            EN: Web link with more information about the event.
            SK: Webový odkaz s viac informáciami o udalosti.
        info (CharField):
            EN: Short info or description of the event.
            SK: Krátke info alebo popis udalosti.
        location (ForeignKey):
            EN: Location where the event is held.
            SK: Miesto konania udalosti.
    """

    title = models.CharField(
        max_length=128,
        verbose_name="Titulok udalosti",
        help_text="Zadajte titulok udalosti.",
    )
    pdf_file = models.FileField(
        upload_to="events/",
        blank=True,
        null=True,
        verbose_name="PDF súbor udalosti",
        help_text="Nahrajte PDF súbor udalosti, ak je k dispozícii.",
    )
    main_image = models.ImageField(
        upload_to="event_image/",
        blank=True,
        null=True,
        verbose_name="Titulný obrázok",
        help_text="Nahrajte hlavný obrázok udalosti, ak je k dispozícii.",
    )
    date_from = models.DateField(
        verbose_name="Dátum začiatku udalosti",
        help_text="Zadajte dátum začiatku udalosti.",
    )
    date_to = models.DateField(
        verbose_name="Dátum ukončenia udalosti",
        help_text="Zadajte dátum ukončenia udalosti.",
    )
    url = models.URLField(
        blank=True,
        null=True,
        verbose_name="url odkaz na udalosť",
        help_text="Zadajte webový odkaz s informáciami o udalosti.",
    )
    info = models.CharField(
        max_length=128,
        blank=True,
        null=True,
        verbose_name="Krátke info k udalosti",
        help_text="Zadajte krátky popis alebo informácie o udalosti.",
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Miesto udalosti",
        help_text="Vyberte lokáciu, kde sa udalosť koná.",
    )
    # TODO description = models.TextField() ...
    # TODO gallery = models.ManytoManyFields(Image)...

    class Meta:
        verbose_name = "Udalosť"
        verbose_name_plural = "Udalosti"

    def __str__(self):
        return self.title


class Comment(ContentBase):
    """
    EN: Represents a comment added to various content types, such as articles or events. Comments allow users to engage with the content.
    SK: Reprezentuje komentár pridaný k rôznym typom obsahu, ako sú články alebo udalosti. Komentáre umožňujú užívateľom zapojiť sa do obsahu.

    Attributes:
        title (CharField):
            EN: Optional title for the comment.
            SK: Voliteľný titulok pre komentár.
        user (ForeignKey):
            EN: User who added the comment.
            SK: Užívateľ, ktorý pridal komentár.
        content_type (ForeignKey):
            EN: Type of content the comment is linked to.
            SK: Typ obsahu, ku ktorému je komentár priradený.
        object_id (PositiveIntegerField):
            EN: ID of the object the comment is linked to.
            SK: ID objektu, ku ktorému je komentár priradený.
        comment (TextField):
            EN: Text of the comment.
            SK: Text komentára.
    """

    title = models.CharField(
        max_length=128,
        blank=True,
        null=True,
        verbose_name="Titulok komentára",
        help_text="Zadajte titulok komentára.",
    )
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        verbose_name="Užívateľ",
        help_text="Vyberte užívateľa, ktorý komentár pridal.",
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        verbose_name="Typ obsahu",
        help_text="Vyberte typ obsahu, ku ktorému je komentár priradený.",
    )
    object_id = models.PositiveIntegerField(
        verbose_name="ID objektu",
        help_text="Zadajte ID objektu, ku ktorému je komentár priradený.",
    )
    content_object = GenericForeignKey("content_type", "object_id")
    comment = models.TextField(
        verbose_name="Text komentára", help_text="Zadajte text komentára."
    )

    class Meta:
        verbose_name = "Komentár"
        verbose_name_plural = "Komentáre"

    def __str__(self):
        return self.title
