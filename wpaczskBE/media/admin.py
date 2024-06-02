from django.contrib import admin
from .models import Image, Movie


class ImageAdmin(admin.ModelAdmin):
    """
    EN: Admin interface for managing images.
    SK: Administračné rozhranie na správu obrázkov.

    Attributes:
        list_display (tuple): Fields displayed in the list view of images.
            EN: Fields displayed in the list view.
            SK: Polia zobrazené v prehľade.
        search_fields (tuple): Fields included in the search functionality for images.
            EN: Fields included in the search functionality.
            SK: Polia zahrnuté do vyhľadávacej funkcionality.
        fieldsets (tuple): Groupings of fields displayed in the detail view of images.
            EN: Groupings of fields displayed in the detail view.
            SK: Skupiny polí zobrazené v detailnom prehľade.
    """

    list_display = ("title", "carousel", "created_at")
    search_fields = ("title",)
    fieldsets = (
        (None, {"fields": ("title", "carousel")}),
        ("Description", {"fields": ("description",)}),
        ("Image File", {"fields": ("image_file",)}),
    )


class MovieAdmin(admin.ModelAdmin):
    """
    EN: Admin interface for managing movies.
    SK: Administračné rozhranie na správu filmov.

    Attributes:
        list_display (tuple): Fields displayed in the list view of movies.
            EN: Fields displayed in the list view.
            SK: Polia zobrazené v prehľade.
        search_fields (tuple): Fields included in the search functionality for movies.
            EN: Fields included in the search functionality.
            SK: Polia zahrnuté do vyhľadávacej funkcionality.
        fieldsets (tuple): Groupings of fields displayed in the detail view of movies.
            EN: Groupings of fields displayed in the detail view.
            SK: Skupiny polí zobrazené v detailnom prehľade.
    """

    list_display = ("title", "created_at")
    search_fields = ("title",)
    fieldsets = (
        (None, {"fields": ("title",)}),
        ("Description", {"fields": ("description",)}),
        ("Movie File", {"fields": ("movie_file",)}),
    )


admin.site.register(Image, ImageAdmin)
admin.site.register(Movie, MovieAdmin)
