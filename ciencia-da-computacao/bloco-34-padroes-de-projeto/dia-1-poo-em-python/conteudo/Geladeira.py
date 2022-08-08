from conteudo.Eletrodomestico import Eletrodomestico

class Geladeira(Eletrodomestico):
    def __init__(self, cor, potencia, voltagem, preco):
        super().__init__(cor, potencia, voltagem, preco)