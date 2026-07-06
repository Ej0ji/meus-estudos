# Exercício 18 - Aula 8
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Desenvolver um programa que leia um valor de ângulo qualquer fornecido pelo usuário e calcule o seu respectivo Seno, Cosseno e Tangente com base no círculo trigonométrico.

# IMPORTAÇÕES

from math import sin, cos, tan, radians

# LÓGICA

ang_qualquer = float(input('Insira um valor de ângulo qualquer: '))

ang_qualquer_grau_para_rad = radians(ang_qualquer)

print('-' * 30)

print('O seno de {}° é de aproximadamente {:.4f}'.format(ang_qualquer, sin(ang_qualquer_grau_para_rad)))
print('O cosseno de {}° é de aproximadamente {:.4f}'.format(ang_qualquer, cos(ang_qualquer_grau_para_rad)))
print('A tangente de {}° é de aproximadamente {:.4f}'.format(ang_qualquer, tan(ang_qualquer_grau_para_rad)))