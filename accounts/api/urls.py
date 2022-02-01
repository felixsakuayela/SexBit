from .views import UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', UserViewSet, basename='user-api')
urlpatterns = router.urls
