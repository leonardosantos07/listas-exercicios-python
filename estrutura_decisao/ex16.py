#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
#O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa
#não deve fazer pedir os demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import math

def bhaskara(a, b, delta):
    x1 = ((-1)*b + math.sqrt(delta)) /(2*a)
    x2 = ((-1)*b - math.sqrt(delta)) /(2*a)
    return x1, x2

print('De a,b e c para calcular uma equação do segundo na forma ax² + bx + c')
a = float(input('digite o valor de a:'))
if a == 0:
    print ('não exite equação: encerrado')
else:
    b = float(input('digite o valor de b:'))
    c = float(input('digite o valor de c:'))
    delta = (math.pow(b,2) - 4 * a * c)
    if delta < 0:
        #a=1 ,b =2, c=5
        print (f'o delta ({delta:.2f}) é menor do que zero, então não existem raízes reais para a equação.')
    elif delta == 0:
        #a=4, b=-4, c=1
        raiz1, raiz2 = bhaskara(a, b, delta)
        print (f'o delta é igual a zero, a equação possui apenas uma raiz real: {raiz1:.2f}.')
    else:
        #a=1, b=5, c=-24
        print ('o delta é positivo, a equação possui duas raizes reais.')
        raiz1, raiz2 = bhaskara(a, b, delta)
        print(f'''
        O x1 da questão é:{raiz1}
        O x2 da questão é:{raiz2}
        ''')
