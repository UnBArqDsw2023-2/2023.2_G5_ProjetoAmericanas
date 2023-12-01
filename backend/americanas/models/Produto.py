from django.db import models
from abstract_factory import Base

class Produto(Base):
    categoria = models.CharField(max_length=255)
    nome = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    desconto = models.FloatField()

    def adicionar_observer(self, observer):
        if not hasattr(self, '_observers'):
            self._observers = []
        self._observers.append(observer)

    def remover_observer(self, observer):
        if hasattr(self, '_observers'):
            self._observers.remove(observer)

    def notificar_observers(self, **kwargs):
        if hasattr(self, '_observers'):
            for observer in self._observers:
                observer.update(self, **kwargs)

    def adicionar_promocao(self, nova_promocao):
        # Lógica para adicionar uma nova promoção ao produto
        print("Adicionar promoção chamado")
        self.notificar_observers(nova_promocao=nova_promocao)

    class Meta:
        db_table = 'produto'
