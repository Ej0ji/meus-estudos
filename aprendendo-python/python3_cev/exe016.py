# Exercício 16 - Aula 8
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Crie um programa que leia um número real qualquer inserido via teclado (ex: 6.127) e exiba na tela apenas a sua porção inteira (ex: 6). Dica: Explore as funções do módulo math.

# IMPORTS

from math import trunc

# LÓGICA

num_real = float(input('Digite um número qualquer do conjunto dos Reais: '))

num_real_truncado = trunc(num_real)

print('-' * 30)

print('A porção inteira de {}, é {}.'.format(num_real, num_real_truncado))