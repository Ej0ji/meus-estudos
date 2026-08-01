# Exercício 45 - Aula 12
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Criar um programa que faça o computador jogar Jokenpô com você.

# IMPORTAÇÕES

import random
  
# LÓGICA

print('-' * 40)
print('Jogo do Jokenpô')
print('-' * 40)

opcoes_de_jogadas = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}

id_maquina = 'Máquina'
jogada_maquina = random.choice(list(opcoes_de_jogadas))
tipo_jogada_maquina = opcoes_de_jogadas[jogada_maquina]

id_jogador = input('Digite o seu nome: ')
jogada_pessoa = int(input('''Selecione uma das opções de jogadas:

    1 - Pedra

    2 - Papel

    3 - Tesoura

Digite o número da sua jogada: '''))

tipo_jogada_pessoa = opcoes_de_jogadas[jogada_pessoa]

print('-' * 40)

if jogada_maquina == jogada_pessoa:
    print('Jogador = {} X Máquina = {}! EMPATE!'.format(tipo_jogada_pessoa, tipo_jogada_maquina))

elif jogada_maquina in [1, 2] and jogada_pessoa in [1, 2]:

    vencedor = id_jogador if jogada_pessoa == 2 else id_maquina
    print('Jogador = {} X Máquina = {}! O vencedor é jogador(a) {}!'.format(tipo_jogada_pessoa, tipo_jogada_maquina, vencedor))

elif jogada_maquina in [2, 3] and jogada_pessoa in [2, 3]:

    vencedor = id_jogador if jogada_pessoa == 3 else id_maquina
    print('Jogador = {} X Máquina = {}! O vencedor é jogador(a) {}!'.format(tipo_jogada_pessoa, tipo_jogada_maquina, vencedor))

elif jogada_maquina in [1, 3] and jogada_pessoa in [1, 3]:

    vencedor = id_jogador if jogada_pessoa == 1 else id_maquina
    print('Jogador = {} X Máquina = {}! O vencedor é jogador(a) {}!'.format(tipo_jogada_pessoa, tipo_jogada_maquina, vencedor))

print('-' * 40)