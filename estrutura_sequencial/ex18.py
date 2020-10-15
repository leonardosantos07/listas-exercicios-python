tamanho = float(input('Qual o tamanho do arquivo em MB? '))
velocidade = float(input('Qual a velocidade do link de internet em Mbps? '))

tamanho_mbit = tamanho * 8.3886
tempo_seg = tamanho_mbit/velocidade

print(f'O tempo aproximado é de {(tempo_seg/60):.2f} minutos')
