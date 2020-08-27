class Direcao:

    def __init__(self, coordenada_inicial = 'norte'):
        self.coordenada_inicial = coordenada_inicial

    def girar_a_direita(self):
        if self.coordenada_inicial == 'norte':
            self.coordenada_inicial = 'leste'
        elif self.coordenada_inicial == 'leste':
             self.coordenada_inicial = 'sul'
        elif self.coordenada_inicial == 'sul':
            self.coordenada_inicial = 'oeste'
        else:
            self.coordenada_inicial = 'norte'


    def girar_a_esquerda(self):
        if self.coordenada_inicial == 'norte':
            self.coordenada_inicial = 'oeste'
        elif self.coordenada_inicial == 'oeste':
             self.coordenada_inicial = 'sul'
        elif self.coordenada_inicial == 'sul':
            self.coordenada_inicial = 'leste'
        else:
            self.coordenada_inicial = 'norte'





if __name__ == '__main__':

    direcao = Direcao()
    print(direcao.coordenada_inicial)
    direcao.girar_a_direita()
    print(direcao.coordenada_inicial)
    direcao.girar_a_direita()
    print(direcao.coordenada_inicial)
    direcao.girar_a_direita()
    print(direcao.coordenada_inicial)
    direcao.girar_a_direita()
    print(direcao.coordenada_inicial)
    print()
    direcao.girar_a_esquerda()
    print(direcao.coordenada_inicial)
    direcao.girar_a_esquerda()
    print(direcao.coordenada_inicial)
    direcao.girar_a_esquerda()
    print(direcao.coordenada_inicial)
    direcao.girar_a_esquerda()
    print(direcao.coordenada_inicial)







