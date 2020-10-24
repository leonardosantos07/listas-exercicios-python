nota = -1

while nota < 0 or nota > 10:
    nota = int(input('Entre com uma nota entre zero e dez: '))
    if nota < 0 or nota > 10:
        print('Valor inválido')
