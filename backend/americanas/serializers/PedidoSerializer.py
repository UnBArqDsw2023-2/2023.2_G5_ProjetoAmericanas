from rest_framework import serializers
from americanas.models.Pedido import Pedido


class PedidoSerializers(serializers.ModelSerializer):
    preco_total = serializers.DecimalField(max_digits=10, decimal_places=2)
    quantidade = serializers.IntegerField()
    estoque = serializers.IntegerField()
    detalhes_pedido = serializers.CharField(max_length=100)
    data_pedido = serializers.DateField()
    status_pedido = serializers.CharField(max_length=100)
    class Meta:
        model = Pedido
        fields = '__all__'