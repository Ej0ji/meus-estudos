# Exercício 27 - Aula 10
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Desenvolver um programa que faça o computador "pensar" em um número inteiro aleatório entre 0 e 5. Peça para o usuário tentar descobrir qual foi o número escolhido. O programa deverá escrever na tela se o usuário venceu ou perdeu.

# IMPORTAÇÕES

from random import randint

# LÓGICA

numero_aleatorio = randint(0, 5)

numero_do_usuario = int(input('Chute o número que o sistema gerou: '))

print('-' * 40)

print('Parabéns, você acertou o número gerado pelo sistema!' if numero_aleatorio == numero_do_usuario else 'Errou! Tente novamente!')




   