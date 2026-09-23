import pygame
import time
import os

print('== CHALLENGE 21 ==')

dire = os.path.dirname(os.path.abspath(__file__))
cam = os.path.join(dire, 'KIB_mp3Test.mp3')

pygame.mixer.init()
pygame.mixer.music.load(cam)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    time.sleep(1)
