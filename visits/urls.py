from rest_framework.routers import DefaultRouter

from visits.apis import VisitViewSet

router = DefaultRouter()
router.register(r'visit', VisitViewSet, basename='visit')

urlpatterns = router.urls
