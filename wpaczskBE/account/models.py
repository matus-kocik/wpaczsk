from django.db import models, transaction
from django.contrib.auth.models import AbstractUser
from geography.models import Country
from phonenumber_field.modelfields import PhoneNumberField

class Profile(AbstractUser):
    mobile_phone = PhoneNumberField(blank=True, null=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=32, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Vytvorenie", help_text="Dátum a čas vytvorenia záznamu")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Aktualizácia", help_text="Dátum a čas poslednej aktualizácie")
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name="Zmazanie", help_text="Dátum a čas zmazania, ak ide o mäkké zmazanie")

    class Meta:
        verbose_name = 'Užívateľ'
        verbose_name_plural = 'Užívatelia'

class BreederProfile(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    registration_number = models.PositiveIntegerField(blank=True, null=True, unique=True)

    class Meta:
        verbose_name = 'Chovateľ'
        verbose_name_plural = 'Chovatelia'
        
    def save(self, *args, **kwargs):
        with transaction.atomic():
            if self._state.adding and not self.registration_number:
                super().save(*args, **kwargs) 
                self.registration_number = self.id
                super().save(update_fields=['registration_number'])
            else:
                super().save(*args, **kwargs)
