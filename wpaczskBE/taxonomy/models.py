from django.db import models

from geography.models import Country
from media.models import Image, Movie


class TaxonomyBase(models.Model):
    """
    EN: Abstract base class for taxonomy entities, providing common fields for naming in multiple languages and tracking the creation and modification times.
    SK: Abstraktná základná trieda pre taxonomické entity, poskytujúca spoločné polia pre pomenovanie v niekoľkých jazykoch a sledovanie času vytvorenia a úprav.

    Attributes:
        latin_name (CharField):
            EN: The original Latin name of the species.
            SK: Originálne latinské pomenovanie druhu.
        czech_name (CharField):
            EN: The original Czech name of the species.
            SK: Originálne české pomenovanie druhu.
        slovak_name (CharField):
            EN: The original Slovak name of the species, optional.
            SK: Originálne slovenské pomenovanie druhu, voliteľné.
        english_name (CharField):
            EN: The original English name of the species, optional.
            SK: Originálne anglické pomenovanie druhu, voliteľné.
        german_name (CharField):
            EN: The original German name of the species, optional.
            SK: Originálne nemecké pomenovanie druhu, voliteľné.
        created_at (DateTimeField), updated_at (DateTimeField), deleted_at (DateTimeField):
            EN: Standard fields for recording the timestamps of creation, updates, and potential soft deletion.
            SK: Štandardné polia pre záznam časových pečiatok vytvorenia, aktualizácií a potenciálneho mäkkého zmazania.
    """

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


class TaxonomyKingdom(TaxonomyBase):
    """
    EN: Represents a biological kingdom, one of the highest classification ranks in the biological taxonomy.
    SK: Reprezentuje biologickú ríšu, jeden z najvyšších klasifikačných stupňov v biologickej taxonómii.
    """

    class Meta:
        verbose_name = "Kingdom - Ríša"
        verbose_name_plural = "Kingdoms - Ríše"


class TaxonomyPhylum(TaxonomyBase):
    """
    EN: Represents a phylum in biological taxonomy, a rank below kingdom and above class.
    SK: Reprezentuje kmeň v biologickej taxonómii, stupeň nižšie ako ríša a vyššie ako trieda.
    """

    taxonomy_kingdom = models.ForeignKey(TaxonomyKingdom, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Phylum - Kmeň"
        verbose_name_plural = "Phyla - Kmene"


class TaxonomyClass(TaxonomyBase):
    """
    EN: Represents a class in biological taxonomy, a rank below phylum and above order.
    SK: Reprezentuje triedu v biologickej taxonómii, stupeň nižšie ako kmeň a vyššie ako rad.
    """

    taxonomy_phylum = models.ForeignKey(TaxonomyPhylum, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Class - Trieda"
        verbose_name_plural = "Classes - Triedy"


class TaxonomySubclass(TaxonomyBase):
    """
    EN: Represents a subclass in biological taxonomy, a rank below class and above order.
    SK: Reprezentuje podtriedu v biologickej taxonómii, stupeň nižšie ako trieda a vyššie ako rad.
    """

    taxonomy_class = models.ForeignKey(TaxonomyClass, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Subclass - Podtrieda"
        verbose_name_plural = "Subclasses - Podtriedy"


class TaxonomyOrder(TaxonomyBase):
    """
    EN: Represents an order in biological taxonomy, a rank below subclass and above family.
    SK: Reprezentuje rad v biologickej taxonómii, stupeň nižšie ako podtrieda a vyššie ako čeľaď.
    """

    subclass = models.ForeignKey(TaxonomySubclass, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Order - Rad"
        verbose_name_plural = "Orders - Rady"


class TaxonomyFamily(TaxonomyBase):
    """
    EN: Represents a family in biological taxonomy, a rank below order and above genus.
    SK: Reprezentuje čeľaď v biologickej taxonómii, stupeň nižšie ako rad a vyššie ako rod.
    """

    taxonomy_order = models.ForeignKey(TaxonomyOrder, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Family - Čeľaď"
        verbose_name_plural = "Families - Čeľade"


class TaxonomySubfamily(TaxonomyBase):
    """
    EN: Represents a subfamily in biological taxonomy, a rank below family and above genus.
    SK: Reprezentuje podčeľaď v biologickej taxonómii, stupeň nižšie ako čeľaď a vyššie ako rod.
    """

    taxonomy_family = models.ForeignKey(TaxonomyFamily, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Subfamily - Podčeľaď"
        verbose_name_plural = "Subfamilies - Podčeľade"


class TaxonomyGenus(TaxonomyBase):
    """
    EN: Represents a genus in biological taxonomy, a rank below subfamily and above species.
    SK: Reprezentuje rod v biologickej taxonómii, stupeň nižšie ako podčeľaď a vyššie ako druh.
    """

    taxonomy_subfamily = models.ForeignKey(TaxonomySubfamily, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Genus - Rod"
        verbose_name_plural = "Genera - Rody"


class TaxonomySpecies(TaxonomyBase):
    """
    EN: Represents a species in biological taxonomy, a rank below genus.
    SK: Reprezentuje druh v biologickej taxonómii, stupeň nižšie ako rod.
    """

    taxonomy_genus = models.ForeignKey(TaxonomyGenus, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Species - Druh"
        verbose_name_plural = "Species - Druhy"


class TaxonomySubspecies(TaxonomyBase):
    """
    EN: Represents a subspecies in biological taxonomy, a rank below species.
    SK: Reprezentuje poddruh v biologickej taxonómii, stupeň nižšie ako druh.
    """

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
        Image,
        related_name="subspecies",
        verbose_name="Obrázky",
        help_text="Obrázky súvisiace s poddruhom",
    )
    movies = models.ManyToManyField(
        Movie,
        related_name="subspecies",
        verbose_name="Videá",
        help_text="Videá súvisiace s poddruhom",
    )

    # TODO: url_video = (URLField): Link to a video associated with the species. // Odkaz na video súvisiace s druhom.
    # TODO: tag = (ManyToManyField to Tag): Tags associated with the species. // Značky priradené k druhu.
    # TODO: category = (ManyToManyField to Category): Categories associated with the species. // Kategórie priradené k druhu.
