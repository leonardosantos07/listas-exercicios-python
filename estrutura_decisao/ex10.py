turno = input('Informe o seu turno de acordo com a letra incial: ')

Matutino = 'M'
Vespertino = 'V'
Noturno = 'N'

if (turno.upper() == Matutino):
    print('Bom dia!')
elif (turno.upper() == Vespertino):
    print('Boa tarde!')
elif (turno.upper() == Noturno):
    print('Boa noite!')
else:
    print('Invalido')
