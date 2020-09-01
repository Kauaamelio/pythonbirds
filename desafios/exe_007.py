"""
ler as notas de um aluno e mostrar sua média
"""

nota_1_bimestre = float(input('Digite a nota do primeiro bimestre : '))
nota_2_bimestre = float(input('Digite a nota do segundo bimestre : '))
nota_3_bimestre = float(input('Digite a nota do terceiro bimestre : '))
nota_4_bimestre = float(input('Digite a nota do quarto bimestre : '))
media_notas = (nota_1_bimestre + nota_2_bimestre + nota_3_bimestre + nota_4_bimestre) / 4

print(f'Sua nota do 1 Bi foi {nota_1_bimestre} a do segundo foi {nota_2_bimestre} '
      f'a do terceiro foi {nota_3_bimestre} e a do quarto {nota_4_bimestre} com isso sua média é {media_notas}')

if 7 > media_notas:
            print('Você foi reprovado')
elif media_notas >= 7:
            print('voce foi aprovado')



