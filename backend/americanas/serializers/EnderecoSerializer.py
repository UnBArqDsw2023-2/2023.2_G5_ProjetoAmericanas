from rest_framework import serializers
from americanas.models import Endereco

class EnderecoSerializers(serializers.ModelSerializer):
    rua = serializers.CharField(max_length=100)
    numero = serializers.IntegerField()
    complemento = serializers.CharField(max_length=100)
    cidade = serializers.CharField(max_length=100)
    estado = serializers.CharField(max_length=100)
    cep = serializers.CharField(max_length=100)
    
    class Meta:
        model = Endereco
        fields = '__all__'