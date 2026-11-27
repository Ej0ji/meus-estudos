# Exercício 57 - Aula 13
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Fazer um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

# LÓGICA

# --- Input de Dados + Lógica de M ou F ---------------------------------------------

sexo_pessoa = input('Digite o seu sexo. "M" para masculino ou "F" para feminino: ')

while sexo_pessoa not in ['M', 'F']:
    sexo_pessoa = input('Digite novamente. O valor deve ser "M" para masculino ou "F" para feminino: ')

print('Sexo do usuário inputado!')

# -----------------------------------------------------------------------------------
