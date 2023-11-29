from django.db import models

from backend.abstract_factory.base_model import Base

# Create your models here.
class Usuario(Base):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11)
    apelido = models.CharField(max_length=100)
    dt_nascimento = models.DateField()

    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = 'usuario'