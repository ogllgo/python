from drawingUtils import *
import pygame as pg
import typing as ty
import math
import time

def getTime():
    return math.floor(time.time_ns() / 1000000)

dims = (1500, 1000)
pg.init()
board = makeScreen(dims, "Text drawing space")
background = (50, 50, 50)
board.fill(background)

phrase = ""
previous_phrase = phrase
pg.display.flip()
Running = True
down: ty.Tuple[bool, bool, bool] = (False, False, False)
mouse: ty.Tuple[int, int] = pg.mouse.get_pos()
capital = False
previous_mouse = mouse
held_key = None
keyRepeatEvent = pg.USEREVENT + 1
repeatAmount = 0
lastCharPress: int = getTime()

specialKeyCases = ["escape", "delete", "caps lock", "left ctrl"]
inverseCaps: bool = False

globalScaling: float = 2
while Running:
    
    for event in pg.event.get():
        if event.type == pg.MOUSEMOTION:
            mouse = pg.mouse.get_pos()

        if event.type == pg.QUIT:
            Running = False

        elif event.type == pg.KEYUP:
            pressed_key = pg.key.name(event.key)
            if pressed_key == "left shift":
                if inverseCaps:
                    capital = True
                else:
                    capital = False
            
            if pressed_key == "escape" or pressed_key == "delete":
                board.fill(background)
                phrase = ""
            
            if event.key == held_key:
                held_key = None
                pg.time.set_timer(keyRepeatEvent, 0)

        elif event.type == pg.KEYDOWN:
            unpressed_key = pg.key.name(event.key)
            if unpressed_key == "caps lock":
                capital = not capital
                inverseCaps = not inverseCaps
            if unpressed_key == "left shift":
                if inverseCaps:
                    capital = False
                else:
                    capital = True
            elif not unpressed_key in specialKeyCases:
                lastCharPress = getTime()
                held_key = event.key
                repeatAmount = 0
                pg.time.set_timer(keyRepeatEvent, 300)
                if pg.key.name(held_key) == "backspace":
                    phrase = phrase[0:-1]
                else:
                    if pg.key.name(held_key) in list("0123456789") and inverseCaps:
                        phrase += get_char(held_key, not capital)
                    else:
                        phrase += get_char(held_key, capital)

        elif event.type == keyRepeatEvent and held_key is not None:
            repeatAmount += 1
            lastCharPress = getTime()
            pg.time.set_timer(keyRepeatEvent, max(math.floor(200 / repeatAmount), 50))
            if pg.key.name(held_key) == "backspace":
                phrase = phrase[0:-1]
            else:
                if held_key in list("0123456789") and inverseCaps:
                    print("special number case")
                    phrase += get_char(held_key, not capital)
                else:
                    phrase += get_char(held_key, capital)
    if math.floor(getTime() / 500) % 2 == 0 or lastCharPress + 200 > getTime():
        board.fill(background)
        printPhrase(board, phrase, (0,0), [[(200, 200, 255)]], dims, scalingFactor=globalScaling)
    else:
        board.fill(background)
        printPhrase(board, phrase + "▉", (0,0), [[(200, 200, 255)]], dims, scalingFactor=globalScaling)
    previous_phrase = phrase
    time.sleep(0.01)
    pg.display.flip()
pg.quit()