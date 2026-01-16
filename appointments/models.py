from django.db import models

from users.models import Doctor, Patient


class Appointment(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='appointments'
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='appointments'
    )
    appointment_date = models.DateTimeField()
    reason = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('scheduled', 'Scheduled'),
            ('completed', 'Completed'),
            ('canceled', 'Canceled')
        ],
        default='scheduled'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment of {self.patient.username} with Dr. {self.doctor.username} on {self.appointment_date}" # noqa
