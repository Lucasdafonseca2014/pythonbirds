from OO.carro_2.direcoes import Direcoes


class Volante:

    def __init__(self):
        self.__direct = Direcoes()

    def virar_esquerda(self):
        self.__direct.esquerda()

    def virar_direita(self):
        self.__direct.direita()

    def mostra_direcao(self):
        return self.__direct.dir
