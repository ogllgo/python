import tetris_main as main
import numpy

def order(blocks: list[main.Block]):
    for i in range(len(blocks)):
        for j in range(i, len(blocks)):
            if blocks[j].x < blocks[i].x:
                [blocks[j], blocks[i]] = [blocks[i], blocks[j]]
    
    for i in range(len(blocks)):
        for j in range(i, len(blocks)):
            if blocks[j].y < blocks[i].y:
                [blocks[j], blocks[i]] = [blocks[i], blocks[j]]
    return blocks

def rotatePiece(piece: main.Piece, clockwise: bool = True):
    max = 4
    if clockwise: max = 1
    for z in range(max):
        minx, miny, maxx, maxy = min(i.x for i in piece.blocks),  min(i.y for i in piece.blocks),  max(i.x for i in piece.blocks),  max(i.y for i in piece.blocks)
        [main.Block(maxx - (block.y-miny), maxy - (block.x - minx), block.dead) for block in piece.blocks]
        piece.rotation = (piece.rotation + 1) % 4
    return piece