# Exercício 50 - Aula 13
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Desenvolver um programa que leia uma quantidade de números inteiros determinada pelo usuário e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

# IMPORTAÇÕES

from random import randint

# LÓGICA

qtd_numeros = int(input("Insira uma quantidade inteira de números inteiros: "))

print("--" * 30)

lista_numeros_int = []
lista_numeros_pares = []

for num in range(1, (qtd_numeros + 1)):

    lista_numeros_int.append(randint(1,30))

    index_lista_numeros = num - 1

    num_lista = lista_numeros_int[index_lista_numeros]

    if num_lista % 2 == 0:
        print('{} é o {}º número da lista e é par.'.format(num_lista, index_lista_numeros + 1))
        lista_numeros_pares.append(num_lista)

print("--" * 30)
print("A soma desses número pares é: {}.".format(sum(lista_numeros_pares)))
# Função sum() é nativa do python. Ela itera sobre uma sequência ou coleção de objetos numéricos
