import typing as ty
import pygame as pg
import time
import math

def makeScreen(coordinates: tuple[int, int], name: str):
    screen = pg.display.set_mode(coordinates) 
    pg.display.set_caption(name) 
    pg.display.flip() 
    return screen
dims = (1000, 500)
board = makeScreen(dims, "test")
background = (50, 50, 50)
board.fill(background)


letters: ty.Dict[
    str, ty.List[ty.List[str]]
] = {
    "A": [[" "," "," "," "," "," "," "," "],[" "," "," ","#","#"," "," "," "],[" "," ","#"," "," ","#"," "," "],[" ","#"," "," "," "," ","#"," "],["#","#","#","#","#","#","#","#"],["#"," "," "," "," "," "," ","#"],["#"," "," "," "," "," "," ","#"],["#"," "," "," "," "," "," ","#"]],
    "B": [[" "," "," "," "," "," "," "," "],["#","#","#","#","#","#","#"," "],["#"," "," "," "," "," "," ","#"],["#"," "," "," "," "," "," ","#"],["#","#","#","#","#","#","#","#"],["#"," "," "," "," "," "," ","#"],["#"," "," "," "," "," "," ","#"],["#","#","#","#","#","#","#"," "]],
    "C": [[" "," "," "," "," "," "," "," "],[" ","#","#","#","#","#","#","#"],[" ","#"," "," "," "," "," "," "],["#"," "," "," "," "," "," "," "],["#"," "," "," "," "," "," "," "],["#"," "," "," "," "," "," "," "],[" ","#"," "," "," "," "," "," "],[" ","#","#","#","#","#","#","#"]],
    "D": [[" "," "," "," "," "," "," "," "],["#","#","#","#","#","#","#"," "],["#"," "," "," "," "," "," ","#"],["#"," "," "," "," "," "," ","#"],["#"," "," "," "," "," "," ","#"],["#"," "," "," "," "," "," ","#"],["#"," "," "," "," "," "," ","#"],["#","#","#","#","#","#","#"," "]],
    "E": [[" "," "," "," "," "," "," "," "],["#","#","#","#","#","#","#","#"],["#"," "," "," "," "," "," "," "],["#"," "," "," "," "," "," "," "],["#","#","#","#","#","#","#","#"],["#"," "," "," "," "," "," "," "],["#"," "," "," "," "," "," "," "],["#","#","#","#","#","#","#","#"]],
    "F": [[" "," "," "," "," "," "," "," "],[" ","#","#","#","#","#","#"," "],[" ","#"," "," "," "," "," "," "],[" ","#"," "," "," "," "," "," "],[" ","#","#","#","#","#","#"," "],[" ","#"," "," "," "," "," "," "],[" ","#"," "," "," "," "," "," "],[" ","#"," "," "," "," "," "," "]],
    "G": [[" "," "," "," "," "," "," "," "],["#","#","#","#","#","#","#","#"],["#"," "," "," "," "," "," "," "],["#"," "," "," "," "," "," "," "],["#"," "," "," ","#","#","#","#"],["#"," "," "," "," "," "," ","#"],["#"," "," "," "," "," "," ","#"],["#","#","#","#","#","#","#","#"]],
    "H": [[" "," "," "," "," "," "," "," "],["#"," "," "," "," "," "," ","#"],["#"," "," "," "," "," "," ","#"],["#"," "," "," "," "," "," ","#"],["#","#","#","#","#","#","#","#"],["#"," "," "," "," "," "," ","#"],["#"," "," "," "," "," "," ","#"],["#"," "," "," "," "," "," ","#"]],
    "I": [[" "," "," "," "," "," "," "," "],[" ","#","#","#","#","#","#","#"],[" "," "," "," ","#"," "," "," "],[" "," "," "," ","#"," "," "," "],[" "," "," "," ","#"," "," "," "],[" "," "," "," ","#"," "," "," "],[" "," "," "," ","#"," "," "," "],[" ","#","#","#","#","#","#","#"]],
    "J": [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," ","#"," "],[" "," "," "," "," "," ","#"," "],[" "," "," "," "," "," ","#"," "],[" "," "," "," "," "," ","#"," "],[" "," "," "," "," "," ","#"," "],[" "," "," "," "," ","#"," "," "],["#","#","#","#","#"," "," "," "]],
    "K": [[" "," "," "," "," "," "," "," "],[" ","#"," "," ","#","#"," "," "],[" ","#"," ","#","#"," "," "," "],[" ","#","#","#"," "," "," "," "],[" ","#","#","#"," "," "," "," "],[" ","#"," ","#","#"," "," "," "],[" ","#"," "," ","#","#"," "," "],[" ","#"," "," "," ","#","#"," "]],
    "L": [[" "," "," "," "," "," "," "," "],[" ","#"," "," "," "," "," "," "],[" ","#"," "," "," "," "," "," "],[" ","#"," "," "," "," "," "," "],[" ","#"," "," "," "," "," "," "],[" ","#"," "," "," "," "," "," "],[" ","#"," "," "," "," "," "," "],[" ","#","#","#","#","#","#"," "]],
    "M": [[" "," "," "," "," "," "," "," "],[" ","#"," "," "," "," ","#"," "],[" ","#","#"," "," ","#","#"," "],[" ","#"," ","#","#"," ","#"," "],[" ","#"," "," "," "," ","#"," "],[" ","#"," "," "," "," ","#"," "],[" ","#"," "," "," "," ","#"," "],[" ","#"," "," "," "," ","#"," "]],
    "N": [[" "," "," "," "," "," "," "," "],[" ","#"," "," "," "," ","#"," "],[" ","#","#"," "," "," ","#"," "],[" ","#"," ","#"," "," ","#"," "],[" ","#"," ","#"," "," ","#"," "],[" ","#"," "," ","#"," ","#"," "],[" ","#"," "," ","#"," ","#"," "],[" ","#"," "," "," ","#","#"," "]],
    "O": [[" "," "," "," "," "," "," "," "],[" ","#","#","#","#","#","#"," "],[" ","#"," "," "," "," ","#"," "],[" ","#"," "," "," "," ","#"," "],[" ","#"," "," "," "," ","#"," "],[" ","#"," "," "," "," ","#"," "],[" ","#"," "," "," "," ","#"," "],[" ","#","#","#","#","#","#"," "]],
    "P": [[" "," "," "," "," "," "," "," "],[" ","#","#","#","#","#","#"," "],[" ","#"," "," "," "," ","#"," "],[" ","#"," "," "," "," ","#"," "],[" ","#","#","#","#","#","#"," "],[" ","#"," "," "," "," "," "," "],[" ","#"," "," "," "," "," "," "],[" ","#"," "," "," "," "," "," "]],
    "Q": [[" "," "," "," "," "," "," "," "],[" "," ","#","#","#","#"," "," "],[" ","#"," "," "," "," ","#"," "],[" ","#"," "," "," "," ","#"," "],[" ","#"," "," "," "," ","#"," "],[" ","#"," "," "," "," ","#"," "],[" "," ","#","#","#","#","#"," "],[" "," "," "," "," "," "," ","#"]],
    "R": [[" "," "," "," "," "," "," "," "],[" ","#","#","#","#","#"," "," "],[" ","#"," "," "," "," ","#"," "],[" ","#","#","#","#","#","#"," "],[" ","#"," "," ","#"," "," "," "],[" ","#"," "," "," ","#"," "," "],[" ","#"," "," "," ","#"," "," "],[" ","#"," "," "," "," ","#"," "]],
    "S": [[" "," "," "," "," "," "," "," "],[" "," ","#","#","#","#","#"," "],[" ","#"," "," "," "," "," "," "],[" ","#"," "," "," "," "," "," "],[" "," ","#","#","#","#"," "," "],[" "," "," "," "," "," ","#"," "],[" "," "," "," "," "," ","#"," "],[" ","#","#","#","#","#"," "," "]],
    "T": [[" "," "," "," "," "," "," "," "],[" ","#","#","#","#","#","#"," "],[" "," "," "," ","#"," "," "," "],[" "," "," "," ","#"," "," "," "],[" "," "," "," ","#"," "," "," "],[" "," "," "," ","#"," "," "," "],[" "," "," "," ","#"," "," "," "],[" "," "," "," ","#"," "," "," "]],
    "U": [[" "," "," "," "," "," "," "," "],[" ","#"," "," "," "," ","#"," "],[" ","#"," "," "," "," ","#"," "],[" ","#"," "," "," "," ","#"," "],[" ","#"," "," "," "," ","#"," "],[" ","#"," "," "," "," ","#"," "],[" ","#"," "," "," "," ","#"," "],[" "," ","#","#","#","#"," "," "]],
    "V": [[" "," "," "," "," "," "," "," "],[" ","#"," "," "," "," ","#"," "],[" ","#"," "," "," "," ","#"," "],[" ","#"," "," "," "," ","#"," "],[" "," ","#"," "," ","#"," "," "],[" "," ","#"," "," ","#"," "," "],[" "," "," ","#","#"," "," "," "],[" "," "," ","#","#"," "," "," "]],
    "W": [[" "," "," "," "," "," "," "," "],[" ","#"," "," "," "," ","#"," "],[" ","#"," "," "," "," ","#"," "],[" ","#"," "," "," "," ","#"," "],[" ","#"," "," "," "," ","#"," "],[" ","#"," ","#","#"," ","#"," "],[" ","#","#"," "," ","#","#"," "],[" ","#"," "," "," "," ","#"," "]],
    "X": [[" "," "," "," "," "," "," "," "],[" ","#"," "," "," "," ","#"," "],[" "," ","#"," "," ","#"," "," "],[" "," "," ","#","#"," "," "," "],[" "," "," ","#","#"," "," "," "],[" "," "," ","#","#"," "," "," "],[" "," ","#"," "," ","#"," "," "],[" ","#"," "," "," "," ","#"," "]],
    "Y": [[" "," "," "," "," "," "," "," "],[" ","#"," "," "," "," ","#"," "],[" "," ","#"," "," ","#"," "," "],[" "," "," ","#","#"," "," "," "],[" "," "," ","#"," "," "," "," "],[" "," "," ","#"," "," "," "," "],[" "," "," ","#"," "," "," "," "],[" "," "," ","#"," "," "," "," "]],
    "Z": [[" "," "," "," "," "," "," "," "],[" ","#","#","#","#","#","#"," "],[" "," "," "," "," ","#"," "," "],[" "," "," "," ","#"," "," "," "],[" "," "," "," ","#"," "," "," "],[" "," "," ","#"," "," "," "," "],[" "," ","#"," "," "," "," "," "],[" ","#","#","#","#","#","#"," "]],

    "a": [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," ","#","#","#"," "," "],[" "," "," "," "," ","#"," "],[" "," ","#","#","#","#"," "],[" ","#"," ","#","#","#"," "],[" ","#","#","#"," ","#"," "]],
    "b": [[" ","#"," "," "," "," "," "," "],[" ","#"," "," "," "," "," "," "],[" ","#"," "," "," "," "," "," "],[" ","#","#","#","#","#"," "," "],[" ","#"," "," "," "," ","#"," "],[" ","#"," "," "," "," ","#"," "],[" ","#"," "," "," "," ","#"," "],[" ","#","#","#","#","#","#"," "]],
    "c": [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," ","#","#","#","#","#"," "],[" ","#"," "," "," "," "," "," "],[" ","#"," "," "," "," "," "," "],[" ","#"," "," "," "," "," "," "],[" "," ","#","#","#","#","#"," "]],
    "d": [[" "," "," "," "," "," ","#"," "],[" "," "," "," "," "," ","#"," "],[" "," "," "," "," "," ","#"," "],[" "," ","#","#","#","#","#"," "],[" ","#"," "," "," "," ","#"," "],[" ","#"," "," "," "," ","#"," "],[" ","#"," "," "," "," ","#"," "],[" "," ","#","#","#","#","#"," "]],
    "e": [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," ","#","#","#","#"," "," "],[" ","#"," "," "," "," ","#"," "],[" ","#","#","#","#","#","#"," "],[" ","#"," "," "," "," "," "," "],[" "," ","#","#","#","#","#"," "]],
    "f": [[" "," "," "," ","#","#","#"," "],[" "," "," ","#"," "," "," "," "],[" "," "," ","#"," "," "," "," "],[" ","#","#","#","#","#","#"," "],[" "," "," ","#"," "," "," "," "],[" "," "," ","#"," "," "," "," "],[" "," "," ","#"," "," "," "," "],[" "," "," ","#"," "," "," "," "]],
    "g": [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," ","#","#","#","#","#"," "],[" ","#"," "," "," "," ","#"," "],[" "," ","#","#","#","#","#"," "],[" "," "," "," "," "," ","#"," "],[" "," ","#"," "," "," ","#"," "],[" "," "," ","#","#","#","#"," "]],
    "h": [[" ","#"," "," "," "," "],[" ","#"," "," "," "," "],[" ","#"," "," "," "," "],[" ","#","#","#"," "," "],[" ","#"," "," ","#"," "],[" ","#"," "," ","#"," "],[" ","#"," "," ","#"," "],[" ","#"," "," ","#"," "]],
    "i": [[" "," "," "," "],[" ","#"," "," "],[" "," "," "," "],[" ","#"," "," "],[" ","#"," "," "],[" ","#"," "," "],[" ","#"," "," "],[" ","#","#"," "]],
    "j": [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," ","#"," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," ","#","#"," "],[" "," "," "," "," "," ","#"," "],[" "," "," "," "," "," ","#"," "],[" ","#"," "," "," "," ","#"," "],[" "," ","#","#","#","#"," "," "]],
    "k": [[" ","#"," "," "," "," "," "," "],[" ","#"," "," "," "," "," "," "],[" ","#"," ","#","#"," "," "," "],[" ","#","#"," "," ","#"," "," "],[" ","#","#","#","#"," "," "," "],[" ","#"," "," ","#"," "," "," "],[" ","#"," "," "," ","#"," "," "],[" ","#"," "," "," "," ","#"," "]],
    "l": [[" "," "," "," "," "," "," "," "],[" "," ","#","#"," "," "," "," "],[" "," "," ","#"," "," "," "," "],[" "," "," ","#"," "," "," "," "],[" "," "," ","#"," "," "," "," "],[" "," "," ","#"," "," "," "," "],[" "," "," ","#"," "," "," "," "],[" ","#","#","#","#","#","#"," "]],
    "m": [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" ","#"," "," "," ","#"," "],[" ","#","#"," ","#","#"," "],[" ","#"," ","#"," ","#"," "],[" ","#"," ","#"," ","#"," "]],
    "n": [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" ","#"," ","#","#","#"," "," "],[" ","#","#"," "," "," ","#"," "],[" ","#"," "," "," "," ","#"," "],[" ","#"," "," "," "," ","#"," "],[" ","#"," "," "," "," ","#"," "]],
    "o": [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," ","#","#","#","#"," "," "],[" ","#"," "," "," "," ","#"," "],[" ","#"," "," "," "," ","#"," "],[" ","#"," "," "," "," ","#"," "],[" "," ","#","#","#","#"," "," "]],
    "p": [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" ","#","#","#","#","#"," "," "],[" ","#"," "," "," "," ","#"," "],[" ","#"," "," "," "," ","#"," "],[" ","#","#","#","#","#","#"," "],[" ","#"," "," "," "," "," "," "],[" ","#"," "," "," "," "," "," "]],
    "q": [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," ","#","#","#","#","#"," "],[" ","#"," "," "," "," ","#"," "],[" ","#"," "," "," "," ","#"," "],[" ","#","#","#","#","#","#"," "],[" "," "," "," "," "," ","#"," "],[" "," "," "," "," "," ","#"," "]],
    "r": [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" ","#"," ","#","#","#"," "," "],[" ","#","#"," "," "," ","#"," "],[" ","#"," "," "," "," "," "," "],[" ","#"," "," "," "," "," "," "],[" ","#"," "," "," "," "," "," "]],
    "s": [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," ","#","#","#","#"," "],[" ","#"," "," "," "," "," "],[" "," ","#","#","#"," "," "],[" "," "," "," "," ","#"," "],[" ","#","#","#","#"," "," "]],
    "t": [[" "," "," "," "," "," "],[" "," ","#"," "," "," "],[" ","#","#","#","#"," "],[" "," ","#"," "," "," "],[" "," ","#"," "," "," "],[" "," ","#"," "," "," "],[" "," ","#"," "," "," "],[" "," "," ","#","#"," "]],
    "u": [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" ","#"," "," "," ","#"," "],[" ","#"," "," "," ","#"," "],[" ","#"," "," "," ","#"," "],[" ","#"," "," "," ","#"," "],[" "," ","#","#","#"," "," "]],
    "v": [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" ","#"," "," "," ","#"," "],[" ","#"," "," "," ","#"," "],[" "," ","#"," ","#"," "," "],[" "," ","#"," ","#"," "," "],[" "," "," ","#"," "," "," "]],
    "w": [[" "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "],[" ","#"," "," "," "," "," ","#"," "],[" ","#"," "," "," "," "," ","#"," "],[" "," ","#"," ","#"," ","#"," "," "],[" "," ","#"," ","#"," ","#"," "," "],[" "," "," ","#"," ","#"," "," "," "]],
    "x": [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" ","#"," "," "," ","#"," "],[" "," ","#"," ","#"," "," "],[" "," "," ","#"," "," "," "],[" "," ","#"," ","#"," "," "],[" ","#"," "," "," ","#"," "]],
    "y": [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" ","#"," "," "," ","#"," "],[" ","#"," "," "," ","#"," "],[" "," ","#"," ","#"," "," "],[" "," "," ","#","#"," "," "],[" "," "," ","#"," "," "," "],[" "," ","#"," "," "," "," "],[" ","#"," "," "," "," "," "]],
    "z": [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" ","#","#","#","#","#"," "],[" "," "," "," ","#"," "," "],[" "," "," ","#"," "," "," "],[" "," ","#"," "," "," "," "],[" ","#","#","#","#","#"," "]],


    " ": [[" "," "," "],[" "," "," "],[" "," "," "],[" "," "," "],[" "," "," "],[" "," "," "],[" "," "," "],[" "," "," "]],
    "!": [[" ","#"," "],[" ","#"," "],[" ","#"," "],[" ","#"," "],[" ","#"," "],[" ","#"," "],[" "," "," "],[" ","#"," "]],
    ",": [[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," ","#"," "],[" ","#"," "," "]],
    ".": [[" "," "," "],[" "," "," "],[" "," "," "],[" "," "," "],[" "," "," "],[" "," "," "],[" ","#"," "],[" "," "," "]],
    ":": [[" "," "," "],[" "," "," "],[" ","#"," "],[" ","#"," "],[" "," "," "],[" "," "," "],[" ","#"," "],[" ","#"," "]]
}


