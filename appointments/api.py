from rest_framework.viewsets import ModelViewSet

from appointments.models import Appointment
from appointments.serializers import AppointmentSerializer


class AppointmentViewSet(ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
