# Exercício 13 - Aula 7
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Ler o salário de um funcionário e mostrar seu novo salário com 15% de aumento.

salario_atual = float(input('Digite o salário do funcionário: R$'))

print()

novo_salario = salario_atual * 1.15

print('O salário do funcionário reajustado em 15% é de R${}'.format(novo_salario))