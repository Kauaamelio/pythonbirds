from unittest import TestCase

from oo.carro import Motor
from oo.carro import Direcao


class Carro_Teste_Case(TestCase):
    def test_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)

    def test_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)

    def test_frear(self):
        motor = Motor()
        motor.frear()
        self.assertEqual(0, motor.velocidade)

    def test_posicao_inicial(self):
        direcao = Direcao()
        direcao.valor
        self.assertEqual('Norte', direcao.valor)

    def test_girar_a_direita(self):
        direcao = Direcao()
        direcao.girar_a_direita()
        self.assertEqual('Leste', direcao.valor)

    def test_girar_a_esquerda(self):
        direcao = Direcao()
        direcao.girar_a_esquerda()
        self.assertEqual('Oeste', direcao.valor)


