from django.db import models


class GeographyBase(models.Model):
    """
    EN: Abstract base class for geography-related entities. Provides common fields for tracking creation, update, and deletion times of geographic data.
    SK: Abstraktná základná trieda pre geograficky súvisiace entity. Poskytuje spoločné polia na sledovanie času vytvorenia, aktualizácie a zmazania geografických údajov.

    Attributes:
        created_at (DateTimeField):
            EN: Timestamp when the geographic entity was created.
            SK: Časová pečiatka vytvorenia geografickej entity.
        updated_at (DateTimeField):
            EN: Timestamp of the last update of the geographic entity.
            SK: Časová pečiatka poslednej aktualizácie geografickej entity.
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


class Country(GeographyBase):
    """
    EN: Represents a country with multilingual name entries and ISO code. Essential for internationalization and localization of geographic data.
    SK: Reprezentuje krajinu s viacjazyčnými záznamami názvov a ISO kódom. Nevyhnutné pre internacionalizáciu a lokalizáciu geografických údajov.

    Attributes:
        czech_name (CharField):
            EN: The name of the country in Czech.
            SK: Názov krajiny v češtine.
        slovak_name (CharField):
            EN: The name of the country in Slovak.
            SK: Názov krajiny v slovenčine.
        english_name (CharField):
            EN: The international English name of the country.
            SK: Medzinárodný anglický názov krajiny.
        code (CharField):
            EN: The international ISO code of the country.
            SK: Medzinárodný ISO kód krajiny.
    """

    czech_name = models.CharField(
        max_length=64,
        verbose_name="Český názov krajiny",
        help_text="Český názov krajiny",
    )
    slovak_name = models.CharField(
        max_length=64,
        verbose_name="Slovenský názov krajiny",
        help_text="Slovenský názov krajiny",
    )
    english_name = models.CharField(
        max_length=64,
        verbose_name="Anglický názov krajiny",
        help_text="Medzinárodný anglický názov krajiny",
    )
    code = models.CharField(
        max_length=8,
        verbose_name="Kód krajiny",
        help_text="Medzinárodný ISO kód krajiny",
    )

    class Meta:
        verbose_name = "Krajina"
        verbose_name_plural = "Krajiny"

    def __str__(self):
        return self.czech_name


class Location(GeographyBase):
    """
    EN: Represents a geographic location with coordinates and country association. Used for mapping and location-based services.
    SK: Reprezentuje geografickú lokalitu so súradnicami a priradením krajiny. Používa sa pre mapovanie a služby založené na lokalite.

    Attributes:
        country (ForeignKey):
            EN: The country in which the location is situated.
            SK: Krajina, v ktorej sa lokalita nachádza.
        latitude (FloatField):
            EN: Latitude coordinate, positive for North and negative for South.
            SK: Zemepisná šírka, kladné hodnoty reprezentujú sever, záporné hodnoty juh.
        longitude (FloatField):
            EN: Longitude coordinate, positive for East and negative for West.
            SK: Zemepisná dĺžka, kladné hodnoty reprezentujú východ, záporné hodnoty západ.
    """

    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        verbose_name="Krajina",
        help_text="Názov krajiny",
    )
    latitude = models.FloatField(
        blank=True,
        null=True,
        verbose_name="Zemepisná šírka",
        help_text="Zemepisnú šírka miesta. Kladné hodnoty reprezentujú sever, záporné hodnoty reprezentujú juh.",
    )
    longitude = models.FloatField(
        blank=True,
        null=True,
        verbose_name="Zemepisná dĺžka",
        help_text="Zemepisná dĺžka miesta. Kladné hodnoty reprezentujú východ, záporné hodnoty reprezentujú západ",
    )

    class Meta:
        verbose_name = "Lokalita"
        verbose_name_plural = "Lokality"
