from rest_framework import viewsets
from americanas.models import Produto
from americanas.serializers import ProdutoSerializers


class ProdutoViewSets(viewsets.ModelViewSet):
    serializer_class = ProdutoSerializers
    queryset = Produto.objects.all()