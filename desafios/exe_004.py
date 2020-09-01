"""
verificar os possíveis valores para as variáveis.

"""

valor = input('Digite um valor')
print(f'o valor digitado é alfanumerico ? {valor.isalnum()}')
print(f'o valor digitado é um alfa ? {valor.isalpha()}')
print(f'o valor digitado é minusculo ? {valor.islower()}')
print(f'o valor digitado é um numero ? {valor.isnumeric()}')
print(f'o valor digitado é um espaço ? {valor.isspace()}')

