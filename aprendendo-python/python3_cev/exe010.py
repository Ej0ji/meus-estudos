# Exercício 10 - Aula 7
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Ler quanto dinheiro uma pessoa tem na carteira (em reais) e mostrar quantos dólares ela pode comprar (cotação utilizada na época: US$ 1.00 = R$ 3,27).

carteira_em_reais = float(input('Insira o valor de sua carteira em reais (R$): '))
cotacao_dolar = 3.27
conversao_real_para_dolar = carteira_em_reais / cotacao_dolar

print('Com o valor total de R${:.2f} de sua carteira é possível comprar um total de US$ {:.2f} (COTAÇÃO ATUAL DO DÓLAR = {}).'.format(carteira_em_reais, conversao_real_para_dolar, cotacao_dolar))