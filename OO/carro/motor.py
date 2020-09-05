class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade = max(self.velocidade - 2, 0)

    def mostra_velocidade(self):
        return self.velocidade
