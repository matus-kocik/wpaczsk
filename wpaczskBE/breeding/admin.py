from django.contrib import admin

from breeding.models import BreedingRecord, Project


class BreedingRecordAdmin(admin.ModelAdmin):
    """
    EN: Admin interface for managing breeding records.
    SK: Administračné rozhranie na správu záznamov o chove.

    Attributes:
        list_display (tuple): Fields displayed in the list view of breeding records.
            EN: Fields displayed in the list view.
            SK: Polia zobrazené v prehľade.
        search_fields (tuple): Fields included in the search functionality for breeding records.
            EN: Fields included in the search functionality.
            SK: Polia zahrnuté do vyhľadávacej funkcionality.
        list_filter (tuple): Fields used for filtering breeding records in the list view.
            EN: Fields used for filtering in the list view.
            SK: Polia používané na filtrovanie v prehľade.
        fieldsets (tuple): Groupings of fields displayed in the detail view of breeding records.
            EN: Groupings of fields displayed in the detail view.
            SK: Skupiny polí zobrazené v detailnom prehľade.
    """

    list_display = (
        "breeder",
        "subspecies",
        "year",
        "total_count_of_species",
        "total_count_offsprings",
    )
    search_fields = (
        "breeder__user__email",
        "subspecies__name",
        "breeder__user__first_name",
        "breeder__user__last_name",
    )
    list_filter = ("year", "subspecies")
    fieldsets = (
        (None, {"fields": ("breeder", "subspecies", "year")}),
        (
            "Numbers",
            {
                "fields": (
                    "number_of_males",
                    "number_of_females",
                    "number_of_males_offsprings",
                    "number_of_females_offsprings",
                    "number_of_unspecified_offsprings",
                )
            },
        ),
        ("Notes", {"fields": ("notes",)}),
    )


class ProjectAdmin(admin.ModelAdmin):
    """
    EN: Admin interface for managing projects.
    SK: Administračné rozhranie na správu projektov.

    Attributes:
        list_display (tuple): Fields displayed in the list view of projects.
            EN: Fields displayed in the list view.
            SK: Polia zobrazené v prehľade.
        search_fields (tuple): Fields included in the search functionality for projects.
            EN: Fields included in the search functionality.
            SK: Polia zahrnuté do vyhľadávacej funkcionality.
        list_filter (tuple): Fields used for filtering projects in the list view.
            EN: Fields used for filtering in the list view.
            SK: Polia používané na filtrovanie v prehľade.
        filter_horizontal (tuple): Fields displayed in a horizontal filter widget.
            EN: Fields displayed in a horizontal filter widget.
            SK: Polia zobrazené vo vodorovnom widgete na filtrovanie.
    """

    list_display = ("name", "start_date", "end_date", "coordinator")
    search_fields = (
        "name",
        "coordinator__user__email",
        "coordinator__user__first_name",
        "coordinator__user__last_name",
    )
    list_filter = ("start_date", "end_date")
    filter_horizontal = ("member",)


admin.site.register(BreedingRecord, BreedingRecordAdmin)
admin.site.register(Project, ProjectAdmin)
