from OO.carro_1.direcoes import TodasDirecoes


class Volante:
    def __init__(self):
        d = TodasDirecoes()
        self.__direcao = d.norte

    def virar_esquerda(self):
        self.__direcao = self.__direcao.esquerda

    def virar_direita(self):
        self.__direcao = self.__direcao.direita

    def mostra_direcao(self):
        return self.__direcao.atual
