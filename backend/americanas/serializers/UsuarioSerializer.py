from rest_framework import serializers
from americanas.models.Usuario import Usuario 


class UsuarioSerializar(serializers.Serializer):
    nome = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    senha = serializers.CharField(max_length=100)
    telefone = serializers.CharField(max_length=20)
    cpf = serializers.CharField(max_length=11)
    apelido = serializers.CharField(max_length=100)
    dt_nascimento = serializers.DateField()
    class Meta:
        model = Usuario
        fields = '__all__'
        