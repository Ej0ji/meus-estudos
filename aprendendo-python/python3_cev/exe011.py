# Exercício 11 - Aula 7
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Ler a largura e a altura de uma parede em metros, calcular a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

print('Vamos calcular quantos litros de tinta precisaremos para pintar uma parede!')

print('-' * 45)

largura_parede = float(input('Qual a largura da parede em metros?: '))
altura_parede = float(input('Qual a altura da parede em metros?: '))

area_parede = largura_parede * altura_parede

litros_tinta_por_parede = area_parede / 2

print('-' * 45)
print('Para pintar a sua parede de {}m², serão necessários {}L de tinta.'.format(area_parede, litros_tinta_por_parede))
