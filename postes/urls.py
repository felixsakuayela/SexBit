from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('postar/<int:id>', views.poste, name='postar'),
    path('<int:id>', views.poste, name='postar_retorno'),
    path('', views.ver_poste, name='comentar_retorno'),
    path('poste/', views.listar_poste, name='allposte'),
    path('ver_poste/<int:id>', views.ver_poste, name='verposte'),
    path('ver_comentario/<int:id>', views.ver_comentario, name='vercomentario'),
    path('reac_forca/<int:id>', views.reac_forca, name='reacforca'),
    path('reac_corac/<int:id>', views.reac_corac, name='reaccorac'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)