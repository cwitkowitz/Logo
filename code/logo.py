"""
Frank Cwitkowitz

Created: Unknown - Sometime during late 2018
Revised: 12/22/2018

Functions to draw my logo with letters.
"""

from letters import *
from utils import *

from turtle import *
from math import *

import graphic3

PEN_COLOR = '#000000'
BG_COLOR  = '#F0F0F0'
WIN_SIZE  = 275
SAVE_IMG  = 1
FILL_SHPS = 1

SCALE     = 100

"""
Outer function that will handle each piece of the project altogether.
"""
def main():
    graphicInit(PEN_COLOR, BG_COLOR, WIN_SIZE)
    drawFigure(SCALE)
    graphicFin('logo', SAVE_IMG)

def drawFigure(scale):
    vertical   = scale
    horizontal = 2 * vertical / 5
    margin     = 7 * vertical / 50
    dot_radius = vertical / 25

    back(2 * horizontal + margin)
    left(90)
    fd(margin)
    right(90)
    draw_F(vertical, horizontal, margin, dot_radius, 4)
    draw_r(vertical, horizontal, margin, dot_radius, 4)
    fd(horizontal)
    left(90)
    back(margin / 2)
    right(90)
    graphic3.drawFigure(vertical + margin)
    fd(margin / 2)
    right(90)
    back(3 * horizontal + 2 * margin)
    left(90)
    back(vertical + margin)
    right(90)
    draw_C(vertical, horizontal, margin, dot_radius, 4)
    draw_w(vertical, horizontal, margin, dot_radius, 4)

if __name__ == '__main__':
    main()
