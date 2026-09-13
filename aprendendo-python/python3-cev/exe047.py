# Exercício 47 - Aula 13
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Criar um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

# LÓGICA

contador_total = 0

for contador in range(1, 51):

    if contador % 2 == 0:
        print('{} é um número par!'.format(contador))
        contador_total += 1

print('Ao todo, existem {} número pares no intervalo de 1 a 50.'.format(contador_total))
