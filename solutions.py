dinoX = 0
dinoY = 0
dinoWidth = 0
dinoHeight = 0
obstacles = []
def checkIfHit():
    for i in range(len(obstacles)):
        obX, obY, obS = obstacles[i]
        if dinoX + dinoWidth < obX:
            continue
        if obX + obstSize < dinoX:
            continue
        if dinoY + dinoHeight < obY - size:
            continue
        if dinoY > obY:
            continue
        print("hit")

