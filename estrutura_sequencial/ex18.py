# Faça um programa que peça o tamanho
# de um arquivo para download (em MB)
# e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download
# do arquivo usando este link (em minutos).

tamanho = float(input('Qual o tamanho do arquivo em MB? '))
velocidade = float(input('Qual a velocidade do link de internet em Mbps? '))

tamanho_mbit = tamanho * 8.3886
tempo_seg = tamanho_mbit/velocidade

print(f'O tempo aproximado é de {(tempo_seg/60):.2f} minutos')
