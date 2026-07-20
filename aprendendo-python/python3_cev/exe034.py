# Exercício 34 - Aula 10
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Desenvolver um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('VALIDADOR DE EXISTÊNCIA DE TRIÂNGULO')

print('-' * 40)

retas = []
reta = float(input('Digite o valor da reta a do triângulo: '))
retas.append(reta)
reta = float(input('Digite o valor da reta b do triângulo: '))
retas.append(reta)
reta = float(input('Digite o valor da reta c do triângulo: '))
retas.append(reta)

print('-' * 40)

if (abs(retas[1] - retas[2]) < retas[0] and retas[0] < retas[1] + retas[2]) and (abs(retas[0] - retas[2]) < retas[1] and retas[1] < retas[0] + retas[2]) + (abs(retas[0] - retas[1]) < retas[2] and retas[2] < retas[0] + retas[1]):
    print('O triângulo com os lados a = ({}), b = ({}) e c = ({}) existe!'.format(retas[0], retas[1], retas[2]))

else:
    print('os lados a = ({}), b = ({}) e c = ({}) não satisfazem a existência de um triângulo!'.format(retas[0], retas[1], retas[2]))