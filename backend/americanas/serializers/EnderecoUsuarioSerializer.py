from  rest_framework import serializers
from americanas.models import EnderecoUsuario


class EnderecoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnderecoUsuario
        fields = '__all__'