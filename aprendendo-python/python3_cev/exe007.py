# Exercício 7 - Aula 7
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Ler duas notas de um aluno, calcular e mostrar a sua média (atenção à precedência ao somar as notas antes de dividir).

nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))

media = (nota1 + nota2) / 2

print('-' * 30)

print('A nota média do aluno foi {:.2f}'.format(media))