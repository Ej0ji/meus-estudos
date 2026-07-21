# Exercício 26 - Aula 9
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Escrever um programa que leia o nome completo de uma pessoa e apresente, de forma separada, apenas o primeiro e o último nome.

nome_completo = input('Digite um nome completo: ').strip()

nome_completo_transformado = nome_completo.title()

indice_fim_primeiro_nome = nome_completo_transformado.find(' ')
indice_comeco_ultimo_nome = nome_completo_transformado.rfind(' ') + 1

print('-' * 45)

print('''Olá, {}!
Seu primeiro nome é {}.
Já seu último nome é {}.'''.format(nome_completo_transformado, nome_completo_transformado[:indice_fim_primeiro_nome], nome_completo_transformado[indice_comeco_ultimo_nome:]))