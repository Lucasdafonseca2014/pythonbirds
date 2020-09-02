class Direcoes:
    def __init__(self):
        self.dir = 'norte'

    def direita(self):
        if self.dir == 'norte':
            self.dir = 'leste'
        elif self.dir == 'leste':
            self.dir = 'sul'
        elif self.dir == 'sul':
            self.dir = 'oeste'
        elif self.dir == 'oeste':
            self.dir = 'norte'

    def esquerda(self):
        if self.dir == 'norte':
            self.dir = 'oeste'
        elif self.dir == 'oeste':
            self.dir = 'sul'
        elif self.dir == 'sul':
            self.dir = 'leste'
        elif self.dir == 'leste':
            self.dir = 'norte'
