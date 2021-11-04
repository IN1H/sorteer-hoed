import pygame

def play():

    pygame.mixer.init()
    pygame.mixer.music.load("assets/Harry_Potter_theme.wav")
    pygame.mixer.music.play(loops = 0)

