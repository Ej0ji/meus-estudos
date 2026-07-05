# Exercício 17 - Aula 8
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Desenvolva um programa que receba o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. O script deve calcular e exibir o comprimento exato da hipotenusa. Dica: Há uma fórmula matemática tradicional (a² + b² = c²), mas também existe uma função específica dentro do módulo math que resolve isso instantaneamente.

# RESOLUÇÃO 1 - Sem módulos -------------------------------------------------

print('Insira os valores a seguir.')

print('-' * 40)

cat_oposto = float(input('Insira o valor do cateto oposto do triângulo: '))
cat_adjacente = float(input('Insira o valor do cateto adjacente do triângulo: '))

print('O valor da hipotenusa do triângulo cujo comprimento do cateto oposto é {} e do cateto adjacente {}, é igual a {}'.format(cat_oposto, cat_adjacente, (cat_oposto ** 2 + cat_adjacente ** 2) ** 0.5))

# RESOLUÇÃO 2 - Com módulos --------------------------------------------------

# IMPORTS

from math import hypot

# LÓGICA

print('Insira os valores a seguir.')

print('-' * 40)

cat_oposto = float(input('Insira o valor do cateto oposto do triângulo: '))
cat_adjacente = float(input('Insira o valor do cateto adjacente do triângulo: '))

print('O valor da hipotenusa do triângulo cujo comprimento do cateto oposto é {} e do cateto adjacente {}, é igual a {}'.format(cat_oposto, cat_adjacente, hypot(cat_oposto, cat_adjacente)))