import pygame
import time
import math
import random

pixelsPerSpace = 20
filledPixels = 16

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
            if max([block.x for block in self.blocks]) < maxX - 1:
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
    def rotate(self, deads: list[Block], clockwise: bool = True):
        maxRepeats = 4
        if clockwise: maxRepeats = 1
        before = self.blocks

        for z in range(maxRepeats):
            minx = min(block.x for block in self.blocks)
            miny = min(block.y for block in self.blocks)
            maxx = max(block.x for block in self.blocks)
            maxy = max(block.y for block in self.blocks)

            self.blocks = [Block(maxx - (block.y-miny), maxy + (block.x - minx), block.alive) for block in self.blocks]
            self.rotation = (self.rotation + 1) % 4
            while max(block.y for block in self.blocks) > maxy:
                self.blocks = [Block(block.x, block.y - 1, block.alive) for block in self.blocks]
            while min(block.x for block in self.blocks) < 0:
                self.blocks = [Block(block.x + 1, block.y, block.alive) for block in self.blocks]
            while max(block.x for block in self.blocks) > maxX:
                self.blocks = [Block(block.x - 1, block.y, block.alive) for block in self.blocks]
        for block in deads:
            if block in self.blocks:
                self.blocks = before
                return

def makeBlocks(x: int, y: int, type: str, dead: list[Block]) -> list[Block]:
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
def draw(screen, deadBlocks: list[Block], piece: Piece, colours = list[tuple[int, int, int]]):
    dead_colour, alive_colour = colours
    for block in deadBlocks:
        colour = dead_colour
        rect = pygame.Rect(block.x * pixelsPerSpace + 1, block.y * pixelsPerSpace + 1, filledPixels, filledPixels)
        pygame.draw.rect(screen, colour, rect)

    for block in piece.blocks:
        colour = alive_colour
        rect = pygame.Rect(block.x * pixelsPerSpace + 1, block.y * pixelsPerSpace + 1, filledPixels, filledPixels)
        pygame.draw.rect(screen, colour, rect)

def main():

    dead_colour = (255, 75, 125)
    alive_colour = (75, 255, 125)

    score: int = 0
    lCleared: int = 0
    level: int = 1
    piece: Piece = Piece()
    piece.blocks = makeBlocks(math.floor(maxX / 2), 0, piece.type, [])
    deads = []
    fallTime = time.time()
    rotateTime = time.time()
    moveTime = time.time()

    screen = pygame.display.set_mode((boardX, boardY)) 
    pygame.display.set_caption("Tetris") 
    pygame.display.flip() 
    running = True
    while running: 
        cycleLinesCleared = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False
            keys=pygame.key.get_pressed()
            if keys[pygame.K_x]:
                if rotateTime < time.time():
                    piece.rotate(deads)
                    rotateTime = time.time() + 0.1
            elif keys[pygame.K_c]:
                if rotateTime < time.time():
                    for i in range(3):
                        piece.rotate(deads)
                    rotateTime = time.time() + 0.1
            elif keys[pygame.K_a]:
                if moveTime < time.time():
                    piece.move(True, deads)
                    moveTime = time.time() + 0.05
            elif keys[pygame.K_d]:
                if moveTime < time.time():
                    piece.move(False, deads)
                    moveTime = time.time() + 0.05
            elif keys[pygame.K_s]:
                fallTime = min(time.time() + 0.07, fallTime)
        if fallTime < time.time():
            piece.fall(deads)
            fallTime = time.time() + (1 / min(level + 3, 13))
        if piece.dead:
            score += 10
            deads += piece.blocks
            for liveBlock in piece.blocks:

                if any([block.x == liveBlock.x and block.y == liveBlock.y and block.y < 2 for block in deads]):
                    pygame.quit()
                    print(f"You got to {score} points!")
                    return
            piece = Piece()
            piece.blocks = makeBlocks(math.floor(maxX / 2), 0, piece.type, [])
        
        for y in range(maxY):
            checkBlocks = []
            for block in deads:
                if block.y == y:
                    checkBlocks.append(block)
            if len(checkBlocks) == maxX:
                cycleLinesCleared += 1
                for block in checkBlocks:
                    while block in deads: deads.remove(block)
                for block in deads:
                    if block.y < y:
                        block.y += 1
        if cycleLinesCleared == 1:
            score += 40 * level
        elif cycleLinesCleared == 2:
            score += 160 * level
        elif cycleLinesCleared == 3:
            score += 400 * level
        elif cycleLinesCleared >= 4:
            score += 1600 * level

        lCleared += cycleLinesCleared
        if level * 10 <= lCleared:
            level += 1
            dead_colour = ((dead_colour[0] + random.randint(20, 30)) % 255, (dead_colour[1] + random.randint(20, 30)) % 255, (dead_colour[2] + random.randint(20, 30)) % 255)

            alive_colour = ((alive_colour[0] + random.randint(20, 30)) % 255, (alive_colour[1] + random.randint(20, 30)) % 255, (alive_colour[2] + random.randint(20, 30)) % 255)

        screen.fill((0, 0, 0))
        draw(screen, deads, piece, [dead_colour, alive_colour])
        pygame.display.flip()
main()