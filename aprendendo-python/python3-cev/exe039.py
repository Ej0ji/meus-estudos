# Exercício 39 - Aula 12
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Fazer um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é o dia exato de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

# IMPORTAÇÕES

# 'as' serve para mudar a forma como a biblioteca será chamada nessa instância de programa (esse é o conceito de 'ALIASES')
import datetime as dt

# LÓGICA

print('Verificação de alistamento militar')
print('-' * 40)

data_nascimento = input('Digite sua data de nascimento no formato dd/mm/yyyy: ')

# Converte a data de string para date sem o time
data_nascimento_convertida = dt.datetime.strptime(data_nascimento, '%d/%m/%Y').date()

# Obtém a data atual sem time
data_atual = dt.date.today()

# Obtém dias totais decorridos desde o dia que a pessoa nasceu
idade_dias = (data_atual - data_nascimento_convertida).days

idade_alistamento_dias = 6574

print('--' * 45)

if idade_dias < idade_alistamento_dias:
    print('Ainda não é possível se alistar. Faltam {} dias!'.format(idade_alistamento_dias - idade_dias))
elif idade_dias > idade_alistamento_dias:
    print('O tempo de alistamento passou faz {} dias!'.format(abs(idade_alistamento_dias - idade_dias)))
elif idade_dias == idade_alistamento_dias:
    print('Hoje é o dia exato para se alistar!')