# Exercício 36 - Aula 12
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Escrever um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa deve perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcular o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

print('Vamos verificar se você está apto para receber o empréstimo para compra de imóvel!')

print('-' * 45)

valor_casa = float(input('Insira o valor da sua casa desejada: R$'))
salario_comprador = float(input('Agora o seu salário: R$'))
anos_parcelas = int(input('Por último, dê uma quantidade inteira de anos para pagar tudo: '))

prestacao_mensal = valor_casa / (anos_parcelas * 12)

valor_permitido = (salario_comprador * 0.3)

if prestacao_mensal > valor_permitido:
    print('Com base no seu salário, seu empréstimo não foi aprovado!')
else:
    print('Com base no seu salário, seu empréstimo foi aprovado')