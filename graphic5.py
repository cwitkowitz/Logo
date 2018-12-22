"""
Frank Cwitkowitz

Created: Unknown - Sometime during early 2017
Revised: 12/22/2018

The fifth graphic.
"""

from utils import *

from turtle import *
from math import *

PEN_COLOR = '#000000'
BG_COLOR  = '#FFFFFF'
WIN_SIZE  = 300

"""
Outer function that will handle
each piece of the project altogether.
"""
def main(windowXSize):
    graphicInit(PEN_COLOR, BG_COLOR, WIN_SIZE)
    left(90)

    """
    This parameter will change the length of the
    tertiary length if that makes sense
    """
    scale = 20

    for i in range(0, 4):
        squareCorners(scale)
        left(90)
        bars(scale)

    graphicFin()


"""
Function that will draw a normal,
straight line with the provided thickness.
"""
def drawThickenedLine(length, thickness):
    pensize(thickness)
    down()
    forward(length)
    up()
    pensize(1)


"""
Function that will draw a normal,
straight line with the provided thickness.
"""
def drawThickenedCircle(radius, extent, thickness):
    pensize(thickness)
    down()
    circle(radius, extent)
    up()
    pensize(1)

"""
Draws one corner of this dope design
"""
def squareCorners(scale):

    hyp = scale * sqrt(2)

    fd(scale / 2)
    left(90)
    fd(scale / 2)
    right(45)

    down()
    fd(hyp)
    left(135)
    fd(scale)
    right(90)
    fd(scale)
    right(90)
    fd(scale * 2)
    up()
    left(45)
    fd(hyp)
    down()
    left(135)
    fd(scale * 2)
    right(90)
    fd(scale)
    right(90)
    fd(scale * 3)
    left(45)
    back(hyp)
    left(135)
    fd(scale * 2)
    right(45)
    fd(hyp)
    right(45)
    fd(scale)
    left(45)
    back(hyp)
    fd(hyp)
    right(135)
    fd(scale * 5)
    up()
    left(45)
    back(hyp * 4)

    down()
    right(135)
    fd(scale)
    left(90)
    fd(scale)
    left(90)
    fd(scale * 2)
    up()
    right(45)
    fd(hyp)
    down()
    right(135)
    fd(scale * 2)
    left(90)
    fd(scale)
    left(90)
    fd(scale * 3)
    right(45)
    back(hyp)
    right(135)
    fd(scale * 2)
    left(45)
    fd(hyp)
    left(45)
    fd(scale)
    right(45)
    back(hyp)
    fd(hyp)
    left(135)
    fd(scale * 5)
    up()
    right(45)
    back(hyp * 5)
    left(45)

    back(scale / 2)
    right(90)
    back(scale / 2)


"""
bars qqa
"""
def bars(scale):

    hyp = scale * sqrt(2)

    down()
    fd(scale * 10)
    right(135)
    fd(hyp * 4.5)
    back(hyp * 4.5)
    right(90)
    fd(hyp * 4.5)
    back(hyp * 4.5)
    right(135)
    back(scale * 10)

    right(45)

    up()
    fd(hyp / 2)
    down()

    left(45)
    fd(scale * 3)
    right(135)
    fd(hyp)
    left(45)
    fd(scale)
    left(135)
    fd(hyp * 2)
    right(45)
    fd(scale * 4)
    right(135)
    fd(hyp * 3)
    back(hyp * 3)
    left(135)
    back(scale)
    right(135)
    fd(hyp * 2)
    back(hyp * 2)
    left(135)
    back(scale * 3)
    up()
    back(scale)
    down()
    back(scale * 3)
    right(45)

    up()
    back(hyp / 2)
    down()

    left(45)

    left(45)

    up()
    fd(hyp / 2)
    down()

    right(45)
    fd(scale * 3)
    left(135)
    fd(hyp)
    right(45)
    fd(scale)
    right(135)
    fd(hyp * 2)
    left(45)
    fd(scale * 4)
    left(135)
    fd(hyp * 3)
    back(hyp * 3)
    right(135)
    back(scale)
    left(135)
    fd(hyp * 2)
    back(hyp * 2)
    right(135)
    back(scale * 3)
    up()
    back(scale)
    down()
    back(scale * 3)
    left(45)

    up()
    back(hyp / 2)
    down()

    right(45)

    up()


main(600)
