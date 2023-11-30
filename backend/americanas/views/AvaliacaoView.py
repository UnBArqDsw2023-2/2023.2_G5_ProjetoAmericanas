from rest_framework import viewsets
from americanas.models import Avaliacao
from americanas.serializers import AvaliacaoSerializers


class AvaliacaoViewSets(viewsets.ModelViewSet):
    serializer_class = AvaliacaoSerializers
    queryset = Avaliacao.objects.all()