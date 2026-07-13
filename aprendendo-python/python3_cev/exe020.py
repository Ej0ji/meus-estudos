# Exercício 20 - Aula 8
# Utilize as aspas triplas (''' ''') ou hashtag (#) para comentar e testar cada comando linha a linha.

# Escrever um programa em Python que abra e reproduza o áudio de um arquivo MP3.

# RESOLUÇÃO 1 - Com pygame -------------------------------------------------

# IMPORTAÇÕES

import pygame

# LÓGICA

# Inicializa o mixer do pygame
pygame.mixer.init()

# Carrega o arquivo MP3 (substitua pelo nome do seu arquivo)
pygame.mixer.music.load('C:/Users/ericj/OneDrive/Documents/GitHub/meus-estudos/aprendendo-python/python3_cev/assets/faaah.mp3')

# Inicia a reprodução
pygame.mixer.music.play()

# Mantém o programa rodando enquanto a música toca
input('Pressione Enter para parar a música...')


# RESOLUÇÃO 2 - Com playsound3 ---------------------------------------------

# IMPORTAÇÕES

import playsound3

# LÓGICA

playsound3.playsound('C:/Users/ericj/OneDrive/Documents/GitHub/meus-estudos/aprendendo-python/python3_cev/assets/faaah.mp3')