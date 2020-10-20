#ex15. Faça um Programa que peça os 3 lados de um triângulo.

lado1 = float(input('Digite o primeiro lado do triângulo: '))
lado2 = float(input('Digite o segundo lado do triângulo: '))
lado3 = float(input('Digite o terceiro lado do triângulo: '))

if (((lado1+lado2) > lado3) and ((lado1+lado3) > lado2) and ((lado3+lado2) > lado1)):
    if (lado1==lado2==lado3):
        print('Triângulo Equilátero')
    elif (lado1==lado2 or lado1 == lado3 or lado2 == lado3):
        print('Triângulo Isósceles')
    elif (lado1 != lado2 and lado2 != lado3 and lado3 != lado1):
        print('Escaleno')
    else:
        print('Não poderá imprimir isso se for triângulo')
else:
    print('Não é triângulo')
