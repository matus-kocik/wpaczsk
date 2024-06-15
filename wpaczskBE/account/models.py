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
    """
    EN: Represents a user profile, extending the default Django user model, adding specific fields for more detailed user information.
    SK: Reprezentuje užívateľský profil, rozširujúci predvolený model užívateľa Django pridaním špecifických polí pre podrobnejšie informácie o užívateľovi.

    Attributes:
        email (EmailField):
            EN: The email address of the user (unique).
            SK: Emailová adresa užívateľa (unikátna).
        first_name (CharField):
            EN: The first name of the user.
            SK: Krstné meno užívateľa.
        last_name (CharField):
            EN: The last name of the user.
            SK: Priezvisko užívateľa.
        gender (CharField):
            EN: The gender of the user.
            SK: Pohlavie užívateľa.
        is_active (BooleanField):
            EN: Indicates whether the user account is active.
            SK: Indikuje, či je účet užívateľa aktívny.
        is_staff (BooleanField):
            EN: Indicates whether the user is a staff member.
            SK: Indikuje, či je užívateľ personál.
        date_joined (DateTimeField):
            EN: The date and time when the user account was created.
            SK: Dátum a čas vytvorenia účtu užívateľa.
        USERNAME_FIELD (str):
            EN: The field used as the unique identifier for the user (default is 'email').
            SK: Pole použité ako jedinečný identifikátor pre užívateľa (predvolené je 'email').
        REQUIRED_FIELDS (list):
            EN: A list of fields required when creating a user account.
            SK: Zoznam polí vyžadovaných pri vytváraní účtu užívateľa.
        academic_title_prefix (CharField):
            EN: The academic or professional title before the name, e.g., 'Dr.', 'Prof.'.
            SK: Akademický alebo profesijný titul pred menom, napr. 'Dr.', 'Prof.'.
        academic_title_suffix (CharField):
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
                self.registration_number = str(self.id).zfill(3)
                super().save(update_fields=["registration_number"])
            else:
                super().save(*args, **kwargs)
