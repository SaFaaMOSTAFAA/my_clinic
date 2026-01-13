from rest_framework.routers import DefaultRouter

from users.apis import DoctorViewSet, PatientViewSet

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet, basename='doctor')
router.register(r'patients', PatientViewSet, basename='patient')

urlpatterns = router.urls
