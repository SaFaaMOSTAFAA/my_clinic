from rest_framework import serializers

from appointments.models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = [
            'id',
            'doctor',
            'patient',
            'appointment_date',
            'status',
            'created_at',
        ]
