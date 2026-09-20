# Exercício 52 - Aula 13
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Fazer um programa que leia um número inteiro e diga se ele é ou não um número primo.

# IMPORTAÇÕES

import math

# LÓGICA

# Receber o numero n
# Obter a raiz quadrada do mesmo
# listar os números >1 e <raiz quadrada
# iterar sobre a lista, numero a numero e ver se os mesmo sao divisiveis pelo numero inteiro inicial
# se nao for, é primo
# se for é primo

num_int_qualquer = int(input('Insira um número inteiro qualquer maior que 1: '))

sqrt_do_num_int = math.ceil(math.sqrt(num_int_qualquer))

num_primo = 1

for i in range(2, sqrt_do_num_int):

    if num_int_qualquer % i == 0:
        num_primo = 0

if num_primo == 1 and num_int_qualquer != 1 and num_int_qualquer != 4:
    print('{} é um número primo!'.format(num_int_qualquer))
else:
    print('{} não é um número primo!'.format(num_int_qualquer))
