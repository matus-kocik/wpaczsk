from django.contrib.auth.models import AbstractUser
from django.db import models, transaction
from phonenumber_field.modelfields import PhoneNumberField

from common_models.models import SEOModel, TimeStampedModel
from geography.models import Country


class Profile(AbstractUser, SEOModel, TimeStampedModel):
    """
    EN: Represents a user profile, extending the default Django user model, adding specific fields for more detailed user information.
    SK: Reprezentuje užívateľský profil, rozširujúci predvolený model užívateľa Django pridaním špecifických polí pre podrobnejšie informácie o užívateľovi.

    Attributes:
        prefix_academic_title (CharField):
            EN: The academic or professional title before the name, e.g., 'Dr.', 'Prof.'.
            SK: Akademický alebo profesijný titul pred menom, napr. 'Dr.', 'Prof.'.
        suffix_academic_title (CharField):
            EN: The academic or professional title after the name, e.g., 'PhD', 'MSc'.
            SK: Akademický alebo profesijný titul za menom, napr. 'PhD', 'MSc'.
        mobile_phone (PhoneNumberField):
            EN: The mobile phone number of the user.
            SK: Mobilné telefónne číslo užívateľa.
        address (CharField):
            EN: The user's street address.
            SK: Ulica a číslo domu užívateľa.
        city (CharField):
            EN: The city where the user resides.
            SK: Mesto, kde užívateľ žije.
        country (ForeignKey):
            EN: The country of the user's residence, linked to the Country model.
            SK: Krajina, kde užívateľ žije, prepojená s modelom Country.
        profile_picture (ImageField):
            EN: User's profile picture.
            SK: Profilový obrázok užívateľa.
        website_url (URLField):
            EN: URL of the user's official website.
            SK: URL oficiálnej webstránky užívateľa.
        facebook_profile (URLField):
            EN: Link to the user's Facebook profile.
            SK: Odkaz na Facebook profil užívateľa.
        notes (TextField):
            EN: Internal notes about the user for administrative purposes.
            SK: Interné poznámky o užívateľovi pre administratívne účely.
        email_verified (BooleanField):
            EN: Indicates whether the user's email has been verified.
            SK: Indikuje, či bol email užívateľa overený.
    """

    prefix_academic_title = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        verbose_name="Predpona titulu",
        help_text="Akademický alebo profesijný titul pred menom, napr. 'Dr.', 'Prof.'",
    )
    suffix_academic_title = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        verbose_name="Prípona titulu",
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

    class Meta:
        verbose_name = "Užívateľ"
        verbose_name_plural = "Užívatelia"


class BreederProfile(SEOModel, TimeStampedModel):
    """
    EN: Represents a breeder's profile linked to a user profile, including detailed information specific to breeders.
    SK: Reprezentuje profil chovateľa prepojený s užívateľským profilom, vrátane detailných informácií špecifických pre chovateľov.

    Attributes:
        user (OneToOneField):
            EN: The associated user profile.
            SK: Asociovaný užívateľský profil.
        registration_number (PositiveIntegerField):
            EN: Unique registration number of the breeder, automatically assigned upon creation.
            SK: Unikátne registračné číslo chovateľa, automaticky pridelené pri vytvorení.
        user_type (CharField):
            EN: Defines the user's type for access rights and functionalities.
            SK: Definuje typ užívateľa pre prístupové práva a funkcie.
        role_type (CharField):
            EN: Defined role of the member within the organization.
            SK: Definovaná funkcia člena v organizácii.
        status_type (CharField):
            EN: Defined status of the member within the organization.
            SK: Definovaný status člena v organizácii.
    """

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
    USER_TYPE_CHOICES = [
        ("member", "Člen"),
        ("admin", "Administrátor"),
    ]
    user_type = models.CharField(
        max_length=16,
        choices=USER_TYPE_CHOICES,
        default="regular",
        verbose_name="Typ užívateľa",
        help_text="Definuje typ užívateľa pre prístupové práva a funkcie.",
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

    class Meta:
        verbose_name = "Chovateľ"
        verbose_name_plural = "Chovatelia"

    def save(self, *args, **kwargs):
        """
        EN: Overrides the save method to assign a unique registration number if it's not provided.
        SK: Prepisuje metódu save pre priradenie unikátneho registračného čísla, ak nie je zadané.

        EN: If the object is being added for the first time and no registration number is provided,
        it automatically assigns the ID as the registration number with leading zeros.
        SK: Ak je objekt pridávaný prvýkrát a registračné číslo nie je poskytnuté,
        automaticky priradí ID ako registračné číslo s vedúcimi nulami.

        EN: It ensures that the saving operation is performed atomically.
        This means that either all changes are saved, or none of them are.
        In case of any error during the save operation, the changes are rolled back to maintain consistency.

        SK: Zabezpečuje, že operácia ukladania sa vykonáva atomicky.
        To znamená, že sa buď všetky zmeny uložia, alebo žiadna z nich.
        V prípade akéhokoľvek chybného stavu počas operácie ukladania sa zmeny vrátia späť, aby sa udržala konzistencia.

        """
        with transaction.atomic():
            if self._state.adding and not self.registration_number:
                super().save(*args, **kwargs)
                self.registration_number = str(self.id).zfill(3)  # Add zeros
                super().save(update_fields=["registration_number"])
            else:
                super().save(*args, **kwargs)
