# Exercício 28 - Aula 10
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Escrever um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado. A multa deve custar R$ 7,00 por cada quilômetro acima do limite estabelecido.

# IMPORTAÇÕES

from random import randint

# LÓGICA

velocidade_carro = randint(40, 120)

velocidade_maxima_permitida = 80 #Km/h

if velocidade_carro > velocidade_maxima_permitida:
    
    delta_velocidade_acima = velocidade_carro - velocidade_maxima_permitida

    multa = 7 * delta_velocidade_acima

    print('''Você atingiu a velocidade de {}Km/h!
    Isto é {}Km/h acima do permitido de {}Km/h!
    Uma multa de R${} será aplicada (MULTA = R$7 por cada km/h acima do limite).'''
    .format(velocidade_carro, delta_velocidade_acima, velocidade_maxima_permitida, multa))

