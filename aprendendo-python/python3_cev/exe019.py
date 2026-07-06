# Exercício 19 - Aula 8
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Escrever um programa que exiba aleatóriamente uma opção de nome dentre quatro nomes possíveis.
# DICA: Para este exercício será necessário o uso de listas

# IMPORTAÇÕES

from random import choice

# LÓGICA

lista_nomes = ['Eric', 'Joji', 'Isshiki', 'Karai']

nome_randomico = choice(lista_nomes)

print(nome_randomico)