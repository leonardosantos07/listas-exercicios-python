#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
#
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente
# e a mensagem “APROVADO” se o conceito for A, B ou C
# ou “REPROVADO” se o conceito for D ou E.

#ex14
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

conceito = 'E'
media = (nota1 + nota2)/2

if (media>=9.0):
    conceito = 'A'
elif (media>=7.5):
    conceito = 'B'
elif (media>=6):
    conceito = 'C'
elif (media>=4):
    conceito = 'D'
else:
    conceito = 'E'

print(f'Notas {nota1} e {nota2}; Média {media}; Conceito {conceito}')
if (conceito in 'ABC'):
    print('APROVADO')
else:
    print('REPROVADO')
