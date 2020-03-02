# sneak game

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class Cube(object):
    rows = 0
    w = 0
    def __init__(self, start, dinrx=1, dinry=0, color=(255, 0, 0)):
        pass

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass


class Snake(object):
    def __init__(self, color, pos):
        pass

    def move(self):
        pass

    def reset(self, pos):
        pass

    def add_cube(self):
        pass

    def draw(self,surface):
        pass


def drawGrid(w, rows, surface):
    pass

def redrawWindow(surface):
    pass

def randomSnack(rows, items):
    pass

def msg_box(subject, content):
    pass

def main():
    width = 500
    height = 500
    rows = 20
    win = pygame.display.set_mode((width, height))
    s = Snake((255, 5, 0), (10, 10))

    flag = True
    while flag:
        pygame.time.delay(50)

main()