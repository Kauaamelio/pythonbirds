class Pessoa:
    olhos = 2
   

    def __init__(self, *filhos, nome=None, idade=62, sexo='M'):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.filhos = list(filhos)

    def comprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_statico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
       return f'{cls} - olhos {cls.olhos}'



if __name__ == '__main__':
    wanderley = Pessoa(nome='wanderley')
    vanderlei = Pessoa(wanderley, nome='vanderlei')
    print(Pessoa.comprimentar(vanderlei))
    print(vanderlei.nome)
    print(vanderlei.idade)
    for filhos in vanderlei.filhos:
        print(filhos.nome)
    vanderlei.sobrenome = 'Amelio'
    print(vanderlei.olhos)
    print(vanderlei.__dict__)
    print(wanderley.__dict__)
    print(Pessoa.metodo_statico(), vanderlei.metodo_statico())
    print(Pessoa.nome_e_atributos_de_classe(), vanderlei.nome_e_atributos_de_classe())

