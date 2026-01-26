from rest_framework.viewsets import ModelViewSet

from users.models import Doctor, Patient
from users.serializers import DoctorSerializer, PatientSerializer


class DoctorViewSet(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class PatientViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
