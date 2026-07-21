# Exercício 33 - Aula 10
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Escrever um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario_funcionario = float(input('Insira o valor do salário para calcular o aumento: '))
novo_salario_funcionario = 0

print('-' * 40)

faixa_salarial = 1250
taxa_aumento_para_maior_faixa = 0.10
taxa_aumento_para_menor_igual_faixa = 0.15

if salario_funcionario > faixa_salarial:

    novo_salario_funcionario = salario_funcionario + (salario_funcionario * taxa_aumento_para_maior_faixa)

    print('O seu salário de R${:.2f} receberá um aumento de {:.0f}%, passando a ser R${:.2f}!'.format(salario_funcionario, (taxa_aumento_para_maior_faixa * 100), novo_salario_funcionario))

else:

    novo_salario_funcionario = salario_funcionario + (salario_funcionario * taxa_aumento_para_menor_igual_faixa)

    print('O seu salário de R${:.2f} receberá um aumento de {:.0f}%, passando a ser R${:.2f}!'.format(salario_funcionario, (taxa_aumento_para_menor_igual_faixa * 100), novo_salario_funcionario))