def makeLetter(color: ty.Tuple[int, int, int], letter: str) -> ty.List[ty.List[ty.Tuple[int, int, int, str]]]:
    newData: ty.List[ty.List[ty.Tuple[int, int, int, str]]] = []
    if not letter in letters:
        return [[(0,0,0,"#")]]
    letterData = letters[letter]
    for x in range(len(letterData)):
        newData.append([])
        for y in range(len(letterData[x])):
            newData[x].append((*color, letterData[x][y]))
    return newData

def draw_sprite(surface: pg.Surface, position: ty.Tuple[float, float], spriteData: ty.List[ty.List[ty.Tuple[int, int, int, str]]], scalingFactor: float = 1, ignoreChar: str = " "):
    for x in range(len(spriteData)):
        for y in range(len(spriteData[x])):
            if spriteData[x][y][3] == ignoreChar: continue
            currPosition: ty.Tuple[float, float] = (position[1] + y * scalingFactor, position[0] + x * scalingFactor)
            colour: ty.Tuple[int, int, int] = (spriteData[x][y][0], spriteData[x][y][1], spriteData[x][y][2])
            rect = pg.Rect(currPosition[0], currPosition[1], scalingFactor, scalingFactor)
            pg.draw.rect(surface, colour, rect)



def countPixels(word: str) -> int:
    totalLength = sum([max([len(pixelLetter) for pixelLetter in makeLetter((0,0,0), letter)]) for letter in word])
    return totalLength
