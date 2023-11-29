from rest_framework import serializers
from backend.americanas.models.Usuario import Usuario 


class UsuarioSerializar(serializers.Serializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        