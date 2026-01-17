from django.db import models

from appointments.models import Appointment


class Visit(models.Model):
    appointment = models.OneToOneField(
        Appointment,
        on_delete=models.CASCADE,
        related_name='visit',
    )
    diagnosis = models.TextField()
    prescription = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Visit for appointment {self.appointment.id}'
