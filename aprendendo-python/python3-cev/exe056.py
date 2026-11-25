# Exercício 55 - Aula 13
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Desenvolver um programa que leia o nome, idade e sexo de n pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

# LÓGICA

# --- Input de Dados e Inicialização de Variáveis Globais ----------------------------

soma_idades = 0
homem_mais_velho = ''
idade_homem_mais_velho = 0
qtd_mulheres_sub_20 = 0

qtd_pessoas = int(input('Quantas pessoas serão inseridas para análise?: '))
print('--' * 30)

# ------------------------------------------------------------------------------------

# --- Lógica de análises -------------------------------------------------------------

for i in range(qtd_pessoas):
    nome_pessoa = input('Digite o nome da {}a pessoa: '.format(i+1))
    idade_pessoa = int(input('Agora a idade dela: '))
    sexo_pessoa = input('Por fim, o sexo. Digite M para masculino ou F para feminino): ')

    soma_idades += idade_pessoa

    if sexo_pessoa.casefold() == 'm' and idade_pessoa > idade_homem_mais_velho:
        homem_mais_velho = nome_pessoa
        idade_homem_mais_velho = idade_pessoa

    if sexo_pessoa.casefold() == 'f' and idade_pessoa < 20:
        qtd_mulheres_sub_20 += 1
    
media_idade_pessoas = round((soma_idades / qtd_pessoas), 1)

# ------------------------------------------------------------------------------------

# --- Saída Final --------------------------------------------------------------------

print('--' * 30)
print('O grupo de {} pessoas possui os seguintes números:\n'.format(qtd_pessoas))
print('Média de idades do grupo: {}.'.format(media_idade_pessoas))

if homem_mais_velho == '':
    print('Não exite homens nesse grupo.')
else:
    print('O homem mais velho do grupo é o {}, com seus {} anos.'.format(homem_mais_velho, idade_homem_mais_velho))

print('A quantidade de mulheres com menos de 20 anos é: {}.'.format(qtd_mulheres_sub_20))

# ------------------------------------------------------------------------------------