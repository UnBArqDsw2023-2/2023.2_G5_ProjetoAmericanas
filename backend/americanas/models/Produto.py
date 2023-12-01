from django.db import models
from abstract_factory import Base


class Produto(Base):
    categoria = models.CharField(max_length=255)
    nome = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    desconto = models.FloatField()
    class Meta:
        db_table = 'produto'