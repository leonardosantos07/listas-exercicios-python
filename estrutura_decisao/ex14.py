n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1+n2)/2
conceito = ''
conceito_aprovado = ['A','B','C']
conceito_reprovado = ['D','E']
if media > 0 and media <= 4:
    conceito = 'E'
elif media > 4 and media <= 6:
    conceito = 'D'
elif media > 6 and media <= 7.5:
    conceito = 'C'
elif media > 7.5 and media <= 9:
    conceito = 'B'
else:
    conceito = 'A'

print(f' A média é:{media}, e obteve o conceito:{conceito}')

if conceito in conceito_aprovado:
    print('APROVADO')
else:
    print('REPROVADO')
