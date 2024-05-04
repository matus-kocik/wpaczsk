from django.db import models
from geography.models import Country
from media.models import Image, Movie

class TaxonomyBase(models.Model):
    latin_name = models.CharField(max_length=64, verbose_name="Latinský názov", help_text="Originálne latinské pomenovanie") # Latin name of ... . // Latinský názov ... .
    czech_name = models.CharField(max_length=64, verbose_name="Český názov", help_text="Originálne české pomenovanie") # Czech name of ... . // Český názov ... .
    slovak_name = models.CharField(max_length=64, null=True, blank=True, verbose_name="Slovenský názov", help_text="Originálne slovenské pomenovanie") # Slovak name of .... // Slovenský názov ... .
    english_name = models.CharField(max_length=64, null=True, blank=True, verbose_name="Anglický názov", help_text="Originálne anglické pomenovanie") # English name of .... // Anglický názov ... .
    german_name = models.CharField(max_length=64, null=True, blank=True, verbose_name="Nemecký názov", help_text="Originálne nemecké pomenovanie") # German name of .... // Nemecký názov ... .
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Vytvorenie", help_text="Dátum a čas vytvorenia záznamu") # Record creation time. // Čas vytvorenia záznamu.
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Aktualizácia", help_text="Dátum a čas poslednej aktualizácie") # Record last update time. // Čas poslednej aktualizácie záznamu.
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name="Zmazanie", help_text="Dátum a čas zmazania") # Record deletion time, if soft deleted. // Čas zmazania záznamu, ak ide o mäkké zmazanie.
    
    class Meta:
        abstract = True
    
    def __str__(self):
        return self.latin_name 

class TaxonomyKingdom(TaxonomyBase):
    
    class Meta:
        verbose_name = "Kingdom - Ríša"
        verbose_name_plural = "Kingdoms - Ríše"

class TaxonomyPhylum(TaxonomyBase):
    taxonomy_kingdom = models.ForeignKey(TaxonomyKingdom, on_delete=models.DO_NOTHING)
    
    class Meta:
        verbose_name = "Phylum - Kmeň"
        verbose_name_plural = "Phyla - Kmene"
        
