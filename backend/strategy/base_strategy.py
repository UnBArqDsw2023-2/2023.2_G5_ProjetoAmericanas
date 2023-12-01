from abc import ABC, abstractmethod
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
    
class MediaNotaStrategy(CalculoMetricaStrategy):
    def calcular_metrica(self, avaliacao, quantidade_avaliacoes):
        return avaliacao.nota / quantidade_avaliacoes

# Classe que utiliza a estratégia para calcular a métrica
class CalculadoraMetrica:
    def __init__(self, estrategia):
        self.estrategia = estrategia

    def calcular(self, avaliacao):
        return self.estrategia.calcular_metrica(avaliacao)
