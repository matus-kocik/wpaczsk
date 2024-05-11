from django.contrib import admin

from .models import BreederProfile, Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "is_staff", "email_verified")
    search_fields = ("email", "first_name", "last_name")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "profile_picture",
                    "prefix_academic_title",
                    "suffix_academic_title",
                    "mobile_phone",
                    "address",
                    "city",
                    "country",
                    "website_url",
                    "facebook_profile",
                    "notes",
                    "email_verified",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )


class BreederProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "registration_number", "status_type")
    list_filter = ("status_type", "user__is_staff")
    search_fields = ("user__email", "registration_number")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "user",
                    "registration_number",
                    "user_type",
                    "role_type",
                    "status_type",
                )
            },
        ),
    )


admin.site.register(Profile, ProfileAdmin)
admin.site.register(BreederProfile, BreederProfileAdmin)
