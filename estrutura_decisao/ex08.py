p1 = float(input('Digite o preço do primeiro produto:'))
p2 = float(input('Digite o preço do segundo produto:'))
p3 = float(input('Digite o preço do terceiro produto:'))
menor = p1
if p2 < menor:
    menor = p2
if p3 < menor:
    menor = p3

print(f' O {menor} é menor')
