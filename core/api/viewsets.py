from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):

    serializer_class = PontoTuristicoSerializer
    filterset_fields = ['aprovado']
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return PontoTuristico.objects.all()

    
    

