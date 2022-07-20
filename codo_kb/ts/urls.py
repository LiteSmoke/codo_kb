from rest_framework import routers
from .api import TsRecordViewSet

router = routers.DefaultRouter()
router.register('api/ts', TsRecordViewSet, 'ts')

urlpatterns = router.urls