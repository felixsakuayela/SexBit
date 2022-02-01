from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    #path('', views.comentar, name='comentar'),
    path('portal', views.portal, name='portal'),
    path('<int:id>', views.perfil, name='perfil'),
    path('sala/<int:id>', views.sala, name='sala'),
    path('follow/<int:id>', views.follow_user, name='follow'),
    path('usuario/sala-vip', views.salavip, name='salavip'),
    path('usuario/completar-perfil', views.novoperfil, name='novo-perfil'),
    path('usuario/editar-perfil', views.editarperfil, name='editar-perfil'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)