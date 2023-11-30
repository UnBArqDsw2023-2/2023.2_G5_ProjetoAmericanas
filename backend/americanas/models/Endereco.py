from django.db import models
from abstract_factory import Base


class Endereco(Base):
    rua = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100)
    numero = models.IntegerField()
    estado = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'endereco'
        