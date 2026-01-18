from rest_framework import serializers

from appointments.models import Appointment
from users.serializers import DoctorSerializer, PatientSerializer


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


class ListAppointmentSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()
    patient = PatientSerializer()

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
