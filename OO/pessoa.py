class Pessoa:
    def __init__(self, *filhos, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    lucas = Pessoa(nome='Lucas', idade=28)
    carlos = Pessoa(lucas, nome='Carlos', idade=62)
    print(Pessoa.cumprimentar(carlos))
    print(id(carlos))
    print(carlos.cumprimentar())
    print(carlos.nome)
    print(carlos.idade)
    for filho in carlos.filhos:
        print(filho.nome)
    carlos.sobrenome = "D'Afonseca"
    del carlos.filhos     # Remover um atributo de objeto.
    print(carlos.__dict__)
    print(lucas.__dict__)



# Atributo especial "__dict__" retorna todos os atributos definidos (tanto pelo "__init__" quanto dinâmicos)
# de um determinado objeto.
