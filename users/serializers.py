from rest_framework import serializers

from users.models import Doctor, Patient


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = [
            'id',
            'username',
            'email',
            'phone',
            'specialization',
            'experience_years',
        ]


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            'id',
            'username',
            'email',
            'phone',
            'age',
            'medical_history',
        ]
