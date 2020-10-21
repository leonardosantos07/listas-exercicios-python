#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

def bissexto(ano):
    if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
        return True
    else:
        return False

data = input('digite uma data no formato dd/mm/aaaa: ')
#considera que a data é válida de início, mas ainda não sabemos
valida = True
try:
    # o split da string vai criar uma lista com as strings
    data_separada = data.split('/')
    #se tiver mais de 3 que dizer que o usuário entrou com algo como 22/12/2020/2022
    if len(data_separada)>3:
        #se tiver mais de 3 blocos vai 'lançar/elevar' uma exceção
        raise Exception()

    dia, mes, ano = data_separada
    #se der erro na conversão do int vai gerar uma exceção
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)
except Exception:
    #qualquer exceção no bloco anterior irá cair aqui
    valida = False

if valida and ano > 0:
    if mes > 0 and mes < 13:
        if dia > 0 and dia < 32:
            valida = True
            if (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
                valida = False
            if mes == 2 and dia > 29:
                valida = False
            if mes == 2 and dia > 28 and not bissexto(ano):
                valida = False
        else:
            valida = False
    else:
        valida = False
else:
    valida = False

if(valida):
    print('válida')
else:
    print('inválida')
