from django.contrib import admin

from breeding.models import BreedingRecord, Project


class BreedingRecordAdmin(admin.ModelAdmin):
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
