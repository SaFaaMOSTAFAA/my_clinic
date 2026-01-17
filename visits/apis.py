from rest_framework.viewsets import ModelViewSet

from visits.models import Visit
from visits.serializers import VisitSerializer


class VisitViewSet(ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
