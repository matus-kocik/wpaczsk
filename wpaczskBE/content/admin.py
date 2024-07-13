from django.contrib import admin
from .models import Article, Event


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "publication_date", "author")
    search_fields = ("title", "author")
    list_filter = ("publication_date",)
    fieldsets = (
        (None, {"fields": ("title", "author", "info", "publication_date")}),
        ("Content", {"fields": ("pdf_file", "main_image", "description", "gallery")}),
    )


class EventAdmin(admin.ModelAdmin):
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
