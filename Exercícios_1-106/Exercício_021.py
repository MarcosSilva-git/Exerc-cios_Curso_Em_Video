import pygame
pygame.init()
pygame.mixer_music.load('Anna_Julia_Letra.mp3')
pygame.mixer_music.set_volume(0.4)
pygame.mixer_music.play(0)
# a = input('Aperte enter para terminar a música')
pygame.event.wait()
