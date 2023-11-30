from rest_framework import viewsets
from americanas.models import EnderecoUsuario
from americanas.serializers import EnderecoUsuarioSerializer


class EnderecoUsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = EnderecoUsuarioSerializer
    queryset = EnderecoUsuario.objects.all()