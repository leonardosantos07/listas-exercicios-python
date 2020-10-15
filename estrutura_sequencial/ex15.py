valor_hora = float(input('Informe o quanto você ganha por horas trabalhadas?:'))
horas_mes = float(input('Informe quantas horas você trabalhou no mes?:'))
salario = valor_hora * horas_mes

def desconto(valor, porcentagem):
    return valor * porcentagem / 100

imposto = desconto(salario, 11)
inss = desconto(salario, 8)
sindicato = desconto(salario, 5)
salario_liq = salario - imposto - inss - sindicato

print(f'O seu salário líquido é R${salario_liq:.2f}')
