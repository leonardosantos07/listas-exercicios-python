#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
dia = int(input('digite o dia:'))
mes = int(input('digite o mes:'))
ano = int(input('difite o ano:'))

if dia==1 >= 31:
    print('verdadeiro')
elif mes==1 >= 12:
    print('verdadeiro')
elif ano==0 >= 3000:
    print('verdadeiro')
else:
    print('Inválida')



dando invalido em qualquer data
