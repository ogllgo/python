import pygame
import time
import math
import random

pixelsPerSpace = 10
filledPixels = 8

boardX = 10 * pixelsPerSpace
boardY = 20 * pixelsPerSpace

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
    def move(self, left: bool, dead: list[Block]) -> None:
        if left:
            for block in dead:
                if any([liveBlock.x - 1 == block.x and liveBlock.y == block.y for liveBlock in self.blocks]):
                    return
            if min([block.x for block in self.blocks]) > 0 :
                self.blocks = [Block(block.x - 1, block.y, block.alive) for block in self.blocks]
        else:
            for block in dead:
                if any([liveBlock.x + 1 == block.x and liveBlock.y == block.y for liveBlock in self.blocks]):
                    return
            if max([block.x for block in self.blocks]) < maxX:
                self.blocks = [Block(block.x + 1, block.y, block.alive) for block in self.blocks]
        
    def hurt(self) -> None:
        if self.dieCounter > 0:
            self.dieCounter -= 1
        else:
            for block in self.blocks:
                block.alive = False
            self.dead = True # tells our main script to delete this and add it to `dead`
    def fall(self, deadBlocks: list[Block]):
        newBlocks = [Block(block.x, block.y + 1, block.alive) for block in self.blocks]

        for newBlock in newBlocks:
            for deadBlock in deadBlocks:
                if newBlock.x == deadBlock.x and newBlock.y == deadBlock.y:
                    self.hurt()
                    return

        if any([block.y == maxY for block in newBlocks]):
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

            self.blocks = [Block(maxx - (block.y-miny), maxy + (block.x - minx), block.alive) for block in self.blocks]
            self.rotation = (self.rotation + 1) % 4

def makeBlocks(x: int, y: int, type: str, dead: list[Block]) -> list[Block] | bool:
    if any([block.x == x and block.y == y for block in dead]):
        return False
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
def draw(screen, deadBlocks: list[Block], piece: Piece):
    aliveColour = (75, 255, 100)
    deadColour = (255, 75, 100)

    for block in deadBlocks:
        colour = deadColour
        rect = pygame.Rect(block.x * pixelsPerSpace + 1, block.y * pixelsPerSpace + 1, filledPixels, filledPixels)
        pygame.draw.rect(screen, colour, rect)

    for block in piece.blocks:
        colour = aliveColour
        rect = pygame.Rect(block.x * pixelsPerSpace + 1, block.y * pixelsPerSpace + 1, filledPixels, filledPixels)
        pygame.draw.rect(screen, colour, rect)

def main():
    score: int = 0
    piece: Piece = Piece()
    piece.blocks = makeBlocks(math.floor(maxX / 2), 0, piece.type, [])
    deads = []
    fallTime = time.time()

    screen = pygame.display.set_mode((boardX, boardY)) 
    pygame.display.set_caption("Tetris") 
    pygame.display.flip() 

    running = True
    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    piece.rotate()
                elif event.key == pygame.K_a:
                    piece.move(True, deads)
                elif event.key == pygame.K_d:
                    piece.move(False, deads)
        if fallTime < time.time():
            piece.fall(deads)
            fallTime = time.time() + 0.3
        if piece.dead:
            deads += piece.blocks
            piece = Piece()
            if (not makeBlocks(math.floor(maxX / 2), 0, piece.type, [])):
                pygame.quit()
                return
            piece.blocks = makeBlocks(math.floor(maxX / 2), 0, piece.type, [])
        
        screen.fill((0, 0, 0))
        draw(screen, deads, piece)
        pygame.display.flip()
    pygame.quit()

main()