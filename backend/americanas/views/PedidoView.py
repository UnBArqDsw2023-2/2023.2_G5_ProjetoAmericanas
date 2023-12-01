from rest_framework import status, viewsets
from americanas.serializers import PedidoSerializers
from americanas.models import Pedido


class PedidoViewSets(viewsets.ModelViewSet):
    serializer_class = PedidoSerializers
    queryset = Pedido.objects.all()
    
    