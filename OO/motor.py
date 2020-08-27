class Motor:

    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        if self.velocidade < 0:
            self.velocidade = 0

#testando Motor
if __name__ == '__main__':
    motor = Motor()
    print(Motor.velocidade)
    motor.acelerar()
    print(Motor.velocidade)
    motor.acelerar()
    print(Motor.velocidade)
    motor.acelerar()
    print(Motor.velocidade)
    motor.frear()
    print(Motor.velocidade)
    motor.frear()
    print(Motor.velocidade)





