from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from atracoes.models import Atracao
from .serializers import AtracaoSerializer

class AtracaoViewSet(ModelViewSet):

    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['idade_minima']