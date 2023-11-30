from rest_framework import serializers
from americanas.models.Pedido import Pedido


class PedidoSerializers(serializers.Serializer):
    id_pedido = serializers.IntegerField()
    id_usuario = serializers.IntegerField()
    id_produto = serializers.IntegerField()
    quantidade = serializers.IntegerField()
    valor_total = serializers.FloatField()
    data_pedido = serializers.DateField()
    status_pedido = serializers.CharField(max_length=100)
    
    class Meta:
        model = Pedido
        fields = '__all__'