# Exercício 9 - Aula 7
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Ler um número inteiro qualquer e mostrar na tela a sua tabuada completa.

numero_inteiro = int(input('Digite um número inteiro para gerar sua tabuada: '))

print('-' * 30)

print('O número digitado foi {}.'.format(numero_inteiro))

print('A tabuada de {0} de 1 a 12 é:\n1×{0} = {1}\n2×{0} = {2}\n3×{0} = {3}\n4×{0} = {4}\n5×{0} = {5}\n6×{0} = {6}\n7×{0} = {7}\n8×{0} = {8}\n9×{0} = {9}\n10×{0} = {10}\n11×{0} = {11}\n12×{0} = {12}'.format(numero_inteiro, numero_inteiro * 1, numero_inteiro * 2, numero_inteiro * 3, numero_inteiro * 4, numero_inteiro * 5, numero_inteiro * 6, numero_inteiro * 7, numero_inteiro * 8, numero_inteiro * 9, numero_inteiro * 10, numero_inteiro * 11, numero_inteiro * 12))

# ---- EXTRA --------------------------------------------------------------------

print('Apesar do curso não estar na etapa de iteradores ainda, eu me recuso em gerar uma tabuada dessa forma acima. Então aqui vai a versão usando iteradores:')

print('Sua tabuada de {} de 1 a 12 é:'.format(numero_inteiro))

indice_tabuada = 0

for i in range(1, 13):
    indice_tabuada += 1
    print('{}×{} = {}'.format(indice_tabuada, numero_inteiro, (indice_tabuada * numero_inteiro)))

# --------------------------------------------------------------------------------