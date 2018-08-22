import pygame

pygame.init()
pygame.mixer.music.load('aula08_g_Desafio21.mp3')
pygame.mixer.music.play()
pygame.event.wait()

print('Tocando a musica...')