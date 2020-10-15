from math import ceil

tamanho = float(input('Qual o tamanho da área em m2? '))
litros = tamanho/6
if (litros < 18):
    qtd_galao = ceil(litros/3.6)
    qtd_lata = 0
else:
    qtd_lata = litros/18
    qtd_galao = (qtd_lata - int(qtd_lata))/3.6

total_lata = round(qtd_lata)
total_galao = ceil(qtd_galao)
print(f'Você precisará de {total_lata} lata(s) e o preço total é R${(total_lata*80):.2f}')
print(f'Você precisará de {total_galao} galão(ões) e o preço total é R${(total_galao*25):.2f}')
