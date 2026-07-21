# Exercício 29 - Aula 10
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Criar um programa que leia um número inteiro qualquer e mostre na tela se ele é PAR ou se ele é ÍMPAR. (Dica: Use o operador de resto da divisão %).

numero = int(input('Digite um número inteiro qualquer para verificar se é par ou ímpar: '))

print('-' * 45)

print('O número é PAR!' if numero % 2 == 0 else 'O número é ÍMPAR!')