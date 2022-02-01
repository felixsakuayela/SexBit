from .views import PerfilViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'perfil', PerfilViewSet, basename='perfil-api')
urlpatterns = router.urls
