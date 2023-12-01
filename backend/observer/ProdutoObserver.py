from observer import Observer


class PromocaoObserver(Observer):
    def update(self, subject, *args, **kwargs):
        print("Update chamado")
        self.notificar_promocao(subject)

    def notificar_promocao(self, promocao):
        print("Notificar promoção chamado")
        # Lógica para notificar sobre uma nova promoção
        print(f"Nova promoção! {promocao.nome} com desconto de {promocao.desconto}%")
