#6
#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
#Depois modifique o programa para que ele mostre os números um ao lado do outro.

#função range(start, stop, step) retorna uma sequencia de números,
#começando pelo 0 se o start não for passado

print('\nUm abaixo do outro:')
for i in range(1, 21):
    print(i)

print('\nUm ao lado do outro:')

for i in range(1, 21):
    print(i, end=' ')

print('\n')

#Dúvida 1
#Qual a diferença entre range(1,21) e range(21)?
#Dúvida 2
#O que acontece se passar um valor diferente de 1 na posição step, ex: range(1,21,5)?
