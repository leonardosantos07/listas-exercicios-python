valor_hora = float(input('Informe o quanto você ganha por horas trabalhadas?:'))
horas_mes = float(input('Informe quantas horas você trabalhou no mes?:'))
salario_bruto = valor_hora * horas_mes

def desconto(valor, porcentagem):
    return valor * porcentagem / 100

if salario_bruto <= 900:
    desconto_ir = 0
elif salario_bruto <= 1500:
    desconto_ir = 5
elif salario_bruto <= 2500:
    desconto_ir = 10
else:
    desconto_ir = 20

inss = desconto(salario_bruto, 10)
fgts = desconto(salario_bruto, 11)
sindicato = desconto(salario_bruto, 3)
ir = desconto(salario_bruto, desconto_ir)

print(f'''
Salário bruto       R$ {salario_bruto:.2f}
FGTS                R$ {fgts:.2f}
IR                  R$ {ir:.2f}
INSS                R$ {inss:.2f}
Sindicato           R$ {sindicato:.2f}
Total de descontos  R$ {(inss + sindicato + ir):.2f}
Salario liquido     R$ {(salario_bruto - (inss + sindicato + ir)):.2f}
''')
