import pygame
import time
import math
import random

boardX = 1200
boardY = 1200

"""
line = Block(x, y), Block(x + 1, y), Block(x + 2, y), Block(x + 3, y)
j = Block(x, y), Block(x, y + 1), Block(x + 1, y + 1), Block(x + 2, y + 1)
l = Block(x + 2, y), Block(x, y + 1), Block(x + 1, y + 1), Block(x + 2, y + 1)
o = Block(x + 1, y), Block(x + 2, y), Block(x + 1, y + 1), Block(x + 2, y + 1)
s = Block(x + 1, y), Block(x + 2, y), Block(x, y + 1), Block(x + 1, y + 1)
t = Block(x + 1, y), Block(x, y + 1), Block(x + 1, y + 1), Block(X + 2, y + 1)
z = Block(x, y), Block(x + 1, y), Block(x + 1, y + 1), Block(x + 2, y + 1)
"""
pixelsPerSpace = 10
filledPixels = 8

maxX = math.floor(boardX / pixelsPerSpace)
maxY = math.floor(boardY / pixelsPerSpace)

class Block:
    x: int
    y: int
    alive: bool
    def __init__(self, x, y, living = True) -> None:
        self.x = x
        self.y = y
        self.alive = living
    
    def die(self) -> None:
        self.alive = False
    
    def isDead(self) -> None:
        return not self.alive



class Piece:
    type: str
    rotation: int
    blocks: list[Block]
    dieCounter: int
    dead: bool
    def __init__(self) -> None:
        ranOut = random.randint(0, 6)
        if ranOut == 0:
            self.type = "line"
        elif ranOut == 1:
            self.type = "j"
        elif ranOut == 2:
            self.type = "l"
        elif ranOut == 3:
            self.type = "o"
        elif ranOut == 4:
            self.type = "s"
        elif ranOut == 5:
            self.type = "t"
        else:
            self.type = "z"
        self.rotation = 0
        self.dieCounter = 1
        self.dead = False
        pass

    def hurt(self) -> None:
        if self.dieCounter > 0:
            self.dieCounter -= 1
        else:
            for block in self.blocks:
                block.alive = False
            self.dead = True # tells our main script to delete this and add it to `dead`
    def fall(self, deadBlocks: list[Block]):
        newBlocks: list[Block] = []
        for block in self.blocks:
            newBlocks.append(Block(block.x, block.y + 1, True))
        for block in deadBlocks:
            if block in newBlocks:
                self.hurt()
                return
        self.blocks = newBlocks
    def rotate(self, clockwise: bool = True):
        maxRepeats = 4
        if clockwise: maxRepeats = 1
        for z in range(maxRepeats):
            minx = min(block.x for block in self.blocks)
            miny = min(block.y for block in self.blocks)
            maxx = max(block.x for block in self.blocks)
            maxy = max(block.y for block in self.blocks)

            self.blocks = [Block(maxx - (block.y-miny), maxy - (block.x - minx), block.alive) for block in self.blocks]
            self.rotation = (self.rotation + 1) % 4

def makeBlocks(x: int, y: int, type: str) -> list[Block]:
    if type == "line":
        return [Block(x, y), Block(x + 1, y), Block(x + 2, y), Block(x + 3, y)]
    if type == "j":
        return [Block(x, y), Block(x, y + 1), Block(x + 1, y + 1), Block(x + 2, y + 1)]
    if type == "l":
        return [Block(x + 2, y), Block(x, y + 1), Block(x + 1, y + 1), Block(x + 2, y + 1)]
    if type == "o":
        return [Block(x + 1, y), Block(x + 2, y), Block(x + 1, y + 1), Block(x + 2, y + 1)]
    if type == "s":
        return [Block(x + 1, y), Block(x + 2, y), Block(x, y + 1), Block(x + 1, y + 1)]
    if type == "t":
        return [Block(x + 1, y), Block(x, y + 1), Block(x + 1, y + 1), Block(x + 2, y + 1)]
    # default piece is Z
    return [Block(x, y), Block(x + 1, y), Block(x + 1, y + 1), Block(x + 2, y + 1)]
def draw(screen, blocks: list[Block], piece: Piece) -> None:
    aliveColour = (75, 255, 100)
    deadColour = (255, 75, 100)
    blocks += piece.blocks
    for block in blocks:
        colour = aliveColour
        if (block.isDead()): colour = deadColour
        rect = pygame.Rect(block.x * pixelsPerSpace + 1, block.y * pixelsPerSpace + 1, filledPixels, filledPixels)
        pygame.draw.rect(screen, colour, rect)
    pass

def main():

    screen = pygame.display.set_mode((boardX, boardY)) 

    pygame.display.set_caption("Tetris") 

    pygame.display.flip() 

    running = True

    score: int = 0
    piece: Piece = Piece()
    piece.blocks = makeBlocks(math.floor(maxX / 2), math.floor(maxY / 2), piece.type)
    deads = []
    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == 120:
                    piece.rotate()
                elif event.key == 99:
                    piece.rotate(False)
        piece.fall(deads)
        if piece.dead:
            deads += piece.blocks
            piece = Piece()
            piece.blocks = makeBlocks(math.floor(maxX / 2), math.floor(maxY / 2), piece.type)
        screen.fill(0)
        draw(screen, deads, piece)
        pygame.display.flip()
        time.sleep(1)

main()