from django.db import models
from taxonomy.models import TaxonomySubspecies
from account.models import BreederProfile

class BreedingBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Vytvorenie", help_text="Dátum a čas vytvorenia záznamu") # Record creation time. // Čas vytvorenia záznamu.
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Aktualizácia", help_text="Dátum a čas poslednej aktualizácie") # Record last update time. // Čas poslednej aktualizácie záznamu.
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name="Zmazanie", help_text="Dátum a čas zmazania") # Record deletion time, if soft deleted. // Čas zmazania záznamu, ak ide o mäkké zmazanie.
    
    class Meta:
        abstract = True

class BreedingRecord(BreedingBase):
    breeder = models.ForeignKey(BreederProfile, on_delete=models.CASCADE, verbose_name="Chovateľ", help_text="Chovateľ a člen organizácie") # The user responsible for the breeding. // Užívateľ zodpovedný za chov.
    subspecies = models.ForeignKey(TaxonomySubspecies, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Poddruh", help_text="Poddruh, ktorý sa chová") # The subspecies being bred. // Poddruh, ktorý sa chová.
    year = models.IntegerField(verbose_name="Rok", help_text="Rok, pre ktorý je záznam o chove") # The year of the breeding record. // Rok, pre ktorý je záznam o chove.
    number_of_males = models.PositiveIntegerField(default=0, verbose_name="Počet samcov", help_text="Počet samcov chovaného druhu/poddruhu") # Number of male animals. // Počet samcov.
    number_of_females = models.PositiveIntegerField(default=0, verbose_name="Počet samíc", help_text="Počet samíc chovaného druhu/poddruhu") # Number of female animals. // Počet samíc.
    number_of_males_offsprings = models.PositiveIntegerField(default=0, verbose_name="Počet samcov odchov", help_text="Počet samcov odchovaného druhu/poddruhu") # Total number of male offsprings produced. // Počet samcov odchovaného druhu/poddruhu
    number_of_females_offsprings = models.PositiveIntegerField(default=0, verbose_name="Počet samíc odchov", help_text="Počet samíc odchovaného druhu/poddruhu") # Total number of female offsprings produced. // Počet samíc odchovaného druhu/poddruhu
    number_of_unspecified_offsprings = models.PositiveIntegerField(default=0, verbose_name="Neurčený odchov", help_text="Počet kusov neurčeného pohlavia druhu/poddruhu") # Total of number female offsprings produced. // Celkový počet produkovaných potomkov.
    notes = models.TextField(blank=True, null=True, verbose_name="Poznámky", help_text="Dodatočné poznámky o chove") # Additional notes about the breeding. // Dodatočné poznámky o chove.

    class Meta:
        verbose_name = "Záznam o chove"
        verbose_name_plural = "Záznamy o chove"
        
    @property
    def total_count_of_species(self):
        return self.number_of_males + self.number_of_females
    
    @property
    def total_count_offsprings(self):
        return self.number_of_males_offsprings + self.number_of_females_offsprings + self.number_of_unspecified_offsprings

class Project(BreedingBase):
    name = models.CharField(max_length=255, verbose_name="Názov projektu", help_text="Plný názov projektu alebo iniciatívy.")
    description = models.TextField(blank=True, verbose_name="Popis projektu", help_text="Detailný popis projektu vrátane hlavných cieľov a očakávaných výsledkov.")
    start_date = models.DateField(blank=True, null=True, verbose_name="Dátum začiatku", help_text="Dátum začiatku realizácie projektu.")
    end_date = models.DateField(blank=True, null=True, verbose_name="Dátum ukončenia", help_text="Predpokladaný dátum ukončenia projektu. Môže byť aktualizovaný podľa priebehu projektu.")
    member = models.ManyToManyField(BreederProfile, related_name="membered_projects" , verbose_name="Členovia projektu", help_text="Chovatelia zapojení do projektu.")
    coordinator = models.ForeignKey(BreederProfile, on_delete=models.CASCADE, related_name='coordinated_projects', verbose_name="Koordinátor projektu", help_text="Chovateľ zodpovedný za vedenie a koordináciu projektu.")

    class Meta:
        verbose_name = 'Projekt'
        verbose_name_plural = 'Projekty'

    def __str__(self):
        return self.name
