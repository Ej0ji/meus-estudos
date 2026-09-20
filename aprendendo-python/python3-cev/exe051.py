# Exercício 51 - Aula 13
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Desenvolver um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

# LÓGICA

a = float(input('Insira o valor do primeiro termo (algum número racional) da P.A.: '))

r = float(input('Agora, o valor da razão (algum número racional) desta P.A.: '))

lista_pa = [a]

for i in range (1, 10):
    a += r
    lista_pa.append(a)

print(lista_pa)
