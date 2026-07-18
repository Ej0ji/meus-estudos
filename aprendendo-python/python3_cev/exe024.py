# Exercício 24 - Aula 9
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Criar um programa que leia o nome de uma pessoa e identifique se ela possui "Silva" em qualquer parte do nome.

nome_pessoa = input('Digite um nome de uma pessoa: ')

nome_pessoa_transformada = nome_pessoa.title()

nome_contem_silva = 'Silva' in nome_pessoa_transformada

print('-' * 30)

print(nome_contem_silva)

