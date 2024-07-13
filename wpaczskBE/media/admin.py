from django.contrib import admin
from .models import Image, Movie


class ImageAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "carousel", "card_item", "gallery_item", "created_at")
    list_filter = ("carousel", "card_item", "gallery_item")
    search_fields = ("title", "description")
    fieldsets = (
        (None, {"fields": ("title", "carousel", "card_item", "gallery_item", "species", "subspecies", "card_title", "card_link")}),
        ("Description", {"fields": ("description",)}),
        ("Image File", {"fields": ("image_file",)}),
    )


class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title",)
    fieldsets = (
        (None, {"fields": ("title", "species", "subspecies")}),
        ("Description", {"fields": ("description",)}),
        ("Movie File", {"fields": ("movie_file",)}),
    )


admin.site.register(Image, ImageAdmin)
admin.site.register(Movie, MovieAdmin)