class TaxonomyClass(TaxonomyBase):
    taxonomy_phylum = models.ForeignKey(TaxonomyPhylum, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Class - Trieda"
        verbose_name_plural = "Classes - Triedy"
        
class TaxonomySubclass(TaxonomyBase):
    taxonomy_class = models.ForeignKey(TaxonomyClass, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Subclass - Podtrieda"
        verbose_name_plural = "Subclasses - Podtriedy"

class TaxonomyOrder(TaxonomyBase):
    subclass = models.ForeignKey(TaxonomySubclass, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Order - Rad"
        verbose_name_plural = "Orders - Rady"

class TaxonomyFamily(TaxonomyBase):
    taxonomy_order = models.ForeignKey(TaxonomyOrder, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Family - Čeľaď"
        verbose_name_plural = "Families - Čeľade"

class TaxonomySubfamily(TaxonomyBase):
    taxonomy_family = models.ForeignKey(TaxonomyFamily, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Subfamily - Podčeľaď"
        verbose_name_plural = "Subfamilies - Podčeľade"

class TaxonomyGenus(TaxonomyBase):
    taxonomy_subfamily = models.ForeignKey(TaxonomySubfamily, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Genus - Rod"
        verbose_name_plural = "Genera - Rody"

class TaxonomySpecies(TaxonomyBase):
    taxonomy_genus = models.ForeignKey(TaxonomyGenus, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Species - Druh"
        verbose_name_plural = "Species - Druhy"

class TaxonomySubspecies(TaxonomyBase):   
    taxonomy_species = models.ForeignKey(TaxonomySpecies, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Subspecies - Poddruh"
        verbose_name_plural = "Subspecies - Poddruhy"


    CONSERVATION_CHOICES = [
    ('LC', 'Málo dotknutý'),
    ('NT', 'Takmer ohrozený'),
    ('VU', 'Zraniteľný'),
    ('EN', 'Ohrozený'),
    ('CR', 'Kriticky ohrozený'),
    ('EW', 'Vyhubený vo voľnej prírode'),
    ('EX', 'Vyhubený'),
]   
    average_lifespan = models.IntegerField(blank=True, null=True, verbose_name="Priemerná dĺžka života", help_text="Priemerná dĺžka života") # Average lifespan of the species, subspecies. // Priemerná dĺžka života druhu, poddruhu.
    biotop = models.TextField(blank=True, null=True, verbose_name="Biotop", help_text="biotop, ktorý prevažne obýva, ekosystém krajiny, kde sa vyskytuje") # Biotop of the species, subspecies. // Biotop druhu, poddruhu.
    description = models.TextField(blank=True, null=True, verbose_name="Popis", help_text="Popis, detailnejšie a podrobnejšie informácie") # Description of the species, subspecies. // Popis druhu, poddruhu.
    habitat_countries = models.ManyToManyField(Country, blank=True, verbose_name="Krajiny", help_text="Krajiny, kde jedinec žije") # Countries of the species, subspecies. // Krajiny druhu, poddruhu.
    status_in_nature = models.CharField(max_length=32, blank=True, null=True, choices=CONSERVATION_CHOICES, verbose_name="Stav v prírode", help_text="Stav ohrozenia jedincov v prírode podľa medzinárodných tabuliek") # Conservation status in nature. // Stav ochrany v prírode.
    status_in_captivity = models.TextField(blank=True, null=True, verbose_name="Stav v zajatí", help_text="Stav chovaných jedincov v zajatí, všeobecná informácia") # Conservation status in captivity. // Stav ochrany v zajatí.
    maturity = models.CharField(max_length=32, blank=True, null=True, verbose_name="Dospelosť", help_text="Vek, v ktorom sú jedince dospelé") # Age of maturity. // Dospelosť.
    length = models.CharField(max_length=32, blank=True, null=True, verbose_name="Dĺžka", help_text="Dĺžka jedinca v cm/mm") # Length of the species, subspecies. // Dĺžka druhu, poddruhu.
    weight = models.CharField(max_length=32, blank=True, null=True, verbose_name="Váha", help_text="Váha jedinca v kg/g") # Weight of the species, subspecies. // Hmotnosť druhu, poddruhu.
    clutch = models.CharField(max_length=32, blank=True, null=True, verbose_name="Znáška", help_text="Znáška, počet znesených vajec") # Clutch size. // Snáška.
    incubation = models.CharField(max_length=32, blank=True, null=True, verbose_name="Inkubácia", help_text="Doba inkubácie udáva, koľko dní trvá, kým sa z vajca vyliahne mláďa.") # Incubation period. // Inkubácia.
    ring_size = models.FloatField(blank=True, null=True, verbose_name="Veľkosť krúžku", help_text="Veľkosť krúžku v mm") # Ring size. // Veľkosť kroužku. (ForeignKey to Ring Size): Reference to a ring size. // Referencia na veľkosť kružku.
    population_in_czech_republic = models.TextField(blank=True, null=True, verbose_name="Populácia v ČR a SVK", help_text="Populácia v ČR a SVK") # Population in the Czech Republic and Slovak Republic. // Populácia v Českej Republike a v Slovenskej Republike.
    breeding_difficulty = models.TextField(blank=True, null=True, verbose_name="Náročnosť chovu", help_text="Náročnosť chovu") # Difficulty of breeding. // Náročnosť chovu.
    images = models.ManyToManyField(Image, related_name='subspecies', verbose_name="Obrázky", help_text="Obrázky súvisiace s poddruhom")
    movies = models.ManyToManyField(Movie, related_name='subspecies', verbose_name="Videá", help_text="Videá súvisiace s poddruhom")

    #TODO: url_video = (URLField): Link to a video associated with the species. // Odkaz na video súvisiace s druhom.
    #TODO: tag = (ManyToManyField to Tag): Tags associated with the species. // Značky priradené k druhu.
    #TODO: category = (ManyToManyField to Category): Categories associated with the species. // Kategórie priradené k druhu.