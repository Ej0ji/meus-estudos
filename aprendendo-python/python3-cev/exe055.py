# Exercício 55 - Aula 13
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Fazer um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

# LÓGICA

# --- Input dos Dados -------------------------------

maior_peso_kg = 0
menor_peso_kg = 999

for i in range(5):
    peso_pessoa = int(input('Digite o peso em kgs da {}ª pessoa: '.format(i+1)))

    if peso_pessoa > maior_peso_kg:
        maior_peso_kg = peso_pessoa

    if peso_pessoa <= menor_peso_kg:
        menor_peso_kg = peso_pessoa

print('O maior peso dentre o grupo de 5 pessoas foi {}kgs e o menor foi {}kgs.'.format(maior_peso_kg, menor_peso_kg))

