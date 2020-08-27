from OO.motor import Motor
from OO.direcao import Direcao
class Carro:

    def __init__(self, motor, direcao):
        self.motor = motor
        self.direcao = direcao

if __name__ == '__main__':
    pe_na_tabua = Motor()
    volante = Direcao()

    veiculo = Carro(motor=pe_na_tabua, direcao=volante)
    #acelerando veiculo
    veiculo.motor.acelerar()
    print(veiculo.motor.velocidade)
    veiculo.motor.acelerar()
    print(veiculo.motor.velocidade)
    veiculo.motor.acelerar()
    print(veiculo.motor.velocidade)
    #freando veiculo
    veiculo.motor.frear()
    print(veiculo.motor.velocidade)
    veiculo.motor.frear()
    print(veiculo.motor.velocidade)
    #virando carro a direita
    print(veiculo.direcao.coordenada_inicial)
    veiculo.direcao.girar_a_direita()
    print(veiculo.direcao.coordenada_inicial)
    #virando carro a esquerda
    veiculo.direcao.girar_a_esquerda()
    print(veiculo.direcao.coordenada_inicial)
    veiculo.direcao.girar_a_esquerda()
    print(veiculo.direcao.coordenada_inicial)







