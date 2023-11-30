from django.db import models
from abstract_factory import Base

class Produto(Base):
    data_pedido = models.DateTimeField(auto_now_add=True)
    status_pedido = models.CharField(max_length=100)