# Exercício 43 - Aula 12
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Desenvolver uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#
# – IMC abaixo de 18,5: Abaixo do Peso
#
# – Entre 18,5 e 25: Peso Ideal
# 
# – 25 até 30: Sobrepeso
#
# – 30 até 40: Obesidade
#
# – Acima de 40: Obesidade Mórbida

print('Calculadora de IMC')
print('-' * 40)

peso = float(input('Digite o seu peso (kg): '))
altura = float(input('Digite a sua altura (m): '))

imc = peso / altura ** 2

print('-' * 40)

print('Com base no seu peso, {}kg e altura, {}m seu IMC = {:.2f}, indica que você está '.format(peso, altura, imc))

if imc < 18.5:
    print('ABAIXO DO PESO!')
elif imc >= 18.5 and imc <= 25:
    print('COM PESO IDEAL!')
elif imc > 25 and imc <= 30:
    print('COM SOBREPESO!')
elif imc > 30 and imc <= 40:
    print('COM OBESIDADE!')
elif imc > 40:
    print('COM OBESIDADE MÓRBIDA!')