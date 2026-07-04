# Exercício 14 - Aula 7
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Escrever um programa que converta uma temperatura digitada em °C e converta para °F.

valor_graus_C = float(input('Digite o valor em graus Célsius: '))

valor_C_para_F = (valor_graus_C * 1.8) + 32

print('-' * 40)

# A fórmula é assim devido à diferença no tamanho dos graus e no ponto de partida (zero) de cada escala.

# A estrutura dividida explica essa relação matemática: A escala Celsius e a escala Fahrenheit possuem intervalos diferentes entre o ponto de congelamento e o ponto de ebulição da água:

# Celsius: Vai de 0°C a 100°C (intervalo de 100 graus).
# Fahrenheit: Vai de 32°F a 212°F (intervalo de 180 graus).
 
# Dividindo o intervalo de Fahrenheit pelo de Celsius (180/100), chegamos à razão de 1,8. Isso significa que cada 1°C varia o equivalente a 1,8°F.

# Agora, por que somar 32? (O ponto de partida)
# As duas escalas não começam a contar o calor do mesmo ponto:

# A água congela a 0°C.
# A água congela a 32°F.

# Como a escala Fahrenheit já começa no 32 quando a Celsius está no zero, você precisa somar 32 após ajustar o tamanho dos graus para corrigir esse "atraso".

print('A temperatura atual em graus Célsius de {}°C, convertida para Fahrenheit, é de {:.1f}°F'.format(valor_graus_C, valor_C_para_F))