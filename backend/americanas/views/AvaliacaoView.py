from rest_framework import viewsets
from americanas.models import Avaliacao
from americanas.serializers import AvaliacaoSerializers
from strategy2 import CalculadoraMetrica, MediaPonderadaStrategy
from rest_framework.response import Response
from rest_framework.views import APIView

class AvaliacaoViewSets(viewsets.ModelViewSet):
    serializer_class = AvaliacaoSerializers
    queryset = Avaliacao.objects.all()
    
class AvaliacaoMetricasViewSets(APIView):
    def get(self, request, format=None):
        avaliacoes = Avaliacao.objects.all()
        calculadora = CalculadoraMetrica(MediaPonderadaStrategy())
        metricas = []
        for avaliacao in avaliacoes:
            metricas.append({ "Métricas da Avaliação": calculadora.calcular(avaliacao)})
        return Response(metricas)