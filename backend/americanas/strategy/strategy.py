from abc import ABC, abstractmethod
from django.db import models

# Interface para a estratégia de pagamento
class MeioPagamentoStrategy(ABC):
    @abstractmethod
    def processar_pagamento(self, valor):
        pass

# Estratégia concreta para pagamento com cartão
class PagamentoCartaoStrategy(MeioPagamentoStrategy):
    def processar_pagamento(self, valor):
        # Lógica específica para pagamento com cartão
        print(f"Processando pagamento com cartão no valor de {valor}")
        return {'message': f'Processando pagamento com cartão no valor de {valor}'}

# Estratégia concreta para pagamento com vale
class PagamentoValeStrategy(MeioPagamentoStrategy):
    def processar_pagamento(self, valor):
        # Lógica específica para pagamento com vale
        print(f"Processando pagamento com vale no valor de {valor}")
        return {'message': f'Processando pagamento com vale no valor de {valor}'}

# Estratégia concreta para pagamento com gift card
class PagamentoGiftCardStrategy(MeioPagamentoStrategy):
    def processar_pagamento(self, valor):
        # Lógica específica para pagamento com gift card
        print(f"Processando pagamento com gift card no valor de {valor}")
        return {'message': f'Processando pagamento com gift card no valor de {valor}'}

