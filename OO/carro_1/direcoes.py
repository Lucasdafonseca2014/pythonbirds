class Direcoes:
    def __init__(self, atual, direita=None, esquerda=None):
        self.atual = atual
        self.direita = direita
        self.esquerda = esquerda


class TodasDirecoes:
    def __init__(self):

        self.norte = Direcoes(atual='norte')
        self.sul = Direcoes(atual='sul')
        self.leste = Direcoes(atual='leste')
        self.oeste = Direcoes(atual='oeste')

        self.norte.direita = self.leste
        self.norte.esquerda = self.oeste
        self.sul.direita = self.oeste
        self.sul.esquerda = self.leste
        self.leste.direita = self.sul
        self.leste.esquerda = self.norte
        self.oeste.direita = self.norte
        self.oeste.esquerda = self.sul
