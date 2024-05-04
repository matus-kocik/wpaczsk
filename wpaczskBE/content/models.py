from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from geography.models import Location
from account.models import Profile

class ContentBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Vytvorenie", help_text="Dátum a čas vytvorenia záznamu") # Record creation time. // Čas vytvorenia záznamu.
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Aktualizácia", help_text="Dátum a čas poslednej aktualizácie") # Record last update time. // Čas poslednej aktualizácie záznamu.
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name="Zmazanie", help_text="Dátum a čas zmazania") # Record deletion time, if soft deleted. // Čas zmazania záznamu, ak ide o mäkké zmazanie.
    
    class Meta:
        abstract = True

class Article(ContentBase):
    title = models.CharField(max_length=128, verbose_name="Titulok článku", help_text="Zadajte titulok článku.") # Title of the article. // Titulok článku.
    pdf_file = models.FileField(upload_to='articles/', verbose_name="PDF súbor článku", help_text="Nahrajte PDF súbor článku.") # Link to the article's PDF file. // Odkaz na PDF súbor článku.
    main_image = models.ImageField(upload_to='article_image/', blank=True, null=True, verbose_name="Titulný obrázok", help_text="Nahrajte hlavný obrázok článku, ak je k dispozícii.") # Main image of article // Titulný obrázok článku
    publication_date = models.DateField(verbose_name="Dátum publikácie článku", help_text="Zadajte dátum publikácie článku.") # Date of article publication. // Dátum publikácie článku.
    # TODO Riesit vyber alebo napisanie mena ... author = models.CharField(max_length=128, verbose_name="Autor článku", help_text="Zadajte meno autora článku.") # Reference to the article's author. // Odkaz na autora článku.
    info = models.CharField(max_length=128, blank=True, null=True, verbose_name="Krátke info k článku", help_text="Zadajte krátky popis alebo informácie o článku.") # Short info of article // Krátke info o článku
    # TODO description = models.TextField() ...
    # TODO gallery = models.ManytoManyFields(Image)...

    class Meta:
        verbose_name = 'Článok'
        verbose_name_plural = 'Články'
        
    def __str__(self):
        return self.title
        
class Event(ContentBase):
    title = models.CharField(max_length=128, verbose_name="Titulok udalosti", help_text="Zadajte titulok udalosti.") # Title of the event. // Titulok udalosti.
    pdf_file = models.FileField(upload_to='events/', blank=True, null=True, verbose_name="PDF súbor udalosti", help_text="Nahrajte PDF súbor udalosti, ak je k dispozícii.") # Link to the event's PDF file. // Odkaz na PDF súbor udalosti.
    main_image = models.ImageField(upload_to='event_image/', blank=True, null=True, verbose_name="Titulný obrázok", help_text="Nahrajte hlavný obrázok udalosti, ak je k dispozícii.") # Main image of event // Titulný obrázok udalosti
    date_from = models.DateField(verbose_name="Dátum začiatku udalosti", help_text="Zadajte dátum začiatku udalosti.") # Start date of the event. // Dátum začiatku udalosti.
    date_to = models.DateField(verbose_name="Dátum ukončenia udalosti", help_text="Zadajte dátum ukončenia udalosti.") # End date of the event. // Dátum konca udalosti.
    url = models.URLField(blank=True, null=True, verbose_name="url odkaz na udalosť", help_text="Zadajte webový odkaz s informáciami o udalosti.") # Web link with information about the event. // Webový odkaz s informáciami o udalosti.
    info = models.CharField(max_length=128, blank=True, null=True, verbose_name="Krátke info k udalosti", help_text="Zadajte krátky popis alebo informácie o udalosti.") # Short info of event // Krátke info o článku
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, verbose_name="Miesto udalosti", help_text="Vyberte lokáciu, kde sa udalosť koná.") # Reference to the Location model. // Odkaz na model.
    # TODO description = models.TextField() ...
    # TODO gallery = models.ManytoManyFields(Image)...

    class Meta:
        verbose_name = 'Udalosť'
        verbose_name_plural = 'Udalosti'

    def __str__(self):
        return self.title
        
class Comment(ContentBase):
    title = models.CharField(max_length=128, blank=True, null=True, verbose_name="Titulok komentára", help_text="Zadajte titulok komentára.") # Title of the comment. // Titulok komentára.
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="Užívateľ", help_text="Vyberte užívateľa, ktorý komentár pridal.")
    content_type= models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name="Typ obsahu", help_text="Vyberte typ obsahu, ku ktorému je komentár priradený.")
    object_id = models.PositiveIntegerField(verbose_name="ID objektu", help_text="Zadajte ID objektu, ku ktorému je komentár priradený.")
    content_object = GenericForeignKey('content_type', 'object_id')
    comment = models.TextField(verbose_name="Text komentára", help_text="Zadajte text komentára.")

    class Meta:
        verbose_name = "Komentár"
        verbose_name_plural = "Komentáre"
    
    def __str__(self):
        return self.title
