# Exercício 30 - Aula 10
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Desenvolver um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.

distancia_viagem = float(input('Insira a distância (em kms) que sua viagem terá: '))

print('-' * 40)

preco_passagem = 0
valor_ate_200km = 0.5
valor_maior_200km = 0.45

if distancia_viagem <= 200:

    preco_passagem = distancia_viagem * valor_ate_200km

else:
    
    preco_passagem = distancia_viagem * valor_maior_200km

print('Com base na distância que sua viagem terá ({}kms). O valor calculado para a passagem é de R${}.'.format(distancia_viagem, preco_passagem))