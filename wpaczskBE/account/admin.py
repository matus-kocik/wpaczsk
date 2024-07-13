from django.contrib import admin

from .models import BreederProfile, Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "email_verified",
        "is_staff",
        "is_superuser",
    )
    search_fields = ("email", "first_name", "last_name")
    list_filter = ("is_superuser", "is_staff", "groups")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "gender",
                    "profile_picture",
                    "academic_title_prefix",
                    "academic_title_suffix",
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
                    "is_superuser",
                    "is_staff",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )


class BreederProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "registration_number", "status_type", "is_active")
    list_filter = ("status_type", "is_active")
    search_fields = ("user__email", "registration_number")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "user",
                    "registration_number",
                    "role_type",
                    "status_type",
                    "is_active",
                )
            },
        ),
    )


admin.site.register(Profile, ProfileAdmin)
admin.site.register(BreederProfile, BreederProfileAdmin)
