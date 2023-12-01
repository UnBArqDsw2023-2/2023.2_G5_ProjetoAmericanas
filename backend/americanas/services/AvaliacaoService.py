from americanas.models import CalculadoraMetrica
from americanas.models import MediaPonderadaStrategy


def calcular_metrica(self):
    # Crie uma instância da CalculadoraMetrica com a estratégia desejada
    calculadora = CalculadoraMetrica(MediaPonderadaStrategy())

    # Utilize a estratégia para calcular a métrica
    return calculadora.calcular(self)