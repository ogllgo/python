import pygame
import math
import random
import time

screenX = 500
screenY = 750

def makeBlock():
    number = random.randint(0, 6)
    if number == 0:
        return "l"
    if number == 1:
        return "j"
    if number == 2:
        return "l"
    if number == 3:
        return "o"
    if number == 4:
        return "s"
    if number == 5:
        return "t"
    return "z"

screenX = math.floor(screenX / 10) * 1
screenY = math.floor(screenY / 10) * 10

pixelsPerSquare = 12
filledPixels = 10

screen = pygame.display.set_mode((screenX, screenY))
pygame.display.flip()

pygame.display.set_caption("Tetris")

running = True
while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False