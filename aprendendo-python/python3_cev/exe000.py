# Exercício 0 - Aula 4
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Testar o comando 'print()' e concatenação com dados do tipo texto e numérico utilizando o símbolo de adição '+'.

print('Olá' + 'mundo') # Olá mundo

print(7 + 4) # 11

print('7' + 4) # TypeError: can only concatenate str (not "int") to str

# Testar o comando 'print()' concatenação com dados do tipo texto e numérico utilizando a vírgula.

print('Olá', 'mundo') # Olá mundo

print(7, 4) # 11

print('7', 4) # 7 4


# Testar variáveis - atribuição de valores padrão e pela função 'input()' + visualização dos valores.

# Atribuir de forma padrão, valores as variáveis globais 'nome', 'idade' e 'peso'.

nome = 'Eric'

idade = '89'

peso = '69'

print('Nome:', nome, 'Idade:', idade, 'Peso:', peso)

# Atribuir utilizando função 'input()', valores as variáveis globais 'nome', 'idade' e 'peso'.

nome = input('Escreva seu nome: ')

idade = input(int('Digite sua idade: '))

peso = input(float('Digite seu peso '))
