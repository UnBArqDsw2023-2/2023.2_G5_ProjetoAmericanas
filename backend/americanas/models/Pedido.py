from django.db import models
from abstract_factory.base_model import Base
from americanas.models import Usuario


class Pedido(Base):
    data_pedido = models.DateField()
    status_pedido = models.CharField(max_length=100)
    detalhes_pedido = models.CharField(max_length=100)
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    estoque = models.IntegerField()
    produto = models.OneToOneField(Usuario, on_delete=models.CASCADE, db_column='id_usuario')
    
    class Meta:
        db_table = 'pedido'