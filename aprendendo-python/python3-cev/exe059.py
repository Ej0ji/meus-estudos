# Exercício 58 - Aula 14
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Criar um programa que leia dois valores e mostre um menu na tela seu programa deverá realizar a operação solicitada em cada caso:

# [ 1 ] somar

# [ 2 ] multiplicar

# [ 3 ] maior

# [ 4 ] novos números

# [ 5 ] sair do programa

# IMPORTAÇÕES

from time import sleep

# LÓGICA

# --- Input dos Dados -----------------------------------------------------------

print('-' * 71)
print(' ======================== Calculadora Simples ========================')
print('-' * 71)

opcao_acao = 0

valor_1 = float(input('\nDigite o valor 1: '))

valor_2 = float(input('\nDigite o valor 2: '))

# -------------------------------------------------------------------------------

# --- Lógica da calculadora -----------------------------------------------------

while opcao_acao != 5:
    print()
    print('-' * 71)
    print(' ==== Digite o número da operação desejada entre ambos os valores ====')
    print('-' * 71)
    print('\n[ 1 ] somar')
    print('\n[ 2 ] multiplicar')
    print('\n[ 3 ] maior')
    print('\n[ 4 ] novos valores')
    print('\n[ 5 ] sair do programa')

    opcao_acao = int(input('\nOpção: '))

    if opcao_acao == 1:
        resultado = valor_1 + valor_2
        print('A soma entre o valor 1 ({}) e o valor 2 ({}) é igual a {}.'.format(valor_1, valor_2, resultado))
        sleep(3)

    elif opcao_acao == 2:
        resultado = valor_1 * valor_2
        print('A multiplicação entre o valor 1 ({}) e o valor 2 ({}) é igual a {}.'.format(valor_1, valor_2, resultado))
        sleep(3)
        
    elif opcao_acao == 3:
        if valor_1 > valor_2:
            resultado = valor_1
        else:
            resultado = valor_2
        print('Entre o valor 1 ({}) e o valor 2 ({}), o maior valor é {}.'.format(valor_1, valor_2, resultado))
        sleep(3)
        
    elif opcao_acao == 4:
        print('=========== Digite os novos valores ===========')

        valor_1 = float(input('\nDigite o valor 1: '))

        valor_2 = float(input('\nDigite o valor 2: '))
        sleep(1)
        
    else:
        if opcao_acao != 5:
            print('Valor inválido. Digite alguma das opções!')

# -------------------------------------------------------------------------------
    
