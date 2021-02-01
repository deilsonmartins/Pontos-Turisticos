from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls.static import static
from core.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracaoViewSet
from comentarios.api.viewsets import ComentarioViewSet
from avaliacoes.api.viewsets import AvaliacaoViewSet
from enderecos.api.viewsets import EnderecoViewSet

router = routers.DefaultRouter()
router.register(r'pontosturisticos', PontoTuristicoViewSet, basename="PontoTuristico")
router.register(r'atracoes', AtracaoViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)
router.register(r'enderecos', EnderecoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token)
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
