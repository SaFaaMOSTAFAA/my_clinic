from rest_framework.viewsets import ModelViewSet

from appointments.models import Appointment
from appointments.serializers import AppointmentSerializer, ListAppointmentSerializer


class AppointmentViewSet(ModelViewSet):
    queryset = Appointment.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ListAppointmentSerializer
        return AppointmentSerializer
