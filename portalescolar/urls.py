from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls')),
    path('', include('mensagens.urls')),
    path('', include('foto_de_perfil.urls')),
    path('', include('postes.urls')),
    path('', include('comentarios.urls')),
    path('', include('notificacao.urls')),
    path('usuarios/api/', include('usuarios.api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/api/', include('accounts.api.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
