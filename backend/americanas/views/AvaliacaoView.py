from rest_framework import viewsets
from americanas.models import Avaliacao
from americanas.serializers import AvaliacaoSerializer


class AvaliacaoViewSets(viewsets.ModelViewSet):
    serializer_class = AvaliacaoSerializer
    queryset = Avaliacao.objects.all()