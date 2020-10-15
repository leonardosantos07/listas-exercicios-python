from math import ceil

tamanho = float(input('Qual o tamanho da área em m2? '))
qtd_lata = ceil((tamanho/3)/18)
print(f'Você precisará de {qtd_lata} latas e o preço total é R${(qtd_lata*80):.2f}')
