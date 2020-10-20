#Faça um Programa que leia um número e exiba o dia correspondente da semana.
#(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

dia_da_semana = int(input('Digite um numero entre 1 e 7: '))

if dia_da_semana == 2:
    print('Segunda-Feira')

elif dia_da_semana == 3:
    print('Terça-Feira')

elif dia_da_semana == 4:
    print('Quarta-Feira')

elif dia_da_semana == 5:
    print('Quinta-Feira')

elif dia_da_semana == 6:
    print('Sexta-Feira')

elif dia_da_semana == 7:
    print('Sábado')

elif dia_da_semana == 1:
    print('Domingo')
else:
    print('inválido')


perguntar outra maneira de fazer... programa ficou muito estenso.. fazer com lista?
