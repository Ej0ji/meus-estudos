# Exercício 48 - Aula 13
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Fazer um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

# LÓGICA

somador = 0

for contador in range(1, 501):
    if contador % 3 == 0:
        somador += contador
        print('{} é um múltiplo de 3! '.format(contador))
        print('Somador de múltiplos de 3 = {}'.format(somador))
    else:
        print('{} não é múltiplo de 3!'.format(contador))