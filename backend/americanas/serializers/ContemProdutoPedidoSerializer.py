from rest_framework import serializers
from americanas.models import ContemProdutoPedido


class ContemProdutoPedidoSerializers(serializers.ModelSerializer):
    produto = serializers.CharField()
    pedido = serializers.CharField()

    class Meta:
        model = ContemProdutoPedido
        fields = '__all__'