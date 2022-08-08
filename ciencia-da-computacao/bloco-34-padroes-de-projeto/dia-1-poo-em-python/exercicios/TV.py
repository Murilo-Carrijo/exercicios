class TV():
    def __init__(self, tamanho):
        self.__volume = 50
        self.__canal = 1
        self.__tamanho = tamanho
        self.__ligada = False
    
    def aumentar_volume(self):
        if self.__volume >= 99:
            self.__volume = 99
        else:
            self.__volume += 1

    def diminuir_volume(self):
        if self.__volume <= 0:
            self.__volume = 0
        else:
            self.__volume -= 1

    def modificar_canal(self, novo_canal):
        if 1 < self.__canal > 99 :
            raise ValueError("O canal está fora dos limites")
        else:
            self.__canal = novo_canal

    def ligar_desligar(self):
        if not self.__ligada:
            self.__ligada = True
        else:
            self.__ligada = False
