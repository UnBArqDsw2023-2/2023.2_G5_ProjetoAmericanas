from rest_framework import serializers
from americanas.models import Produto

class ProdutoSerializers(serializers.ModelSerializer):
    categoria = serializers.CharField()
    nome = serializers.CharField()
    tipo = serializers.CharField()
    preco = serializers.DecimalField(max_digits=10, decimal_places=2)
    desconto = serializers.FloatField()
    class Meta:
        model = Produto
        fields = '__all__'