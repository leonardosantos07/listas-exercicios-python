peso_peixe = float(input('Informe o peso total dos peixes:'))
print (f' O peso total dos peixes é:{peso_peixe:.2f}')

if (peso_peixe>50):
    excesso = (peso_peixe - 50)
    multa = (excesso * 4)
    print(f'Você precisará pagar R${multa:.2f} de multa por ter excedido o peso em {excesso:.2f} kg')
else:
    print(f'Você não precisará pagar multa, não excedeu ao limite de 50kg')
