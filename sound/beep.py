import pygame


def beep():
    pygame.mixer.init()
    pygame.mixer.music.load('sound/beep.mp3')
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():  # Wait until the sound has finished playing
        continue


