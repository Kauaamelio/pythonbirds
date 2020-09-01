contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
            'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
            'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
     num = int(input('digite um número entre 0 e 20 .:'))
     if 0 <= num <= 20:
         break
     print('tente novamente vc nao digitou o valor esperado 0-20 ')
print(f'Vc digitou {contagem[num]}')
