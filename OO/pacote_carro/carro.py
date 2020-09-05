from OO.pacote_carro.motor import Motor
from OO.pacote_carro.volante import Volante


class Carro:
    """
        Classe que implementa a experiência de um pacote_carro, possuindo um motor e um volante.

        * Atributos de dado: Modelo, cor, motor, volante.
        * Métodos: Acelerar, frear, virar à direita, virar à esquerda, mostra velocidade, mostra direção.


        DOCTEST: Amostra de como a classe "Carro" deve funcionar ao ser implementada.

        >>> gol = Carro(modelo='Gol', cor='Prata')
        >>> gol.modelo
        'Gol'
        >>> gol.cor
        'Prata'
        >>> gol.direcao()
        'norte'
        >>> gol.direita()
        >>> gol.direcao()
        'leste'
        >>> gol.velocidade()
        0
        >>> gol.acelerar()
        >>> gol.acelerar()
        >>> gol.acelerar()
        >>> gol.acelerar()
        >>> gol.velocidade()
        4
        >>> gol.frear()
        >>> gol.velocidade()
        2

        """
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
