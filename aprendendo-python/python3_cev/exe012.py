# Exercício 12 - Aula 7
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Ler o preço de um produto e mostrar seu novo preço com 5% de desconto.


preco_produto = float(input('Digite o valor do produto: R$'))

print('-' * 30)

print('O produto de valor igual a R${}, com o desconto de 5%, passará a ter o valor de R${:.2f}.'.format(preco_produto, (preco_produto - preco_produto * 0.05)))