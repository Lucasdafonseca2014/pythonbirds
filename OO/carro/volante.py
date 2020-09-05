class Volante:
    def __init__(self):
        self.dir = 'norte'

    def virar_direita(self):
        if self.dir == 'norte':
            self.dir = 'leste'
        elif self.dir == 'leste':
            self.dir = 'sul'
        elif self.dir == 'sul':
            self.dir = 'oeste'
        elif self.dir == 'oeste':
            self.dir = 'norte'

    def virar_esquerda(self):
        if self.dir == 'norte':
            self.dir = 'oeste'
        elif self.dir == 'oeste':
            self.dir = 'sul'
        elif self.dir == 'sul':
            self.dir = 'leste'
        elif self.dir == 'leste':
            self.dir = 'norte'

    def mostra_direcao(self):
        return self.dir
