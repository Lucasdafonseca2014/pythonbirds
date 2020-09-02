from OO.carro_2.motor import Motor
from OO.carro_2.volante import Volante


class Carro:
    def __init__(self, modelo='Gol', cor='Prata'):
        self.cor = cor
        self.modelo = modelo
        self.__motor = Motor()
        self.__volante = Volante()

    def acelerar(self):
        self.__motor.acelerar()

    def frear(self):
        self.__motor.frear()

    def direita(self):
        self.__volante.virar_direita()

    def esquerda(self):
        self.__volante.virar_esquerda()

    def velocidade(self):
        return self.__motor.mostra_velocidade()

    def direcao(self):
        return self.__volante.mostra_direcao()
