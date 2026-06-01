# Desafio 000 - Aula 4
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Criar um script que leia o nome de uma pessoa e mostra uma mensagem de boas-vindas de acordo com o valor digitado.

print('*Exercício 1* - Script que recebe o nome do usuário e dá boas-vindas ao usuário indicado:\n')

nomeUsuario = input(str('Insira seu nome: '))

print(f'Seja muito bem-vindo, {nomeUsuario}!\n')

# Criar um script que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.

print('*Exercício 2* - Script que recebe o dia, mês e ano de nascimento do usuário e ao final mostra a data formatada na data no padrão brasileiro de datas:\n')

diaNascUsuario = int(input('Digite o seu dia de nascimento: '))
mesNascUsuario = int(input('Digite o seu mês de nascimento: '))
anoNascUsuario = int(input('Digite o seu ano de nascimento: '))

print(f'Sua data de nascimento completa é: {diaNascUsuario}/{mesNascUsuario}/{anoNascUsuario}\n')

# Criar um script que leia dois números inteiros e tente mostrar a soma entre eles.

print('*Exercício 3* - Script que recebe dois números inteiros e mostra a soma entre eles:\n')

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
resultado = num1 + num2

print(f'A soma entre o {num1} e o {num2} é igual a {resultado}!')