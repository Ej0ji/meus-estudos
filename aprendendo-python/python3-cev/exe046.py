# Exercício 46 - Aula 12
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Fazer um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

# IMPORTAÇÕES

from time import sleep

# LÓGICA

print('Começando a contagem dos fogos!!')
sleep(1)

for contador in range(10, 0, -1):
    sleep(1)
    print(contador)

sleep(1)
print('*Fogos estourando!!*')