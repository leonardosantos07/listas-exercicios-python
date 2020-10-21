#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

#Regra
# São bissextos todos os anos múltiplos de 400, p.ex: 1600, 2000, 2400, 2800...
# São bissextos todos os múltiplos de 4, exceto se for múltiplo de 100 mas não de 400, p.ex: 1996, 2000, 2004, 2008, 2012, 2016, 2020...
# Não são bissextos todos os demais anos.
ano = int(input('digite o ano para saber se é bissexto:'))
if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    print('é bissexto')
else:
    print('não é bissexto')


#Outra maneira
#
# if ano % 400 == 0:
#     bissexto = True
# elif ano % 4 == 0 and ano % 100 != 0:
#     bissexto = True
# else:
#     bissexto = False
#
# if bissexto:
#     print('é bissexto')
# else:
#     print('não é bissexto')
