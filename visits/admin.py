from django.contrib import admin

from visits.models import Visit


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'appointment',
        'created_at',
    )

    search_fields = (
        'appointment__doctor__full_name',
        'appointment__patient__full_name',
    )

