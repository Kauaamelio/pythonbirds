class Pessoa:
    def __init__(self, *filhos, nome=None, idade=62, sexo='M'):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.filhos = list(filhos)

    def comprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    wanderley = Pessoa(nome='wanderley')
    vanderlei = Pessoa(wanderley, nome='vanderlei')
    print(Pessoa.comprimentar(vanderlei))
    print(vanderlei.nome)
    print(vanderlei.idade)
    for filhos in vanderlei.filhos:
        print(filhos.nome)
    vanderlei.sobrenome = 'Amelio'
    print(vanderlei.__dict__)
    print(wanderley.__dict__)
    del vanderlei.sobrenome
    print(vanderlei.__dict__)
