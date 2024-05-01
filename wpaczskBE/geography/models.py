from django.db import models

class GeographyBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Vytvorenie", help_text="Dátum a čas vytvorenia záznamu") # Record creation time. // Čas vytvorenia záznamu.
    update_at = models.DateTimeField(auto_now=True, verbose_name="Aktualizácia", help_text="Dátum a čas poslednej aktualizácie") # Record last update time. // Čas poslednej aktualizácie záznamu.
    delete_at = models.DateTimeField(null=True, blank=True, verbose_name="Zmazanie", help_text="Dátum a čas zmazania") # Record deletion time, if soft deleted. // Čas zmazania záznamu, ak ide o mäkké zmazanie.
    
    class Meta:
        abstract = True

class Country(GeographyBase):
    czech_name = models.CharField(max_length=64, verbose_name="Český názov krajiny", help_text="Český názov krajiny") # Name of the country. // Názov krajiny.
    slovak_name = models.CharField(max_length=64, verbose_name="Slovenský názov krajiny", help_text="Slovenský názov krajiny") # Name of the country. // Názov krajiny.
    english_name = models.CharField(max_length=64, verbose_name="Anglický názov krajiny", help_text="Medzinárodný anglický názov krajiny") # Name of the country. // Názov krajiny.
    code = models.CharField(max_length=8, verbose_name="Kód krajiny", help_text="Medzinárodný ISO kód krajiny") # ISO code of the country, e.g., 'SK' for Slovakia. // ISO kód krajiny, napr. 'SK' pre Slovensko.
    
    class Meta:
        verbose_name = "Krajina"
        verbose_name_plural = "Krajiny"
        
class Location(GeographyBase):
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, verbose_name="Krajina", help_text="Názov krajiny") # Reference to the Country model. // Odkaz na model Country.
    latitude = models.FloatField(verbose_name="Zemepisná šírka", help_text="Zemepisnú šírka miesta. Kladné hodnoty reprezentujú sever, záporné hodnoty reprezentujú juh.") # Latitude for the event location. // Zemepisná šírka miesta konania.
    longitude = models.FloatField(verbose_name="Zemepisná dĺžka", help_text="Zemepisná dĺžka miesta. Kladné hodnoty reprezentujú východ, záporné hodnoty reprezentujú západ") # Longitude for the event location. // Zemepisná dĺžka miesta konania.
    
    class Meta:
        verbose_name = "Lokalita"
        verbose_name_plural = "Lokality"
    
    
    