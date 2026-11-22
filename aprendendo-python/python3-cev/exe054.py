# Exercício 54 - Aula 13
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Criar um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

# IMPORTAÇÕES

# Caso a dependênca da biblioteca datetime não esteja funcionando, dê um 'pip install datetime'
import datetime as dt 

# LÓGICA

print('Verificação de maioridade de sete pessoas')
print('-' * 40)

# --- Input de dados, Inicialização de Variáveis e------------

maioridade_em_dias = 6574
data_atual = dt.date.today()

qtd_maiores = 0
qtd_menores = 0

for i in range(7):
    data_nascimento = input('Digite a data de nascimento no formato dd/mm/yyyy da pessoa {}: '.format(i+1))
    data_nascimento_convertida = dt.datetime.strptime(data_nascimento, '%d/%m/%Y').date()
    idade_dias = (data_atual - data_nascimento_convertida).days

    if idade_dias >= maioridade_em_dias:
        print('Pessoa {} é MAIOR de idade, com {} anos!'.format(i, round((idade_dias/365.25), 2)))
        qtd_maiores += 1
    else:
        print('Pessoa {} é MENOR de idade, com {} anos!'.format(i, (idade_dias/365.25)))
        qtd_menores += 1

print('Ao todo foram observados, dentre o grupo de pessoas, {} maiores e {} menores.'.format(qtd_maiores, qtd_menores))

# -------------------------------------------------------------