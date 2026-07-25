# Exercício 40 - Aula 12
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Criar um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#
# – Média abaixo de 5.0: REPROVADO
#
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
#
# – Média 7.0 ou superior: APROVADO

# IMPORTAÇÕES

# LÓGICA

print('Verificação de média bimestral')
print('-' * 40)

notas = []

notas.append(float(input('Digite a primeira nota: ')))
notas.append(float(input('Digite a segunda nota: ')))

media_bim = sum(notas) / len(notas)

media_de_reprova = 5
media_de_aprovacao = 7
media_de_recuperacao = media_bim >= media_de_reprova and media_bim < media_de_aprovacao

print('-' * 40)

if media_bim < media_de_reprova:
    print('REPROVADO! A média bimestral, {} é menor que {}'.format(media_bim, media_de_reprova))
elif media_de_recuperacao:
    print('RECUPERAÇÃO! A média bimestral, {} está entre {} e menos que {}'.format(media_bim, media_de_reprova, media_de_aprovacao))
elif media_bim >= media_de_aprovacao:
    print('APROVADO! A média bimestral, {} é maior ou igual a {}'.format(media_bim, media_de_aprovacao))

