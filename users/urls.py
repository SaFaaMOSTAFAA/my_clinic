from django.urls import path
from rest_framework.routers import DefaultRouter

from users.views import DoctorViewSet, PatientViewSet, create_patient

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet, basename='doctor')
router.register(r'patients', PatientViewSet, basename='patient')

urlpatterns = router.urls

urlpatterns = [
    path('patients/create/', create_patient, name='create-patient'),
]
