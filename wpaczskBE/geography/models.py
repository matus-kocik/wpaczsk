from django.db import models
from django_countries.fields import CountryField

from common_models.models import SEOModel, TimeStampedModel

class Country(SEOModel, TimeStampedModel):
    """
    EN: Represents a country with multilingual name entries and ISO code. Essential for internationalization and localization of geographic data.
    SK: Reprezentuje krajinu s viacjazyčnými záznamami názvov a ISO kódom. Nevyhnutné pre internacionalizáciu a lokalizáciu geografických údajov.

    Attributes:
        country_info (CountryField):
            EN: Field that includes the ISO code and the country name in multiple languages.
            SK: Pole obsahujúce ISO kód a názov krajiny v rôznych jazykoch.
        czech_name (CharField):
            EN: The name of the country in Czech.
            SK: Názov krajiny v češtine.
        slovak_name (CharField):
            EN: The name of the country in Slovak.
            SK: Názov krajiny v slovenčine.
    """
    country_info = CountryField(blank_label="(select country)", verbose_name="Country")
    czech_name = models.CharField(
        max_length=64,
        verbose_name="Český názov krajiny",
        help_text="Český názov krajiny",
    )
    slovak_name = models.CharField(
        blank=True,
        null=True,
        max_length=64,
        verbose_name="Slovenský názov krajiny",
        help_text="Slovenský názov krajiny",
    )

    class Meta:
        verbose_name = "Krajina"
        verbose_name_plural = "Krajiny"

    def __str__(self):
        return self.czech_name

class Location(SEOModel, TimeStampedModel):
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
        help_text="Zemepisná šírka miesta. Kladné hodnoty reprezentujú sever, záporné hodnoty reprezentujú juh.",
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
