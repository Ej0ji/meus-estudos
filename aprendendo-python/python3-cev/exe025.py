# Exercício 25 - Aula 9
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Fazer um programa que leia uma frase e exiba quantas vezes aparece uma letra especificada pelo usuário, em que posição ela aparece a primeira vez e em que posição ela surge pela última vez.

frase = input('Digite uma frase qualquer: ').strip()
letra_a_ser_buscada = input('Digite uma letra para buscar dentro da frase: ').strip()

print('-' * 45)

frase_transformada = frase.lower()
letra_a_ser_buscada_transformada = letra_a_ser_buscada.lower()

contagem_de_letras_A = frase_transformada.count(letra_a_ser_buscada_transformada)
primeira_letra_A = frase_transformada.find(letra_a_ser_buscada_transformada)
ultima_letra_A = frase_transformada.rfind(letra_a_ser_buscada_transformada)

print('''A quantidade de letras "A" apresentadas na frase "{}" é de {}.
E a primeira aparição da letra é na posição {}.
Já a última é na posição {}.'''.format(frase, contagem_de_letras_A, (primeira_letra_A + 1), (ultima_letra_A + 1))) 

