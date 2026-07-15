# Exercício 21 - Aula 9
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Desenvolver um programa que leia o nome completo de uma pessoa e mostre o nome com todas as letras maiúsculas, com todas as minúsculas, a quantidade de letras ao todo (sem contar os espaços) e quantas letras tem o primeiro nome.

nome_completo = input('Digite o seu nome completo: ')

print('-' * 30)

print('Olá, {}!'.format(nome_completo))

print('Seu nome todo em maíusculas é {}.'.format(nome_completo.upper()))

print('E todo em minúsculas é {}.'.format(nome_completo.lower()))

print('A quantidade de letras no seu nome é {}.'.format(len(nome_completo)  - nome_completo.count(' ')))

print('Já a quantidade de letras no primeiro nome é {}.'.format(len(nome_completo) - len(nome_completo[nome_completo.find(' '):])))

