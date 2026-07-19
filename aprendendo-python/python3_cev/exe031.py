# Exercício 31 - Aula 10
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Fazer um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Insira um ano qualquer: '))

print('-' * 40)

# É um ano normal divisível por 4 OU, um ano secular divisível por 400? (ex: 1700, 1900)
if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    # Se sim, é um ano bissexto
    print('{} é um ano bissexto'.format(ano))
else:
    # Se não, não é um ano bissexto
    print('{} não é um ano bissexto'.format(ano))

