NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'


class Volante:
    __virar_a_direita_dict = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    __virar_a_esquerda_dict = {NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE}

    def __init__(self):
        self.dir = 'Norte'

    def virar_direita(self):
        self.dir = self.__virar_a_direita_dict[self.dir]

    def virar_esquerda(self):
        self.dir = self.__virar_a_esquerda_dict[self.dir]

    def mostra_direcao(self):
        return self.dir


if __name__ == '__main__':
    v = Volante()
    print(v.dir)
    v.virar_direita()
    v.virar_direita()
    print(v.dir)
    v.virar_esquerda()
    v.virar_esquerda()
    print(v.dir)
