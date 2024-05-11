from django.contrib import admin
from geography.models import Country, Location

class CountryAdmin(admin.ModelAdmin):
    """
    EN: Admin interface customization for the Country model.
        This configuration enhances the usability of the admin interface by adding
        display columns, search capability, and filters based on country properties.
    SK: Prispôsobenie administračného rozhrania pre model Country.
        Táto konfigurácia zlepšuje použiteľnosť administračného rozhrania pridaním
        stĺpcov zobrazenia, možností vyhľadávania a filtrov na základe vlastností krajiny.
    """
    list_display = ['country_info', 'czech_name', 'slovak_name']
    search_fields = ['country_info__name', 'czech_name', 'slovak_name']
    list_filter = ['country_info']

class LocationAdmin(admin.ModelAdmin):
    """
    EN: Admin interface customization for the Location model.
        This configuration includes essential fields such as country association
        and geographic coordinates in the list view, and allows filtering by country
        and searching by geographic details.
    SK: Prispôsobenie administračného rozhrania pre model Location.
        Táto konfigurácia zahrnuje základné polia, ako sú asociácie krajiny
        a geografické súradnice v zozname, a umožňuje filtrovanie podľa krajiny
        a vyhľadávanie podľa geografických detailov.
    """
    list_display = ['country', 'latitude', 'longitude']
    list_filter = ['country']
    search_fields = ['country__country_info__name', 'latitude', 'longitude']

admin.site.register(Country, CountryAdmin)
admin.site.register(Location, LocationAdmin)
