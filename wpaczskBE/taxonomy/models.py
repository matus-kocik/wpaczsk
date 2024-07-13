from django.db import models

from common_models.models import SEOModel, TaggableManager, TimeStampedModel
from geography.models import Country


class TaxonomyBase(SEOModel, TimeStampedModel, TaggableManager):
    latin_name = models.CharField(
        max_length=64,
        verbose_name="Latinský názov",
        help_text="Originálne latinské pomenovanie",
    )
    czech_name = models.CharField(
        max_length=64,
        verbose_name="Český názov",
        help_text="Originálne české pomenovanie",
    )
    slovak_name = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        verbose_name="Slovenský názov",
        help_text="Originálne slovenské pomenovanie",
    )
    english_name = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        verbose_name="Anglický názov",
        help_text="Originálne anglické pomenovanie",
    )
    german_name = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        verbose_name="Nemecký názov",
        help_text="Originálne nemecké pomenovanie",
    )

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
        ("LC", "Málo dotknutý"),
        ("NT", "Takmer ohrozený"),
        ("VU", "Zraniteľný"),
        ("EN", "Ohrozený"),
        ("CR", "Kriticky ohrozený"),
        ("EW", "Vyhubený vo voľnej prírode"),
        ("EX", "Vyhubený"),
    ]
    average_lifespan = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Priemerná dĺžka života",
        help_text="Priemerná dĺžka života",
    )
    biotop = models.TextField(
        blank=True,
        null=True,
        verbose_name="Biotop",
        help_text="biotop, ktorý prevažne obýva, ekosystém krajiny, kde sa vyskytuje",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Popis",
        help_text="Popis, detailnejšie a podrobnejšie informácie",
    )
    habitat_countries = models.ManyToManyField(
        Country,
        blank=True,
        verbose_name="Krajiny",
        help_text="Krajiny, kde jedinec žije",
    )
    status_in_nature = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        choices=CONSERVATION_CHOICES,
        verbose_name="Stav v prírode",
        help_text="Stav ohrozenia jedincov v prírode podľa medzinárodných tabuliek",
    )
    status_in_captivity = models.TextField(
        blank=True,
        null=True,
        verbose_name="Stav v zajatí",
        help_text="Stav chovaných jedincov v zajatí, všeobecná informácia",
    )
    maturity = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        verbose_name="Dospelosť",
        help_text="Vek, v ktorom sú jedince dospelé",
    )
    length = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        verbose_name="Dĺžka",
        help_text="Dĺžka jedinca v cm/mm",
    )
    weight = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        verbose_name="Váha",
        help_text="Váha jedinca v kg/g",
    )
    clutch = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        verbose_name="Znáška",
        help_text="Znáška, počet znesených vajec",
    )
    incubation = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        verbose_name="Inkubácia",
        help_text="Doba inkubácie udáva, koľko dní trvá, kým sa z vajca vyliahne mláďa.",
    )
    ring_size = models.FloatField(
        blank=True,
        null=True,
        verbose_name="Veľkosť krúžku",
        help_text="Veľkosť krúžku v mm",
    )
    population_in_czech_republic = models.TextField(
        blank=True,
        null=True,
        verbose_name="Populácia v ČR a SVK",
        help_text="Populácia v ČR a SVK",
    )
    breeding_difficulty = models.TextField(
        blank=True,
        null=True,
        verbose_name="Náročnosť chovu",
        help_text="Náročnosť chovu",
    )
    images = models.ManyToManyField(
        'media.Image',
        blank=True,
        related_name="subspecies_image",
        verbose_name="Obrázky",
        help_text="Obrázky súvisiace s poddruhom",
    )
    movies = models.ManyToManyField(
        'media.Movie',
        blank=True,
        related_name="subspecies_movie",
        verbose_name="Videá",
        help_text="Videá súvisiace s poddruhom",
    )
    movies_url = models.URLField(
        blank=True,
        null=True,
        verbose_name="Odkaz na videá",
        help_text="Odkaz na videá súvisiace s poddruhom",
    )
