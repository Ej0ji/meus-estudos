# Exercício 19 - Aula 8
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Escrever um programa que exiba aleatóriamente uma opção de nome dentre quatro nomes possíveis. Logo após exiba uma nova ordem dos quatro nomes.
# DICA: Para este exercício será necessário o uso de listas

# IMPORTAÇÕES

from random import choice
from random import shuffle

# LÓGICA

lista_nomes = ['Eric', 'Joji', 'Isshiki', 'Karai']

print('Lista de nomes atual: {}.'.format(lista_nomes))

nome_randomico = choice(lista_nomes)

print('Nome sorteado: {}.'.format(nome_randomico))

# ------------------------------------------------------

shuffle(lista_nomes)

print('Nova ordem da lista de nomes: {}.'.format(lista_nomes))



