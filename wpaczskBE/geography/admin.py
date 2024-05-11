from django.contrib import admin
from .models import Country, Location


class CountryAdmin(admin.ModelAdmin):
    """
    EN: Admin interface for managing countries.
    SK: Administračné rozhranie na správu krajín.

    Attributes:
        list_display (tuple): Fields displayed in the list view of countries.
            EN: Fields displayed in the list view.
            SK: Polia zobrazené v prehľade.
        search_fields (tuple): Fields included in the search functionality for countries.
            EN: Fields included in the search functionality.
            SK: Polia zahrnuté do vyhľadávacej funkcionality.
        fieldsets (tuple): Groupings of fields displayed in the detail view of countries.
            EN: Groupings of fields displayed in the detail view.
            SK: Skupiny polí zobrazené v detailnom prehľade.
    """

    list_display = ("country_info", "czech_name", "slovak_name")
    search_fields = ("country_info", "czech_name", "slovak_name")
    fieldsets = (
        (None, {"fields": ("country_info",)}),
        ("Names", {"fields": ("czech_name", "slovak_name")}),
    )


class LocationAdmin(admin.ModelAdmin):
    """
    EN: Admin interface for managing locations.
    SK: Administračné rozhranie na správu lokalít.

    Attributes:
        list_display (tuple): Fields displayed in the list view of locations.
            EN: Fields displayed in the list view.
            SK: Polia zobrazené v prehľade.
        search_fields (tuple): Fields included in the search functionality for locations.
            EN: Fields included in the search functionality.
            SK: Polia zahrnuté do vyhľadávacej funkcionality.
        list_filter (tuple): Fields used for filtering locations in the list view.
            EN: Fields used for filtering in the list view.
            SK: Polia používané na filtrovanie v prehľade.
        fieldsets (tuple): Groupings of fields displayed in the detail view of locations.
            EN: Groupings of fields displayed in the detail view.
            SK: Skupiny polí zobrazené v detailnom prehľade.
    """

    list_display = ("country", "latitude", "longitude")
    search_fields = ("country__country_info",)
    list_filter = ("country",)
    fieldsets = (
        (None, {"fields": ("country",)}),
        ("Coordinates", {"fields": ("latitude", "longitude")}),
    )


admin.site.register(Country, CountryAdmin)
admin.site.register(Location, LocationAdmin)
