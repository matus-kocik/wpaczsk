from django.db import models
from django_countries.fields import CountryField

from common_models.models import SEOModel, TimeStampedModel


class Country(SEOModel, TimeStampedModel):
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
