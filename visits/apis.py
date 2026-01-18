from rest_framework.viewsets import ModelViewSet

from visits.models import Visit
from visits.serializers import ListVisitSerializer, VisitSerializer


class VisitViewSet(ModelViewSet):
    queryset = Visit.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ListVisitSerializer
        return VisitSerializer
