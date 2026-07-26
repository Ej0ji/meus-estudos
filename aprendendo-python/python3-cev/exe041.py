# Exercício 41 - Aula 12
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# A Confederação Nacional de Natação precisa de um programa.
# 
# Escrever um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#
# – Até 9 anos: MIRIM
#
# – Até 14 anos: INFANTIL
#
# – Até 19 anos: JÚNIOR
#
# – Até 25 anos: SÊNIOR
#
# – Acima de 25 anos: MASTER

print('Categorização de atletas por idade')
print('-' * 40)

idade_atleta = int(input('Digite a idade do atleta: '))

print('-' * 40)

if idade_atleta <= 9:
    print('Atleta de {} anos = MIRIM'.format(idade_atleta))
elif idade_atleta > 9 and idade_atleta <= 14:
    print('Atleta de {} anos = INFANTIL'.format(idade_atleta))
elif idade_atleta > 14 and idade_atleta <= 19:
    print('Atleta de {} anos = JÚNIOR'.format(idade_atleta))
elif idade_atleta > 19 and idade_atleta <= 25:
    print('Atleta de {} anos = SÊNIOR'.format(idade_atleta))
elif idade_atleta > 25:
    print('Atleta de {} anos = MASTER'.format(idade_atleta))
