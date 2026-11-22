# Exercício 53 - Aula 13
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Criar um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

# APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

# IMPORTAÇÕES

from unidecode import unidecode # Dê o pip install unidecode

# LÓGICA

# --- Input de Dados --------------------------------------------

frase = input('Insira uma frase qualquer para ver se é palíndromo: ')

print('--' * 30)

# ----------------------------------------------------------------

# --- Inicialização de Variáveis Globais -------------------------

# Aqui seria melhor criar uma função para fazer todas as etapas de tratamento de dado, ao invés de criar várias variáveis
# Mas como devemos seguir a evolução de conhecimento do curso vamos fazer dessa forma =D

# Tratamento do Dado de Input 
frase_sem_espacos = frase.replace(' ', '')
frase_em_upper = frase_sem_espacos.upper()
frase_sem_acentos = unidecode(frase_em_upper)

# Variáveis de parâmetro
caracteres_frase = len(frase_sem_acentos)
e_palindromo = True

# ----------------------------------------------------------------

# --- Lógica de Verificação de Palíndromo ------------------------

if caracteres_frase % 2 == 0:
    indice_max = int(caracteres_frase/2)
    for i in range(0, indice_max):
        indice_fim_frase = (i+1) * -1
        if frase_sem_acentos[i] == frase_sem_acentos[indice_fim_frase]:
            print('{}ª comparação de caracteres: OK.'.format(i+1))
        else:
            e_palindromo = False
            print('{}ª comparação de caracteres: FALHOU.'.format(i+1))
else:
    indice_max = int(((caracteres_frase-1)/2)+1)
    for i in range(0, indice_max):
        indice_fim_frase = (i+1) * -1
        if frase_sem_acentos[i] == frase_sem_acentos[indice_fim_frase ]:
            print('{}ª comparação de caracteres: OK.'.format(i+1))
        else:
            e_palindromo = False
            print('{}ª comparação de caracteres: FALHOU.'.format(i+1))

# ----------------------------------------------------------------

# --- Consideração Final de Palíndromo ---------------------------

if e_palindromo == True:
    print('A frase "{}" é um palíndromo.'.format(frase))
else:
    print('A frase "{}" não é um palíndromo.'.format(frase))

# ----------------------------------------------------------------


# Esboço da Lógica:

# criar variável para armazenar a frase

# armazenar a frase

# criar variável para armazenar a versão limpa da frase

# ler a frase e limpar acentos e espaços e padronizar o formato

# armazenar a versão limpa da frase

# criar um loop de iteração que lê caractere por caractere da string da frase normalmente e que lê da mesma forma a frase, porém de trás pra frente e compara cada string para ver se elas são iguais

