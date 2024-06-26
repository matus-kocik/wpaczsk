# Generated by Django 5.0.4 on 2024-06-04 18:26

import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('geography', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Dátum a čas vytvorenia záznamu', null=True, verbose_name='Vytvorenie')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Dátum a čas poslednej aktualizácie', null=True, verbose_name='Aktualizácia')),
                ('deleted_at', models.DateTimeField(help_text='Dátum a čas zmazania, ak ide o mäkké zmazanie', null=True, verbose_name='Zmazanie')),
                ('meta_title', models.CharField(blank=True, help_text='Titulok stránky pre SEO.', max_length=255, null=True, verbose_name='Meta Titulok')),
                ('meta_description', models.TextField(blank=True, help_text='Popis stránky pre SEO.', null=True, verbose_name='Meta Popis')),
                ('meta_keywords', models.CharField(blank=True, help_text='Kľúčové slová pre SEO, oddeľované čiarkami.', max_length=255, null=True, verbose_name='Meta Kľúčové Slová')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('male', 'Muž'), ('female', 'Žena'), ('undefined', 'Nedefinované')], default='undefined', help_text='Pohlavie užívateľa.', max_length=16, verbose_name='Pohlavie')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, help_text='Dátum a čas, kedy bol vytvorený používateľský účet.', verbose_name='Dátum vytvorenia účtu')),
                ('academic_title_prefix', models.CharField(blank=True, help_text="Akademický alebo profesijný titul pred menom, napr. 'Dr.', 'Prof.'", max_length=32, null=True, verbose_name='Predpona akademického titulu')),
                ('academic_title_suffix', models.CharField(blank=True, help_text="Akademický alebo profesijný titul za menom, napr. 'PhD', 'MSc'", max_length=32, null=True, verbose_name='Prípona akademického titulu')),
                ('mobile_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Mobilné telefónne číslo užívateľa.', max_length=128, null=True, region=None, verbose_name='Mobilný telefón')),
                ('address', models.CharField(blank=True, help_text='Ulica a číslo domu užívateľa.', max_length=64, null=True, verbose_name='Adresa')),
                ('city', models.CharField(blank=True, help_text='Mesto, kde užívateľ žije.', max_length=32, null=True, verbose_name='Mesto')),
                ('profile_picture', models.ImageField(blank=True, help_text='Profilový obrázok užívateľa.', null=True, upload_to='profile_pics/', verbose_name='Profilový obrázok')),
                ('website_url', models.URLField(blank=True, help_text='URL oficiálnej webstránky chovateľa.', null=True, verbose_name='Webstránka')),
                ('facebook_profile', models.URLField(blank=True, help_text='Odkaz na Facebook profil užívateľa.', null=True, verbose_name='Facebook Profil')),
                ('notes', models.TextField(blank=True, help_text='Interné poznámky o chovateľovi pre správu.', null=True, verbose_name='Poznámky')),
                ('email_verified', models.BooleanField(default=False, help_text='Indikuje, či bol email užívateľa overený.', verbose_name='Email overený')),
                ('country', models.ForeignKey(blank=True, help_text='Krajina, kde užívateľ žije.', null=True, on_delete=django.db.models.deletion.CASCADE, to='geography.country', verbose_name='Krajina')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Užívateľ',
                'verbose_name_plural': 'Užívatelia',
            },
        ),
        migrations.CreateModel(
            name='BreederProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Dátum a čas vytvorenia záznamu', null=True, verbose_name='Vytvorenie')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Dátum a čas poslednej aktualizácie', null=True, verbose_name='Aktualizácia')),
                ('deleted_at', models.DateTimeField(help_text='Dátum a čas zmazania, ak ide o mäkké zmazanie', null=True, verbose_name='Zmazanie')),
                ('meta_title', models.CharField(blank=True, help_text='Titulok stránky pre SEO.', max_length=255, null=True, verbose_name='Meta Titulok')),
                ('meta_description', models.TextField(blank=True, help_text='Popis stránky pre SEO.', null=True, verbose_name='Meta Popis')),
                ('meta_keywords', models.CharField(blank=True, help_text='Kľúčové slová pre SEO, oddeľované čiarkami.', max_length=255, null=True, verbose_name='Meta Kľúčové Slová')),
                ('registration_number', models.PositiveIntegerField(blank=True, help_text='Unikátne registračné číslo chovateľa.', null=True, unique=True, verbose_name='Registračné číslo')),
                ('user_type', models.CharField(choices=[('member', 'Člen'), ('admin', 'Administrátor')], default='regular', help_text='Definuje typ užívateľa pre prístupové práva a funkcie.', max_length=16, verbose_name='Typ užívateľa')),
                ('role_type', models.CharField(blank=True, choices=[('president', 'Predseda'), ('vice_president', 'Miestopredseda'), ('treasurer', 'Pokladník'), ('registrar', 'Registrátor'), ('web_admin', 'Správca webu'), ('manager', 'Jednatel')], help_text='Definovaná funkcia člena v organizácii.', max_length=24, null=True, verbose_name='Funkcia')),
                ('status_type', models.CharField(blank=True, choices=[('breeder', 'Chovateľ'), ('honorary_member', 'Čestný člen')], help_text='Definovaný status člena v organizácii.', max_length=24, null=True, verbose_name='Status')),
                ('user', models.OneToOneField(help_text='Profil užívateľa, ku ktorému je tento chovateľský profil priradený.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Užívateľ')),
            ],
            options={
                'verbose_name': 'Chovateľ',
                'verbose_name_plural': 'Chovatelia',
            },
        ),
    ]
