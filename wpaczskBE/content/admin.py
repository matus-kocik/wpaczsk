from django.contrib import admin
from .models import Article, Event


class ArticleAdmin(admin.ModelAdmin):
    """
    EN: Admin interface for managing articles.
    SK: Administračné rozhranie na správu článkov.

    Attributes:
        list_display (tuple): Fields displayed in the list view of articles.
            EN: Fields displayed in the list view.
            SK: Polia zobrazené v prehľade.
        search_fields (tuple): Fields included in the search functionality for articles.
            EN: Fields included in the search functionality.
            SK: Polia zahrnuté do vyhľadávacej funkcionality.
        list_filter (tuple): Fields used for filtering articles in the list view.
            EN: Fields used for filtering in the list view.
            SK: Polia používané na filtrovanie v prehľade.
        fieldsets (tuple): Groupings of fields displayed in the detail view of articles.
            EN: Groupings of fields displayed in the detail view.
            SK: Skupiny polí zobrazené v detailnom prehľade.
    """

    list_display = ("title", "publication_date", "author")
    search_fields = ("title", "author")
    list_filter = ("publication_date",)
    fieldsets = (
        (None, {"fields": ("title", "author", "info", "publication_date")}),
        ("Content", {"fields": ("pdf_file", "main_image", "description", "gallery")}),
    )


class EventAdmin(admin.ModelAdmin):
    """
    EN: Admin interface for managing events.
    SK: Administračné rozhranie na správu udalostí.

    Attributes:
        list_display (tuple): Fields displayed in the list view of events.
            EN: Fields displayed in the list view.
            SK: Polia zobrazené v prehľade.
        search_fields (tuple): Fields included in the search functionality for events.
            EN: Fields included in the search functionality.
            SK: Polia zahrnuté do vyhľadávacej funkcionality.
        list_filter (tuple): Fields used for filtering events in the list view.
            EN: Fields used for filtering in the list view.
            SK: Polia používané na filtrovanie v prehľade.
        fieldsets (tuple): Groupings of fields displayed in the detail view of events.
            EN: Groupings of fields displayed in the detail view.
            SK: Skupiny polí zobrazené v detailnom prehľade.
    """

    list_display = ("title", "date_from", "date_to", "location")
    search_fields = ("title", "location__name")
    list_filter = ("date_from", "location")
    fieldsets = (
        (
            None,
            {"fields": ("title", "info", "date_from", "date_to", "location", "url")},
        ),
        ("Content", {"fields": ("pdf_file", "main_image", "description", "gallery")}),
    )


admin.site.register(Article, ArticleAdmin)
admin.site.register(Event, EventAdmin)

# admin.site.register(Comment)
