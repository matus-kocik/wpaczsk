from django.db import models

class ClassificationBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Vytvorenie", help_text="Dátum a čas vytvorenia záznamu") # Record creation time. // Čas vytvorenia záznamu.
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Aktualizácia", help_text="Dátum a čas poslednej aktualizácie") # Record last update time. // Čas poslednej aktualizácie záznamu.
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name="Zmazanie", help_text="Dátum a čas zmazania") # Record deletion time, if soft deleted. // Čas zmazania záznamu, ak ide o mäkké zmazanie.
    
    class Meta:
        abstract = True

class Category(ClassificationBase):
    name = models.CharField(max_length=32, verbose_name="Názaov kategórie", help_text="Názov kategórie.")
    description = models.TextField(blank=True, null=True, verbose_name="Popis", help_text="Popis kategórie.")
    
    class Meta:
        verbose_name = "Kategória"
        verbose_name_plural = "Kategórie"

class Tag(ClassificationBase):
    name = models.CharField(max_length=32, verbose_name="Názov tagu", help_text="Názov tagu.")
    description = models.TextField(blank=True, null=True, verbose_name="Popis", help_text="Popis tagu.")
    
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tagy"

