"""
Faça um programa que leia um numero inteiro e mostre na tela o seu sussessor e o seu antecessor.

"""

num_inteiro = int(input('Digite um numero.: '))
antecessor = num_inteiro - 1
sussessor = num_inteiro + 1
#utilizando o format
print('O numero inteiro digitado {} o seu sussessor é {} e o antecessor é {}'
      .format(num_inteiro, antecessor, sussessor))


# utilizando o f'

print(f'O numero inteiro digitado foi >>> {num_inteiro} ', end=' ')
print(f'o seu antecessor é {antecessor}', end=' ')
print(f'o seu sussessor é {sussessor}')

