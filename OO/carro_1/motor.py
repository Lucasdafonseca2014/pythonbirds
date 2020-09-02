class Motor:
    def __init__(self):
        self.__velocidade = 0

    def acelerar(self):
        self.__velocidade += 1

    def frear(self):
        self.__velocidade = max(self.__velocidade - 2, 0)

    def mostra_velocidade(self):
        return self.__velocidade
