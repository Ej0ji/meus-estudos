# Exercício 15 - Aula 7
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Escrever um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km_percorridos = float(input('Quantos KMs o seu carro percorreu?: '))

dias_alugados = float(input('E por quantos dias você alugou o carro?: '))

valor_a_pagar_total = (km_percorridos * 0.15) + (dias_alugados * 60)

print('-' * 40)

print('O valor total a pagar pelo aluguel do carro será de R${:.2f}'.format(valor_a_pagar_total))
print('CÁLCULO UTILIZADO: (KMs percorridos ({}kms) * R$0.15) + (Dias alugados ({} dias) * R$60) = Valor total do aluguel'.format(km_percorridos, dias_alugados))