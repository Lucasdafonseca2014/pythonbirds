class Pessoa:
    olhos = 2

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):       # Se conecta com a classe através do 'cls', assim como os métodos
        return f'{cls} - olhos {cls.olhos}'    # utilizando o 'self'.

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
    carlos.olhos = 1
    print(carlos.__dict__)
    print(lucas.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(carlos.olhos)
    print(lucas.olhos)
    print(id(Pessoa.olhos), id(carlos.olhos), id(lucas.olhos))


# Atributo especial "__dict__" retorna todos os atributos definidos (tanto pelo "__init__" quanto dinâmicos)
# de um determinado objeto.
