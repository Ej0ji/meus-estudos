# Exercício 58 - Aula 14
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Melhorar o jogo do 'exe027.py' onde, agora, o computador “pensa” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

# IMPORTAÇÕES

from random import randint

# LÓGICA

# --- Inicialização e Input de Variáveis --------------------------------------------------

qtd_palpites = 1
numero_aleatorio = randint(0, 10)

numero_do_usuario = int(input('Chute o número que o sistema gerou: '))

print('-' * 40)

# -----------------------------------------------------------------------------------------

# --- Lógica de Palpites + Exibição de Resultado ------------------------------------------

while numero_do_usuario != numero_aleatorio:
    qtd_palpites += 1
    numero_do_usuario = int(input('Errou!! Tente novamente: '))

print('Parabéns, você acertou o número gerado pelo sistema! A quantidade de palpites foi: {}.'.format(qtd_palpites))

# -----------------------------------------------------------------------------------------
