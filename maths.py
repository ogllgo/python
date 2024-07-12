import math as Math



num = 229

square = num**2

nextSquare = int(str(square) + "1")
nextNum = Math.sqrt(nextSquare)

while True:
    num += 1
    square = num**2
    nextSquare = int(str(square) + "1")
    nextNum = Math.sqrt(nextSquare)
    if int(nextNum) == nextNum:
        print(f"{nextNum} / {num} = {nextNum / num}")


        # 3.162277660168379