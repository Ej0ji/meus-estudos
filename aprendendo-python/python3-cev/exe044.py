# Exercício 44 - Aula 12
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Criar um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#
# – à vista dinheiro/cheque: 10% de desconto
#
# – à vista no cartão: 5% de desconto
#
# – em até 2x no cartão: preço formal 
#
# – 3x ou mais no cartão: 20% de juros

# IMPORTAÇÕES

import random

# LÓGICA

print('Calculadora de pagamento por produto')
print('-' * 40)

# O conceito de dicionário ainda não foi abordado durante o curso com profundidade, assim como as listas também não foram. Porém para este exercício é interessante que haja a presença deste tipo de variável para agregar maior qualidade para o presente exercício.
produtos = {'Geladeira': 2170.50,
            'Fogão': 599.50,
            'Armário': 876.99,
            'Microondas': 499.75}

# Seleção aleatória de produto com valor do dicionário de produtos.
produto_aleatorio = random.choice(list(produtos))
valor_produto = produtos[produto_aleatorio]

print('O produto escolhido foi o {}. O mesmo custa R${}!'.format(produto_aleatorio, valor_produto))

metodo_pagamento = int(input('''Qual será o método de pagamento?

1 – À vista dinheiro/cheque: 10% de desconto

2 – À vista no cartão: 5% de desconto

3 – Em até 2x no cartão: preço formal

4 - 3x ou mais no cartão: 20% de juros

(Digite o número de uma das opções): '''))

print('-' * 40)

valor_produto_alterado = 0

if metodo_pagamento == 1:

    valor_alteracao = valor_produto * 0.1 
    valor_produto_alterado = valor_produto - valor_alteracao

    print('Com o pagamento à vista no dinheiro/cheque, o valor total do(a) {} é de R${:.2f}! (valor formal (R${:.2f}) - 10% (R${:.2f}).'.format(produto_aleatorio, valor_produto_alterado, valor_produto, valor_alteracao))

elif metodo_pagamento == 2:

    valor_alteracao = valor_produto * 0.05
    valor_produto_alterado = valor_produto - valor_alteracao

    print('Com o pagamento à vista no cartão, o valor total do(a) {} é de R${:.2f}! (valor formal (R${:.2f}) - 5% (R${:.2f}).'.format(produto_aleatorio, valor_produto_alterado, valor_produto, valor_alteracao))

elif metodo_pagamento == 3:

    valor_alteracao = valor_produto * 0
    valor_produto_alterado = valor_produto - valor_alteracao

    print('Com o pagamento em até 2x no cartão, o valor total do(a) {} é de R${:.2f}! (valor formal (R${:.2f}).'.format(produto_aleatorio, valor_produto_alterado, valor_produto))

elif metodo_pagamento == 4:

    valor_alteracao = valor_produto * 0.2
    valor_produto_alterado = valor_produto + valor_alteracao

    print('Com o pagamento em até 3x ou mais, no cartão, o valor total do(a) {} é de R${:.2f}! (valor formal (R${:.2f}) + 20% (R${:.2f})).'.format(produto_aleatorio, valor_produto_alterado, valor_produto, valor_alteracao))