def printPhrase(board: pg.Surface, phrase: str, position: ty.Tuple[float, float], scalingFactor: float = 1):
    y_pos, x_pos = position
    words = phrase.split()
    lines = [""]
    for word in words:
        lineLength: float = countPixels(lines[-1]) * scalingFactor
        wordLength: float = countPixels(word) * scalingFactor
        if lineLength + wordLength > dims[0]:
            lines.append("")
            lineLength: float = countPixels(lines[-1]) * scalingFactor
            print("adding a line")
        print(f"Current line: '{lines[-1]}', length: {lineLength}")
        print(f"Word: '{word}', length: {wordLength}")
        print(f"Total length: {lineLength + wordLength}")
        lines[-1] += word + " "
    print(len(lines))
    for line in lines:
        drawLine(board, line, (y_pos, x_pos), [(200, 200, 255)], scalingFactor)
        y_pos += 9 * scalingFactor
def drawLine(board: pg.Surface, phrase: str, offsets: ty.Tuple[float, float], colours: ty.List[ty.Tuple[int, int, int]], scalingFactor: float = 1) -> None:
    newLetters: ty.List[ty.List[ty.List[ty.Tuple[int, int, int, str]]]] = []
    for index in range(len(phrase)):
        letter = phrase[index]
        colour = colours[index % len(colours)]
        newLetters.append(makeLetter(colour, letter))
    before = 0
    for index in range(len(newLetters)):
        letter = newLetters[index]
        offsets = (offsets[0], before + max([len(line) for line in newLetters[index - 1]]) * scalingFactor*1.2)
        draw_sprite(board, offsets, letter, scalingFactor)
        before = offsets[1]

printPhrase(board, "this is a very long phrase that should be split up by the end of the screen", (0,0), scalingFactor=3)
pg.display.flip()
Running = True
down: ty.Tuple[bool, bool, bool] = (False, False, False)
mouse: ty.Tuple[int, int] = pg.mouse.get_pos()
previous_mouse = mouse
while Running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            Running = False
        if event.type == pg.MOUSEMOTION:
            mouse = pg.mouse.get_pos()
        if event.type == pg.MOUSEBUTTONDOWN:
            if pg.mouse.get_pressed(3)[0]:
                down = (True, down[1], down[2])
        elif event.type == pg.MOUSEBUTTONUP:
            down = (False, False, False)
    
    if down[0]:
        pg.draw.line(board, (255, 255, 255), mouse, previous_mouse)
        board.fill((255, 255, 255), pg.rect.Rect(mouse[0], mouse[1], 1, 1))
    previous_mouse = mouse
    time.sleep(0.2)
    pg.display.flip()
pg.quit()