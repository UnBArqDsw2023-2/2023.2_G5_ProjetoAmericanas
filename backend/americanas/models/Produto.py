from django.db import models
from abstract_factory import Base
from americanas.models import Usuario


class Produto(Base):
    data_pedido = models.DateTimeField(auto_now_add=True)
    status_pedido = models.CharField(max_length=100)
    detalhes_pedido = models.CharField(max_length=100)
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    estoque = models.IntegerField()
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'produto'