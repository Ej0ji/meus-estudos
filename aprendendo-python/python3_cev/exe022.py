# Exercício 22 - Aula 9
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Criar um programa que leia um número de 0 a 9999 e exiba na tela cada um dos dígitos separados por unidade, dezena, centena e milhar, utilizando lógica de string ou matemática.

# OPÇÃO 1 - LÓGICA DE STRINGS ----------------------------------------
numero = input('Digite um número de 0 a 9999 no formato xxxx: ')

print('-' * 30)

print('As casas decimais do número {} são:'.format(numero))

print('UNIDADES: {}'.format(numero[len(numero) - 1]))
print('DEZENAS: {}'.format(numero[len(numero) - 2]))
print('CENTENAS: {}'.format(numero[len(numero) - 3]))
print('MILHARES: {}'.format(numero[len(numero) - 4]))

# OPÇÃO 2 - LÓGICA MATEMÁTICA ----------------------------------------

numero = int(input('Digite um número de 0 a 9999: '))

print('-' * 30)

print('As casas decimais do número {} são:'.format(numero))


