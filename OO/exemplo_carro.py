from OO.pacote_carro.carro import Carro

kombi = Carro(modelo='Kombi', cor='Branco')
kombi.acelerar()
kombi.acelerar()
kombi.acelerar()
kombi.acelerar()
kombi.direita()
kombi.direita()
kombi.direita()
print(f'Direção: {kombi.direcao()}')
print(f'Velocidade: {kombi.velocidade()} m/s')
print(f'Modelo: {kombi.modelo}')
print(f'cor: {kombi.cor}')
