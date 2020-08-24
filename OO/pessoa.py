class Pessoa:
    def __init__(self, nome=None, idade=35, sexo='m'):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def comprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
     p = Pessoa('wanderley')
     print(Pessoa.comprimentar(p))
     print(id(p))
     print(p.comprimentar())
     p.nome = 'wanderley'
     print(p.nome)
     p.idade = 34
     print(p.idade)
     p.sexo = 'M'
     print(p.sexo)
