from django.contrib import admin

from .models import BreederProfile, Profile


class ProfileAdmin(admin.ModelAdmin):
    """
    EN: Admin class for managing user profiles.
    SK: Trieda admina na správu používateľských profilov.

    Attributes:
        list_display (tuple): A tuple of model fields displayed in the admin list view.
            EN: Fields displayed in the admin list view.
            SK: Polia zobrazené v prehľade admina.
        search_fields (tuple): A tuple of fields used for searching in the admin interface.
            EN: Fields used for searching in the admin interface.
            SK: Polia používané na vyhľadávanie v rozhraní admina.
        list_filter (tuple): A tuple of fields used for filtering the admin list view.
            EN: Fields used for filtering the admin list view.
            SK: Polia používané na filtrovanie zobrazenia v adminovi.
        fieldsets (tuple): A tuple of fieldsets used to organize fields in the admin interface.
            EN: Fieldsets used to organize fields in the admin interface.
            SK: Skupiny polí používané na usporiadanie polí v rozhraní admina.
    """

    list_display = ("first_name", "last_name", "email", "email_verified", "is_staff", "is_superuser")
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
    """
    EN: Admin class for managing breeder profiles.
    SK: Trieda admina na správu profilov chovateľov.

    Attributes:
        list_display (tuple): A tuple of model fields displayed in the admin list view.
            EN: Fields displayed in the admin list view.
            SK: Polia zobrazené v prehľade admina.
        list_filter (tuple): A tuple of fields used for filtering the admin list view.
            EN: Fields used for filtering the admin list view.
            SK: Polia používané na filtrovanie zobrazenia v adminovi.
        search_fields (tuple): A tuple of fields used for searching in the admin interface.
            EN: Fields used for searching in the admin interface.
            SK: Polia používané na vyhľadávanie v rozhraní admina.
        fieldsets (tuple): A tuple of fieldsets used to organize fields in the admin interface.
            EN: Fieldsets used to organize fields in the admin interface.
            SK: Skupiny polí používané na usporiadanie polí v rozhraní admina.
    """

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
                    "user_type",
                    "role_type",
                    "status_type",
                    "is_active",
                )
            },
        ),
    )


admin.site.register(Profile, ProfileAdmin)
admin.site.register(BreederProfile, BreederProfileAdmin)
