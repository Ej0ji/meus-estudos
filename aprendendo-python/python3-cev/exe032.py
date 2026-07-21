# Exercício 32 - Aula 10
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Fazer um programa que leia três números e mostre qual é o maior e qual é o menor.

lista_numeros = []
numero = float(input('Digite o primeiro número: '))
lista_numeros.append(numero)
numero = float(input('Digite o segundo número: '))
lista_numeros.append(numero)
numero = float(input('Digite o terceiro número: '))
lista_numeros.append(numero)

print('-' * 40)

maior_numero = lista_numeros[0]
menor_numero = lista_numeros[0]

# Encontra maior valor (DE FORMA BRUTA) da lista
if lista_numeros[1] >= lista_numeros[0] and lista_numeros[1] >= lista_numeros[2]:
    maior_numero = lista_numeros[1]
if lista_numeros[2] >= lista_numeros[0] and lista_numeros[2] >= lista_numeros[1]:
    maior_numero = lista_numeros[2]

# Encontra menor valor (DE FORMA BRUTA) da lista
if lista_numeros[1] <= lista_numeros[0] and lista_numeros[1] <= lista_numeros[2]:
    menor_numero = lista_numeros[1]
if lista_numeros[2] <= lista_numeros[0] and lista_numeros[2] <= lista_numeros[1]:
    menor_numero = lista_numeros[2]

if maior_numero == menor_numero:
    print('O maior número da lista é {} e o menor também é {}.'.format(maior_numero, menor_numero))
else:
    print('O maior número da lista é {}, já o menor é {}.'.format(maior_numero, menor_numero))