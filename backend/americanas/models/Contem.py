from django.db import models
from template_method import Base
from americanas.models import Produto
from americanas.models import Pedido


class ContemProdutoPedido(Base):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

    class Meta:
        db_table = 'contem_produto_pedido'