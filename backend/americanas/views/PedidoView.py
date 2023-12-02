from rest_framework import viewsets
from rest_framework.views import APIView
from americanas.serializers import PedidoSerializers
from americanas.models import Pedido
from rest_framework.response import Response
from americanas.strategy.strategy import PagamentoCartaoStrategy, PagamentoGiftCardStrategy, PagamentoValeStrategy


class PedidoViewSets(viewsets.ModelViewSet):
    serializer_class = PedidoSerializers
    queryset = Pedido.objects.all()
    
    
class MeioPagamentoViewSets(APIView):
    def post(self, request, *args, **kwargs):
        try:
            # Tipo de estratégia (pode ser obtido a partir do request ou de outras fontes)
            tipo_estrategia = request.data
            # Cria um meio de pagamento com a estratégia escolhida
            if tipo_estrategia['tipo_estrategia'] == 'cartao':
                estrategia = PagamentoCartaoStrategy()
            elif tipo_estrategia['tipo_estrategia'] == 'vale':
                estrategia = PagamentoValeStrategy()
            elif tipo_estrategia['tipo_estrategia'] == 'giftcard':
                estrategia = PagamentoGiftCardStrategy()
            else:
                estrategia = PagamentoCartaoStrategy()
            dado = estrategia.processar_pagamento(tipo_estrategia['valor'])
            
            return Response(dado, status=201)
        except Exception as e:
            return Response({'message': str(e)}, status=400)