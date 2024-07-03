from django.db import models

from common_models.models import SEOModel, TaggableManager, TimeStampedModel


class Image(SEOModel, TimeStampedModel, TaggableManager):
    """
    EN: Represents an image with a title, description, and file location. This model is used to manage images stored in the system.
    SK: Reprezentuje obrázok s názvom, popisom a umiestnením súboru. Tento model sa používa na správu obrázkov uložených v systéme.

    Attributes:
        title (CharField):
            EN: The title of the image.
            SK: Názov obrázka.
        description (TextField):
            EN: A brief description of the image.
            SK: Stručný popis obrázka.
        image_file (ImageField):
            EN: The file of the image stored in the system.
            SK: Súbor obrázka uloženého v systéme.
        carousel (BooleanField):
            EN: Indicates if the image should be displayed in the carousel.
            SK: Označuje, či by sa mal obrázok zobraziť v karuseli.
    """

    title = models.CharField(
        max_length=64, verbose_name="Názov obrázka", help_text="Názov obrázka"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Popis obrázka", help_text="Popis obrázka"
    )
    image_file = models.ImageField(
        upload_to="static/media/images/",
        verbose_name="Súbor obrázka",
        help_text="Súbor obrázka",
    )
    carousel = models.BooleanField(
        default=False, verbose_name="Karusel", help_text="Zobraziť v karuseli"
    )
    card_item = models.BooleanField(
        default=False, verbose_name="Obrázok karty", help_text="Obrázky pre karty"
    )
    gallery_item = models.BooleanField(
        default=False, verbose_name="Obrázok galérie", help_text="Obrázok do galérie"
    )
    template_name = models.CharField(
        max_length=64,
        blank=True,
        null=True,
        verbose_name="Názov šablóny",
        help_text="Názov šablóny",
    )
    card_title = models.CharField(
        max_length=128,
        blank=True,
        null=True,
        verbose_name="Názov karty",
        help_text="Názov pre kartu",
    )
    card_link = models.URLField(
        blank=True, null=True, verbose_name="Odkaz karty", help_text="Odkaz pre kartu"
    )
    subspecies = models.ForeignKey(
        "taxonomy.TaxonomySubspecies",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="images_subspecies",
        verbose_name="Poddruh",
        help_text="Poddruh pre tento obrázok",
    )
    species = models.ForeignKey(
        "taxonomy.TaxonomySpecies",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="images_species",
        verbose_name="Druh",
        help_text="Druh pre tento obrázok",
    )

    class Meta:
        verbose_name = "Obrázok"
        verbose_name_plural = "Obrázky"
        
    def __str__(self):
        return self.title

class Movie(SEOModel, TimeStampedModel, TaggableManager):
    """
    EN: Represents a movie with a title, description, and file location. This model is used to manage videos stored in the system.
    SK: Reprezentuje film s názvom, popisom a umiestnením súboru. Tento model sa používa na správu videí uložených v systéme.

    Attributes:
        title (CharField):
            EN: The title of the movie.
            SK: Názov filmu.
        description (TextField):
            EN: A brief description of the movie.
            SK: Stručný popis filmu.
        movie_file (FileField):
            EN: The file of the movie stored in the system.
            SK: Súbor filmu uloženého v systéme.
    """

    title = models.CharField(
        max_length=64, verbose_name="Názov filmu", help_text="Názov filmu"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Popis filmu", help_text="Popis filmu"
    )
    movie_file = models.FileField(
        upload_to="videos/", verbose_name="Súbor videa", help_text="Súbor videa"
    )
    gallery_item = models.BooleanField(
        default=False, verbose_name="Video galérie", help_text="Video do galérie"
    )
    subspecies = models.ForeignKey(
        "taxonomy.TaxonomySubspecies",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="movies_subspecies",
        verbose_name="Poddruh",
        help_text="Poddruh pre tento obrázok",
    )
    species = models.ForeignKey(
        "taxonomy.TaxonomySpecies",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="movies_species",
        verbose_name="Druh",
        help_text="Druh pre tento obrázok",
    )
    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videá"
        
    def __str__(self):
        return self.title