# Exercício 37 - Aula 12
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Escrever um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero_int = int(input('Digite um número inteiro qualquer: '))

base_conversao = int(input('Digite a base de conversão: 1 para binário, 2 para octal ou 3 para hexadecimal: '))

print('-' * 40)

if base_conversao == 1:
    print('O número {} convertido para binário é: {}.'.format(numero_int, bin(numero_int)))
elif base_conversao == 2:
    print('O número {} convertido para octal é: {}.'.format(numero_int, oct(numero_int)))
elif base_conversao == 3:
    print('O número {} convertido para hexadecimal é: {}.'.format(numero_int, hex(numero_int)))