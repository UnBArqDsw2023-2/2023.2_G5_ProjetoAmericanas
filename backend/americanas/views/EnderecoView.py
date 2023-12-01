from rest_framework import viewsets
from americanas.models import Endereco
from americanas.serializers import EnderecoSerializers


class EnderecoViewSets(viewsets.ModelViewSet):
    serializer_class = EnderecoSerializers
    queryset = Endereco.objects.all()