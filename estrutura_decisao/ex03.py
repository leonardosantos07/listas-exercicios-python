#Faça um Programa que verifique se uma letra digitada é "F" ou "M".
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
letra = input('digite uma letra:')
print (f' a letra é {letra}')
if (letra.upper() == 'F'):
    print (f' se a letra for igual F o sexo é feminino: {letra}')
elif (letra.lower() == 'm'):
    print (f' se a letra for igual M o sexo é masculino: {letra}')
else:
    print ('Inválido')
