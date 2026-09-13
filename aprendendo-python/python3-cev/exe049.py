# Exercício 49 - Aula 13
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Fazer um programa para mostrar a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

# LÓGICA

numero_usuario = int(input('Digite um número inteiro: '))
print('A tabuada completa de {} é:'.format(numero_usuario))
print('--' * 30)

for multiplo in range(1, (numero_usuario + 1)):
    multiplic_tabuada = numero_usuario * multiplo
    print('{} x {} = {}'.format(numero_usuario, multiplo, multiplic_tabuada))
