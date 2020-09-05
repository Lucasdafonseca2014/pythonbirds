from unittest import TestCase
from OO.pacote_carro.carro import Carro


class CarroTesteCase(TestCase):
    def teste_velocidade_inicial(self):
        carro = Carro()
        self.assertEqual(0, carro.velocidade())

    def teste_direcao_inicial(self):
        carro = Carro()
        self.assertEqual('norte', carro.direcao())

    def teste_acelerar(self):
        carro = Carro()
        carro.acelerar()
        self.assertEqual(1, carro.velocidade())

    def teste_frear(self):
        carro = Carro()
        carro.acelerar()
        carro.frear()
        self.assertEqual(0, carro.velocidade())

    def teste_virar_direita(self):
        carro = Carro()
        carro.direita()
        self.assertEqual('leste', carro.direcao())

    def teste_virar_esquerda(self):
        carro = Carro()
        carro.esquerda()
        self.assertEqual('oeste', carro.direcao())
