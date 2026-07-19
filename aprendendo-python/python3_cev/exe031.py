# Exercício 31 - Aula 10
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Fazer um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Insira um ano qualquer: '))

print('-' * 40)

# É um ano secular? (ex: 1700, 1900)
if ano % 100 == 0:
    # Se sim, é divisível por 400?
    if ano % 400 == 0:
        # Se sim, é um ano bissexto
        print('{} é um ano bissexto'.format(ano))
    else:
        # Se não, não é um ano bissexto
        print('{} não é um ano bissexto'.format(ano))
else:
    # Se não, é divisível por 4?
    if ano % 4 == 0:
        # Se sim, é um ano bissexto
        print('{} é um ano bissexto'.format(ano))
    else:
        # Se não, não é um ano bissexto
        print('{} não é um ano bissexto'.format(ano))

