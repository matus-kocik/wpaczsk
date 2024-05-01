from django.contrib.auth.models import User
from django.db import models
from wpaczskBE.taxonomy.models import TaxonomySpecies, TaxonomySubspecies

class BreedingRecord(models.Model):
    breeder = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Chovateľ", help_text="Chovateľ a člen organizácie") # The user responsible for the breeding. // Užívateľ zodpovedný za chov.
    species = models.ForeignKey(TaxonomySpecies, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Druh", help_text="Druh, ktorý sa chová") # Connection to the Species table. // Kľúč pre spojenie s tabuľkou Species.
    subspecies = models.ForeignKey(TaxonomySubspecies, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Poddruh", help_text="Poddruh, ktorý sa chová") # The subspecies being bred. // Poddruh, ktorý sa chová.
    year = models.IntegerField(verbose_name="Rok", help_text="Rok, pre ktorý je záznam o chove") # The year of the breeding record. // Rok, pre ktorý je záznam o chove.
    number_of_males = models.IntegerField(verbose_name="Počet samcov", help_text="Počet samcov chovaného druhu/poddruhu") # Number of male animals. // Počet samcov.
    number_of_females = models.IntegerField(verbose_name="Počet samíc", help_text="Počet samíc chovaného druhu/poddruhu") # Number of female animals. // Počet samíc.
    total_of_species = models.IntegerField(verbose_name="Celkový počet kusov", help_text="Celkový počet kusov chovaného druhu") # Total number of species bred. // Celkový počet chovaných druhov.
    number_of_male_offsprings = models.IntegerField(verbose_name="Počet samcov odchov", help_text="Počet samcov odchovaného druhu/poddruhu") # Total number of male offsprings produced. // Počet samcov odchovaného druhu/poddruhu
    number_of_female_offsprings = models.IntegerField(verbose_name="Počet samíc odchov", help_text="Počet samíc odchovaného druhu/poddruhu") # Total number of female offsprings produced. // Počet samíc odchovaného druhu/poddruhu
    number_of_unspecified_offsprings = models.IntegerField(verbose_name="Neurčený odchov", help_text="Počet kusov neurčeného pohlavia druhu/poddruhu") # Total of number female offsprings produced. // Celkový počet produkovaných potomkov.
    total_offsprings = models.IntegerField(verbose_name="Celkový počet potomkov", help_text="Celkový počet potomkov") # Total number of offsprings produced. // Celkový počet produkovaných potomkov.
    notes = models.TextField(verbose_name="Poznámky", help_text="Dodatočné poznámky o chove", blank=True, null=True) # Additional notes about the breeding. // Dodatočné poznámky o chove.
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Vytvorenie", help_text="Čas vytvorenia záznamu") # Record creation time. // Čas vytvorenia záznamu.
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Aktualizácia", help_text="Čas poslednej aktualizácie záznamu") # Record last update time. // Čas poslednej aktualizácie záznamu.
    deleted_at = models.DateTimeField(blank=True, null=True, verbose_name="Zmazanie", help_text="Čas zmazania záznamu, ak ide o mäkké zmazanie") # Record deletion time, if soft deleted. // Čas zmazania záznamu, ak ide o mäkké zmazanie.

    class Meta:
        verbose_name = "Záznam o chove"
        verbose_name_plural = "Záznamy o chove"

class Ring(models.Model):
    size = models.FloatField(blank=True, null=True, verbose_name="Veľkosť", help_text="Veľkosť kružku") # Size of the ring. // Veľkosť kružku.

    class Meta:
        verbose_name = "Krúžok"
        verbose_name_plural = "Krúžky"
