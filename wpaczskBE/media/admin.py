from django.contrib import admin
from .models import Image, Movie


class ImageAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title",)
    fieldsets = (
        (None, {"fields": ("title",)}),
        ("Description", {"fields": ("description",)}),
        ("Image File", {"fields": ("image_file",)}),
    )


class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title",)
    fieldsets = (
        (None, {"fields": ("title",)}),
        ("Description", {"fields": ("description",)}),
        ("Movie File", {"fields": ("movie_file",)}),
    )


admin.site.register(Image, ImageAdmin)
admin.site.register(Movie, MovieAdmin)
