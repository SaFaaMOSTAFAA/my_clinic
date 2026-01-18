from rest_framework import serializers

from appointments.serializers import ListAppointmentSerializer
from visits.models import Visit


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = [
            'id',
            'appointment',
            'diagnosis',
            'prescription',
            'notes',
            'created_at',
        ]


class ListVisitSerializer(serializers.ModelSerializer):
    appointment = ListAppointmentSerializer()

    class Meta:
        model = Visit
        fields = [
            'id',
            'appointment',
            'diagnosis',
            'prescription',
            'notes',
            'created_at',
        ]
