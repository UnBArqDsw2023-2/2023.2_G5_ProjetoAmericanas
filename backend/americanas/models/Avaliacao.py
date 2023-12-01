from abc import ABC
from django.db import models
from abstract_factory import Base
from americanas.models import Produto

# Interface para a estratégia de cálculo de métricas
class CalculoMetricaStrategy(ABC):
    @abstractmethod
    def calcular_metrica(self, avaliacao):
        pass

# Estratégia concreta para calcular a média ponderada
class MediaPonderadaStrategy(CalculoMetricaStrategy):
    def calcular_metrica(self, avaliacao):
        peso = 1  # Defina o peso conforme necessário
        return (avaliacao.nota * peso) / peso

# Classe que utiliza a estratégia para calcular a métrica
class CalculadoraMetrica:
    def __init__(self, estrategia):
        self.estrategia = estrategia

    def calcular(self, avaliacao):
        return self.estrategia.calcular_metrica(avaliacao)

# Modelo Avaliacao com o método calcular_metrica
class Avaliacao(Base):
    titulo_avaliacao = models.CharField(max_length=255)
    comentario = models.CharField(max_length=255)
    nota = models.IntegerField()
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'avaliacao'
