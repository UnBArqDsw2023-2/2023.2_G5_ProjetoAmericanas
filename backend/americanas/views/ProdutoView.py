from rest_framework import viewsets, status
from rest_framework.response import Response
from americanas.models import Produto
from americanas.serializers import ProdutoSerializers
from observer.ProdutoObserver import PromocaoObserver

class ProdutoViewSets(viewsets.ModelViewSet):
    serializer_class = ProdutoSerializers
    queryset = Produto.objects.all()

    def perform_create(self, serializer):
        print("Perform create chamado")
        produto_instance = serializer.save()
        promocao_observer = PromocaoObserver()
        produto_instance.adicionar_promocao(nova_promocao=promocao_observer)
        promocao_observer.notificar_promocao(produto_instance)

        return Response(serializer.data, status=status.HTTP_201_CREATED)