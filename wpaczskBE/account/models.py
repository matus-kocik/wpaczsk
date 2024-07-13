from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models, transaction
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

from common_models.models import SEOModel, TimeStampedModel
from geography.models import Country

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

    def get_by_natural_key(self, email):
        return self.get(email=email)

class Profile(AbstractBaseUser, PermissionsMixin, SEOModel, TimeStampedModel):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(
        max_length=16,
        choices=[
            ("male", "Muž"),
            ("female", "Žena"),
            ("undefined", "Nedefinované"),
        ],
        default="undefined",
        verbose_name="Pohlavie",
        help_text="Pohlavie užívateľa.",
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(
        default=timezone.now,
        verbose_name="Dátum vytvorenia účtu",
        help_text="Dátum a čas, kedy bol vytvorený používateľský účet.",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    academic_title_prefix = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        verbose_name="Predpona akademického titulu",
        help_text="Akademický alebo profesijný titul pred menom, napr. 'Dr.', 'Prof.'",
    )
    academic_title_suffix = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        verbose_name="Prípona akademického titulu",
        help_text="Akademický alebo profesijný titul za menom, napr. 'PhD', 'MSc'",
    )
    mobile_phone = PhoneNumberField(
        blank=True,
        null=True,
        verbose_name="Mobilný telefón",
        help_text="Mobilné telefónne číslo užívateľa.",
    )
    address = models.CharField(
        max_length=64,
        blank=True,
        null=True,
        verbose_name="Adresa",
        help_text="Ulica a číslo domu užívateľa.",
    )
    city = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        verbose_name="Mesto",
        help_text="Mesto, kde užívateľ žije.",
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Krajina",
        help_text="Krajina, kde užívateľ žije.",
    )
    profile_picture = models.ImageField(
        upload_to="profile_pics/",
        blank=True,
        null=True,
        verbose_name="Profilový obrázok",
        help_text="Profilový obrázok užívateľa.",
    )
    website_url = models.URLField(
        blank=True,
        null=True,
        verbose_name="Webstránka",
        help_text="URL oficiálnej webstránky chovateľa.",
    )
    facebook_profile = models.URLField(
        blank=True,
        null=True,
        verbose_name="Facebook Profil",
        help_text="Odkaz na Facebook profil užívateľa.",
    )
    notes = models.TextField(
        blank=True,
        null=True,
        verbose_name="Poznámky",
        help_text="Interné poznámky o chovateľovi pre správu.",
    )
    email_verified = models.BooleanField(
        default=False,
        verbose_name="Email overený",
        help_text="Indikuje, či bol email užívateľa overený.",
    )

    objects = CustomUserManager()

    class Meta:
        verbose_name = "Užívateľ"
        verbose_name_plural = "Užívatelia"

    def __str__(self):
        return self.email

    def get_full_name(self):
        """
        EN: Returns the user's full name.
        SK: Vráti celé meno užívateľa.
        """
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        """
        EN: Returns the user's short name.
        SK: Vráti krátke meno užívateľa.
        """
        return self.first_name


class BreederProfile(SEOModel, TimeStampedModel):
    user = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
        verbose_name="Užívateľ",
        help_text="Profil užívateľa, ku ktorému je tento chovateľský profil priradený.",
    )
    registration_number = models.PositiveIntegerField(
        blank=True,
        null=True,
        unique=True,
        verbose_name="Registračné číslo",
        help_text="Unikátne registračné číslo chovateľa.",
    )

    ROLE_TYPE_CHOICES = [
        ("president", "Predseda"),
        ("vice_president", "Miestopredseda"),
        ("treasurer", "Pokladník"),
        ("registrar", "Registrátor"),
        ("web_admin", "Správca webu"),
        ("manager", "Jednatel"),
    ]
    role_type = models.CharField(
        max_length=24,
        choices=ROLE_TYPE_CHOICES,
        blank=True,
        null=True,
        verbose_name="Funkcia",
        help_text="Definovaná funkcia člena v organizácii.",
    )
    STATUS_TYPE_CHOICES = [("breeder", "Chovateľ"), ("honorary_member", "Čestný člen")]
    status_type = models.CharField(
        max_length=24,
        choices=STATUS_TYPE_CHOICES,
        blank=True,
        null=True,
        verbose_name="Status",
        help_text="Definovaný status člena v organizácii.",
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Chovateľ"
        verbose_name_plural = "Chovatelia"

    def save(self, *args, **kwargs):
        with transaction.atomic():
            if self._state.adding and not self.registration_number:
                super().save(*args, **kwargs)
                self.registration_number = str(self.id).zfill(3)
                super().save(update_fields=["registration_number"])
            else:
                super().save(*args, **kwargs)
