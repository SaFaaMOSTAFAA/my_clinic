from django.contrib import admin

from appointments.models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'doctor',
        'patient',
        'appointment_date',
        'status',
        'created_at',
    )

    list_filter = (
        'status',
        'appointment_date',
    )

    search_fields = (
        'doctor__full_name',
        'patient__full_name',
    )

