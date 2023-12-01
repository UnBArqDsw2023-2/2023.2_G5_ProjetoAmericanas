from observer import Observer

class PromocaoObserver(Observer):
    def update(self, subject, *args, **kwargs):
        if "nova_promocao" in kwargs:
            nova_promocao = kwargs["nova_promocao"]
            self.notificar_promocao(nova_promocao)

    def notificar_promocao(self, promocao):
        # Lógica para notificar sobre uma nova promoção
        print(f"Nova promoção! {promocao.nome} com desconto de {promocao.desconto}%")
x