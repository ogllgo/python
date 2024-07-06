import pygame
import math
import random
import time
screenX = 500
screenY = 750

screenX = math.floor(screenX / 10) * 10
screenY = math.floor(screenY / 10) * 10

pixelsPerSquare = 12
filledPixels = 10

maxX = math.floor(screenX / pixelsPerSquare) - 1
maxY = math.floor(screenY / pixelsPerSquare) - 1

screen = pygame.display.set_mode((screenX, screenY))
pygame.display.flip()

pygame.display.set_caption("Snake")


def drawApples(surface, apples: list[tuple[int, int]]):
    colour = (255,0,0)
    for apple in apples: 
        [x, y] = apple
        shape = pygame.Rect(x*pixelsPerSquare+1, y*pixelsPerSquare+1, filledPixels, filledPixels)
        pygame.draw.rect(surface, colour, shape)
def drawSnake(surface, snake: list[tuple[int, int]]):
    colour = (25,250,75)
    for segment in snake: 
        [x, y] = segment
        shape = pygame.Rect(x*pixelsPerSquare+1, y*pixelsPerSquare+1, filledPixels, filledPixels)
        pygame.draw.rect(surface, colour, shape)

def moveSnake(snake: list[tuple[int, int]], direction: str, desiredLength: int):
    oldSnake = snake
    if (len(snake) >= desiredLength):
        oldSnake = snake[0:-1]
    first = snake[0]
    first = snake[0]
    if (direction == "r"):
        snake = [(snake[0][0]+1, snake[0][1]), *oldSnake]
    elif (direction == "s"):
        snake = [(snake[0][0], snake[0][1]+1), *oldSnake]
    elif (direction == "l"):
        snake = [(snake[0][0]-1, snake[0][1]), *oldSnake]
    elif (direction == "u"):
        snake = [(first[0], first[1]-1), *oldSnake]
    else:
        snake = [(first[0]+1, first[1]), *oldSnake]
    return snake

def makeApple(avoid: list[tuple[int, int]]) -> bool | tuple[int, int]:
    guess = (random.randint(0, maxX), random.randint(0, maxY))
    i=0
    while pointsColliding(avoid, guess):
        i += 1
        if i >= 1000:
            return False
        guess = (random.randint(0, maxX), random.randint(0, maxY))
    return guess

def pointsColliding(points: list[tuple[int, int]], point: tuple[int, int]): return point in points



running = True
apples: list[tuple[int, int]] = []
snake: list[tuple[int, int]] = [(0, 0)]
desiredAppleAmount = 3
dir = ""
desiredSnakeLength = 5
moveDelay = time.time()
while running:
    for i in range(len(apples)):
        apple = apples[i]
        if (pointsColliding(snake, apple)): 
            apples[i] = makeApple(snake + apples)
            desiredSnakeLength += 1
    screen.fill((0, 0, 0))
    while len(apples) < desiredAppleAmount:
        apple = makeApple(apples + snake)
        if apple: apples.append(apple)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            dir = event.key
            if (dir == 115): dir = "s"
            elif (dir == 119): dir = "u"
            elif (dir == 97): dir = "l"
            elif (dir == 100): dir = "r"
    if (time.time() > moveDelay):
        snake = moveSnake(snake, dir, desiredSnakeLength)
        moveDelay += 0.1
    drawApples(screen, apples)
    drawSnake(screen, snake)
    pygame.display.flip()
    if snake[0][0] < 0 or snake[0][1] < 0 or snake[0][0] > maxX or snake[0][1] > maxY:
        running = False
    for segment in snake[1:]:
        if (segment == snake[0]):
            running = False