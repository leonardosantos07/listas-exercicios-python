peso_peixe = float(input('Informe o peso total dos peixes:'))
print (f' O peso total dos peixes é:{peso_peixe:.2f}')

if (peso_peixe>50):
    excesso = (peso_peixe - 50)
    multa = (excesso * 4)
