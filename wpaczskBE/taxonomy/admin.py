from django.contrib import admin
from .models import (
    TaxonomyKingdom,
    TaxonomyPhylum,
    TaxonomyClass,
    TaxonomySubclass,
    TaxonomyOrder,
    TaxonomyFamily,
    TaxonomySubfamily,
    TaxonomyGenus,
    TaxonomySpecies,
    TaxonomySubspecies,
)


class TaxonomyBaseAdmin(admin.ModelAdmin):
    """
    EN: Admin interface for managing taxonomy entities.
    SK: Administračné rozhranie na správu taxonomických entít.

    Attributes:
        list_display (tuple): Fields displayed in the list view of taxonomy entities.
            EN: Fields displayed in the list view.
            SK: Polia zobrazené v prehľade.
        list_filter (tuple): Fields used for filtering in the admin list view of taxonomy entities.
            EN: Fields used for filtering in the admin list view.
            SK: Polia používané na filtrovanie v prehľade admina.
    """

    list_display = (
        "latin_name",
        "czech_name",
        "slovak_name",
        "english_name",
        "german_name",
    )
    list_filter = (
        "latin_name",
        "czech_name",
        "slovak_name",
        "english_name",
        "german_name",
    )


@admin.register(TaxonomyKingdom)
class TaxonomyKingdomAdmin(TaxonomyBaseAdmin):
    pass


@admin.register(TaxonomyPhylum)
class TaxonomyPhylumAdmin(TaxonomyBaseAdmin):
    list_filter = TaxonomyBaseAdmin.list_filter + ("taxonomy_kingdom",)


@admin.register(TaxonomyClass)
class TaxonomyClassAdmin(TaxonomyBaseAdmin):
    list_filter = TaxonomyBaseAdmin.list_filter + ("taxonomy_phylum",)


@admin.register(TaxonomySubclass)
class TaxonomySubclassAdmin(TaxonomyBaseAdmin):
    list_filter = TaxonomyBaseAdmin.list_filter + ("taxonomy_class",)


@admin.register(TaxonomyOrder)
class TaxonomyOrderAdmin(TaxonomyBaseAdmin):
    list_filter = TaxonomyBaseAdmin.list_filter + ("subclass",)


@admin.register(TaxonomyFamily)
class TaxonomyFamilyAdmin(TaxonomyBaseAdmin):
    list_filter = TaxonomyBaseAdmin.list_filter + ("taxonomy_order",)


@admin.register(TaxonomySubfamily)
class TaxonomySubfamilyAdmin(TaxonomyBaseAdmin):
    list_filter = TaxonomyBaseAdmin.list_filter + ("taxonomy_family",)


@admin.register(TaxonomyGenus)
class TaxonomyGenusAdmin(TaxonomyBaseAdmin):
    list_filter = TaxonomyBaseAdmin.list_filter + ("taxonomy_subfamily",)


@admin.register(TaxonomySpecies)
class TaxonomySpeciesAdmin(TaxonomyBaseAdmin):
    list_filter = TaxonomyBaseAdmin.list_filter + ("taxonomy_genus",)


@admin.register(TaxonomySubspecies)
class TaxonomySubspeciesAdmin(TaxonomyBaseAdmin):
    """
    EN: Admin class for managing subspecies taxonomy.
    SK: Trieda admina na správu taxonómie poddruhov.

    Attributes:
        list_filter (tuple): A tuple of fields used for filtering the admin list view.
            EN: Fields used for filtering the admin list view.
            SK: Polia používané na filtrovanie zobrazenia v adminovi.
        fieldsets (tuple): A tuple of fieldsets used to organize fields in the admin interface.
            EN: Fieldsets used to organize fields in the admin interface.
            SK: Skupiny polí používané na usporiadanie polí v rozhraní admina.
    """

    list_filter = TaxonomyBaseAdmin.list_filter + ("taxonomy_species",)

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "latin_name",
                    "czech_name",
                    "slovak_name",
                    "english_name",
                    "german_name",
                )
            },
        ),
        ("Taxonomy", {"fields": ("taxonomy_species",)}),
        (
            "Additional Information",
            {
                "fields": (
                    "average_lifespan",
                    "biotop",
                    "description",
                    "habitat_countries",
                    "status_in_nature",
                    "status_in_captivity",
                    "maturity",
                    "length",
                    "weight",
                    "clutch",
                    "incubation",
                    "ring_size",
                    "population_in_czech_republic",
                    "breeding_difficulty",
                    "images",
                    "movies",
                    "movies_url",
                ),
                "classes": ("collapse",),
            },
        ),
    )
