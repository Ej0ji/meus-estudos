# Exercício 23 - Aula 9
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Construir um script que leia o nome de uma cidade e informe se ela começa ou não com a palavra "Santo".

nome_cidade = input('Digite o nome de uma cidade: ').strip()

nome_cidade_transformada = nome_cidade.title()

nome_comeca_com_santo = 'Santo' in nome_cidade_transformada[:(nome_cidade_transformada.find(' '))]

print('-' * 30)

print('A cidade com nome de {}, começa com a palavra "Santo"?: {}'.format(nome_cidade_transformada, nome_comeca_com_santo))