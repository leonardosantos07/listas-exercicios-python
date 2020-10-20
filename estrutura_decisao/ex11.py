salario = float(input('Digite o salário do trabalhador:'))

if salario <= 280:
    aumento_percentual = 20
elif salario <= 700:
    aumento_percentual = 15
elif salario <= 1500:
    aumento_percentual = 10
else:
    aumento_percentual = 5

aumento = (salario * aumento_percentual/100)
novo_salario = salario + aumento

print(f' O salario antes do reajusta era de: R${salario:.2f}')
print(f' O aumento foi de: {aumento_percentual}%')
print(f' O valor do aumento foi de: R${aumento:.2f}')
print(f' O novo salario é de: R${novo_salario:.2f}')
