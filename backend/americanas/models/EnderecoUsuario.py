from django.db import models
from abstract_factory import Base
from americanas.models import Usuario, Endereco


class EnderecoUsuario(Base):
    id_endereco = models.IntegerField()
    id_usuario = models.IntegerField()
    endereco_padrao = models.DecimalField(max_digits=10, decimal_places=2)
    usuario_id = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    endereco_id = models.OneToOneField(Endereco, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'endereco_usuario'