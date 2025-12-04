import pygame
import time

#inicializa o mixer de áudio
pygame.mixer.init()

#carrega o arquivo MP3 (Troque "musica.mp3" pelo nome do seu arquivo)
pygame.mixer.music.load('musica.mp3')

#Reproduz o áudio
pygame.mixer.music.play()

#Mantém o programa aberto até a música terminar
while pygame.mixer.music.get_busy():
    time.sleep(1)

# pygame.mixer.init() inicializa o sistema de áudio
# pygame.mixer.music.load() carrega o arquivo
# pygame.mixer.music.play() toca
# O While serve para não deixar o programa fechar antes do áudio terminar
