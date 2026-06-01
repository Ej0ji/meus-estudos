# Desafios - Aula 6
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Criar um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e informações possíveis sobre ele (se é número, se é alfanumérico, etc).

print('*Exercício 4* - Script que recebe inputs e que mostre, logo em seguida, o tipo primitivo e informações possíveis sobre ele (se é número, se é alfanumérico, etc):\n')

conteudo = input('Digite algo: ')

print(f"{conteudo} é do tipo {type(conteudo)}")
print("-------------------------------------------------")
print(f"{conteudo} é um alfanumérico?: {conteudo.isalnum()}")
print(f"{conteudo} é um número?: {conteudo.isnumeric()}")
print(f"{conteudo} é um decimal?: {conteudo.isdecimal()}")
print(f"{conteudo} é um caractere ou string pertence ao padrão US-ASCII de 7 bits?: {conteudo.isascii()}")
print(f"{conteudo} é um caractere ou string minúsculo?: {conteudo.islower()}")
print(f"{conteudo} é um caractere ou string maíusculo?: {conteudo.isupper()}")
print(f"{conteudo} é um dígito(s) numérico(s)?: {conteudo.isdigit()}")
print(f"{conteudo} é um espaço?: {conteudo.isspace()}")


