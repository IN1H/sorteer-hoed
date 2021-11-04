
from tkinter import *
import pygame

pygame.mixer.init()

def play():

    pygame.mixer.music.load("assets/Harry_Potter_theme.wav")
    pygame.mixer.music.play(loops = 0)

