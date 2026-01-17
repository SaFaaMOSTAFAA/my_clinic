from rest_framework import serializers

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
