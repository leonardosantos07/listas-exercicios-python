#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#326 = 3 centenas, 2 dezenas e 6 unidades
#12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
numero = input('Digite um número menor que 1000:')

if int(numero) > 1000:
    import sys
    #vai interromper o programa e o resto não será executado.
    sys.exit("O número não é menor que 1000")

tamanho_numero = len(numero)
centena = 0
dezena = 0
unidade = 0
mensagem = '\n{} = '.format(numero)

if tamanho_numero == 3:
    centena = numero[0:1]
    dezena = numero[1:2]
    unidade = numero[2:3]

if tamanho_numero == 2:
    dezena = numero[0:1]
    unidade = numero[1:2]

if tamanho_numero == 1:
    unidade = numero[0:1]

if int(centena) > 1:
    mensagem += '{} centenas'.format(centena)
elif int(centena) == 1:
    mensagem += '{} centena'.format(centena)
else:
    mensagem += '' #para explicação do código

if int(centena) > 0:
    mensagem += ', '

if int(dezena) > 1:
    mensagem += '{} dezenas e '.format(dezena)
elif int(dezena) == 1:
    mensagem += '{} dezena e '.format(dezena)
elif int(dezena) == 0 and int(centena) > 0:
    mensagem += '{} dezena e '.format(dezena)

#poderia acrescentar o 'e' com condição aqui,
#mas decidi sempre imprimir a unidade depois da dezena
#mesmo que ela seja 0

if int(unidade) > 1:
    mensagem += '{} unidades'.format(unidade)
else:
    mensagem += '{} unidade'.format(unidade)

print(mensagem)
