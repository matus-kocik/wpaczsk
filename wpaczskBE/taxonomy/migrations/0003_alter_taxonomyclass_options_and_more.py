# Generated by Django 5.0.4 on 2024-05-01 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0002_remove_taxonomyspecies_average_lifespan_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taxonomyclass',
            options={'verbose_name': 'Class - Trieda', 'verbose_name_plural': 'Triedy'},
        ),
        migrations.AlterModelOptions(
            name='taxonomyfamily',
            options={'verbose_name': 'Family - Čeľaď', 'verbose_name_plural': 'Čeľade'},
        ),
        migrations.AlterModelOptions(
            name='taxonomygenus',
            options={'verbose_name': 'Genus - Rod', 'verbose_name_plural': 'Rody'},
        ),
        migrations.AlterModelOptions(
            name='taxonomykingdom',
            options={'verbose_name': 'Kingdom - Ríša', 'verbose_name_plural': 'Ríše'},
        ),
        migrations.AlterModelOptions(
            name='taxonomyorder',
            options={'verbose_name': 'Order - Rad', 'verbose_name_plural': 'Rady'},
        ),
        migrations.AlterModelOptions(
            name='taxonomyphylum',
            options={'verbose_name': 'Phylum - Kmeň', 'verbose_name_plural': 'Kmene'},
        ),
        migrations.AlterModelOptions(
            name='taxonomyspecies',
            options={'verbose_name': 'Species - Druh', 'verbose_name_plural': 'Druhy'},
        ),
        migrations.AlterModelOptions(
            name='taxonomysubclass',
            options={'verbose_name': 'Subclass - Podtrieda', 'verbose_name_plural': 'Podtriedy'},
        ),
        migrations.AlterModelOptions(
            name='taxonomysubfamily',
            options={'verbose_name': 'Subfamily - Podčeľaď', 'verbose_name_plural': 'Podčeľade'},
        ),
        migrations.AlterModelOptions(
            name='taxonomysubspecies',
            options={'verbose_name': 'Subspecies - Poddruh', 'verbose_name_plural': 'Poddruhy'},
        ),
    ]