lado_a = float(input('Digite o primeiro lado:'))
lado_b = float(input('Digite o primeiro lado:'))
lado_c = float(input('Digite o primeiro lado:'))

if lado_a + lado_b > lado_c and lado_b + lado_c > lado_a and lado_a + lado_c > lado_b:
    if lado_a == lado_b and lado_a == lado_c:
        print('O triangulo é equilátero')
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        print('O triangulo é isósceles')
    else:
        print('O triandulo é escaleno')
else:
    print('Não é um triângulo')
