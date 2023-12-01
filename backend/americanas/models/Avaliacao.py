from django.db import models
from template_method import Base
from americanas.models import Produto


class Avaliacao(Base):
    titulo_avaliacao = models.CharField(max_length=255)
    comentario = models.CharField(max_length=255)
    nota = models.IntegerField()
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'avaliacao'
