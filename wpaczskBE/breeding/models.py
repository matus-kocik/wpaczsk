from django.db import models

from account.models import BreederProfile
from common_models.models import SEOModel, TaggableManager, TimeStampedModel
from taxonomy.models import TaxonomySubspecies


class BreedingRecord(SEOModel, TimeStampedModel):
    """
    EN: Represents a record of breeding activities within a specific project or initiative, tracking detailed information about the breeding process.
    SK: Reprezentuje záznam o chovateľských aktivitách v rámci konkrétneho projektu alebo iniciatívy, sleduje detailné informácie o procese chovu.

    Attributes:
        breeder (ForeignKey):
            EN: The breeder responsible for the breeding, linked to the BreederProfile model.
            SK: Chovateľ zodpovedný za chov, prepojený s modelom BreederProfile.
        subspecies (ForeignKey):
            EN: The specific subspecies being bred, linked to the TaxonomySubspecies model.
            SK: Konkrétny poddruh, ktorý sa chová, prepojený s modelom TaxonomySubspecies.
        year (IntegerField):
            EN: The year for which the breeding record is maintained.
            SK: Rok, pre ktorý sa udržiava záznam o chove.
        number_of_males (PositiveIntegerField):
            EN: Number of male individuals of the species/subspecies involved in breeding.
            SK: Počet samcov druhu/poddruhu zapojených do chovu.
        number_of_females (PositiveIntegerField):
            EN: Number of female individuals of the species/subspecies involved in breeding.
            SK: Počet samíc druhu/poddruhu zapojených do chovu.
        number_of_males_offsprings (PositiveIntegerField):
            EN: Total number of male offsprings produced.
            SK: Celkový počet produkovaných samcov.
        number_of_females_offsprings (PositiveIntegerField):
            EN: Total number of female offsprings produced.
            SK: Celkový počet produkovaných samíc.
        number_of_unspecified_offsprings (PositiveIntegerField):
            EN: Total number of offsprings of unspecified gender.
            SK: Celkový počet potomkov neurčeného pohlavia.
        notes (TextField):
            EN: Additional notes about the breeding.
            SK: Dodatočné poznámky o chove.
    """

    breeder = models.ForeignKey(
        BreederProfile,
        on_delete=models.CASCADE,
        verbose_name="Chovateľ",
        help_text="Chovateľ a člen organizácie",
    )
    subspecies = models.ForeignKey(
        TaxonomySubspecies,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Poddruh",
        help_text="Poddruh, ktorý sa chová",
    )
    year = models.IntegerField(
        verbose_name="Rok", help_text="Rok, pre ktorý je záznam o chove"
    )
    number_of_males = models.PositiveIntegerField(
        default=0,
        verbose_name="Počet samcov",
        help_text="Počet samcov chovaného druhu/poddruhu",
    )
    number_of_females = models.PositiveIntegerField(
        default=0,
        verbose_name="Počet samíc",
        help_text="Počet samíc chovaného druhu/poddruhu",
    )
    number_of_males_offsprings = models.PositiveIntegerField(
        default=0,
        verbose_name="Počet samcov odchov",
        help_text="Počet samcov odchovaného druhu/poddruhu",
    )
    number_of_females_offsprings = models.PositiveIntegerField(
        default=0,
        verbose_name="Počet samíc odchov",
        help_text="Počet samíc odchovaného druhu/poddruhu",
    )
    number_of_unspecified_offsprings = models.PositiveIntegerField(
        default=0,
        verbose_name="Neurčený odchov",
        help_text="Počet kusov neurčeného pohlavia druhu/poddruhu",
    )
    notes = models.TextField(
        blank=True,
        null=True,
        verbose_name="Poznámky",
        help_text="Dodatočné poznámky o chove",
    )

    class Meta:
        verbose_name = "Záznam o chove"
        verbose_name_plural = "Záznamy o chove"

    @property
    def total_count_of_species(self):
        return self.number_of_males + self.number_of_females

    @property
    def total_count_offsprings(self):
        return (
            self.number_of_males_offsprings
            + self.number_of_females_offsprings
            + self.number_of_unspecified_offsprings
        )


class Project(SEOModel, TimeStampedModel, TaggableManager):
    """
    EN: Represents a specific project or initiative focused on breeding, including all related activities and members.
    SK: Reprezentuje konkrétny projekt alebo iniciatívu zameranú na chov, vrátane všetkých súvisiacich aktivít a členov.

    Attributes:
        name (CharField):
            EN: Full name of the project or initiative.
            SK: Plný názov projektu alebo iniciatívy.
        description (TextField):
            EN: Detailed description of the project including main goals and expected outcomes.
            SK: Detailný popis projektu vrátane hlavných cieľov a očakávaných výsledkov.
        start_date (DateField):
            EN: The date when the project starts.
            SK: Dátum začiatku realizácie projektu.
        end_date (DateField):
            EN: The anticipated end date of the project, which can be updated as the project progresses.
            SK: Predpokladaný dátum ukončenia projektu, ktorý môže byť aktualizovaný podľa priebehu projektu.
        member (ManyToManyField):
            EN: Breeders involved in the project.
            SK: Chovatelia zapojení do projektu.
        coordinator (ForeignKey):
            EN: The breeder responsible for leading and coordinating the project.
            SK: Chovateľ zodpovedný za vedenie a koordináciu projektu.
    """

    name = models.CharField(
        max_length=255,
        verbose_name="Názov projektu",
        help_text="Plný názov projektu alebo iniciatívy.",
    )
    description = models.TextField(
        blank=True,
        verbose_name="Popis projektu",
        help_text="Detailný popis projektu vrátane hlavných cieľov a očakávaných výsledkov.",
    )
    start_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Dátum začiatku",
        help_text="Dátum začiatku realizácie projektu.",
    )
    end_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Dátum ukončenia",
        help_text="Predpokladaný dátum ukončenia projektu. Môže byť aktualizovaný podľa priebehu projektu.",
    )
    member = models.ManyToManyField(
        BreederProfile,
        related_name="membered_projects",
        verbose_name="Členovia projektu",
        help_text="Chovatelia zapojení do projektu.",
    )
    coordinator = models.ForeignKey(
        BreederProfile,
        on_delete=models.CASCADE,
        related_name="coordinated_projects",
        verbose_name="Koordinátor projektu",
        help_text="Chovateľ zodpovedný za vedenie a koordináciu projektu.",
    )

    class Meta:
        verbose_name = "Projekt"
        verbose_name_plural = "Projekty"

    def __str__(self):
        return self.name
