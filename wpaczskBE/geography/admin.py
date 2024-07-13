from django.contrib import admin
from .models import Country, Location


class CountryAdmin(admin.ModelAdmin):
    list_display = ("country_info", "czech_name", "slovak_name")
    search_fields = ("country_info", "czech_name", "slovak_name")
    fieldsets = (
        (None, {"fields": ("country_info",)}),
        ("Names", {"fields": ("czech_name", "slovak_name")}),
    )


class LocationAdmin(admin.ModelAdmin):
    list_display = ("country", "latitude", "longitude")
    search_fields = ("country__country_info",)
    list_filter = ("country",)
    fieldsets = (
        (None, {"fields": ("country",)}),
        ("Coordinates", {"fields": ("latitude", "longitude")}),
    )


admin.site.register(Country, CountryAdmin)
admin.site.register(Location, LocationAdmin)
