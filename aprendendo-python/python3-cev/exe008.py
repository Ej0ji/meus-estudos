# Exercício 8 - Aula 7
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Ler um valor em metros e exibi-lo convertido em centímetros e milímetros.

valor_metros = float(input('Digite um valor (m): '))

print('-' * 30)

print('O valor em metros é {}m.'.format(valor_metros))
print('Em centímetros é {}cm'.format(valor_metros * 100))
print('Já seu valor em milímetros é {}mm.'.format(valor_metros * 1000))
