#ex11
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo critérios

salario_atual = float(input('Digite o salário atual: '))
#dciionarios
reajustes_percentual = {'faixa1': 20, 'faixa2': 15, 'faixa3': 10, 'faixa4': 5 }
faixas_salariais = {'faixa1': 280, 'faixa2': 699, 'faixa3': 1499, 'faixa4': 1500 }

#funcao
def calcula_valor_aumento(salario, reajuste):
    return salario * (reajuste/100)

#funcao
def imprime_novo_salario(salario, reajuste, aumento):
    print(f'''
    O salário antigo era {salario:.2f}.
    Essa faixa salarial teve reajuste de {reajuste}%,
    com o aumento de R${aumento:.2f}, o salário atual é R${(salario+aumento):.2f}
    ''')

if (salario_atual <= faixas_salariais['faixa1']):
    aumento = calcula_valor_aumento(salario_atual,reajustes_percentual['faixa1'])
    imprime_novo_salario(salario_atual,reajustes_percentual['faixa1'], aumento)
elif (salario_atual <= faixas_salariais['faixa2']):
    aumento = calcula_valor_aumento(salario_atual,reajustes_percentual['faixa2'])
    imprime_novo_salario(salario_atual,reajustes_percentual['faixa2'], aumento)
elif (salario_atual <= faixas_salariais['faixa3']):
    aumento = calcula_valor_aumento(salario_atual,reajustes_percentual['faixa3'])
    imprime_novo_salario(salario_atual,reajustes_percentual['faixa3'], aumento)
else:
    aumento = calcula_valor_aumento(salario_atual,reajustes_percentual['faixa4'])
    imprime_novo_salario(salario_atual,reajustes_percentual['faixa4'], aumento)
