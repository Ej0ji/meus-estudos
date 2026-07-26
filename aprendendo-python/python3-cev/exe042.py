# Exercício 42 - Aula 12
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Refazer o DESAFIO 34 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#
# – EQUILÁTERO: todos os lados iguais
#
# – ISÓSCELES: dois lados iguais, um diferente
#
# – ESCALENO: todos os lados diferentes

print('VALIDADOR DE EXISTÊNCIA DE TRIÂNGULO V2')

print('-' * 40)

retas = []
retas.append(float(input('Digite o valor da reta a do triângulo: ')))
retas.append(float(input('Digite o valor da reta b do triângulo: ')))
retas.append(float(input('Digite o valor da reta c do triângulo: ')))

print('-' * 40)

if (abs(retas[1] - retas[2]) < retas[0] and retas[0] < retas[1] + retas[2]) and (abs(retas[0] - retas[2]) < retas[1] and retas[1] < retas[0] + retas[2]) + (abs(retas[0] - retas[1]) < retas[2] and retas[2] < retas[0] + retas[1]):
                        
    print('O triângulo com os lados a = ({}), b = ({}) e c = ({}) existe!'.format(retas[0], retas[1], retas[2]))

    if (retas[0] == retas[1]) and (retas[1] == retas[2]) and (retas[2] == retas[0]):
        print('Este é um triângulo EQUILÁTERO! Apresentando todos os lados iguais!')
    elif (retas[0] == retas[1]) or (retas[1] == retas[2]) or (retas[2] == retas[0]):
        print('Este é um triângulo ISÓSCELES! Apresentando ao menos um lados iguais!')
    elif (retas[0] != retas[1]) and (retas[1] != retas[2]) and (retas[2] != retas[0]):
        print('Este é um triângulo ESCALENO! Apresentando todos os lados diferentes entre si!')

else:
    print('os lados a = ({}), b = ({}) e c = ({}) não satisfazem a existência de um triângulo!'.format(retas[0], retas[1], retas[2]))




