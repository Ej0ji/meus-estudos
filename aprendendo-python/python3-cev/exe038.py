# Exercício 38 - Aula 12
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Escrever um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#
# – O primeiro valor é maior
#
# – O segundo valor é maior
#
# – Não existe valor maior, os dois são iguais

numero_int1 = int(input('Digite o primeiro número inteiro: '))
numero_int2 = int(input('Digite o segundo número inteiro: '))

if numero_int1 > numero_int2:
    print('O primeiro valor, {} é o maior!'.format(numero_int1))
elif numero_int1 < numero_int2:
    print('O segundo valor, {} é o maior!'.format(numero_int2))
else:
    print('Não existe valor maior, ambos são o iguais!')