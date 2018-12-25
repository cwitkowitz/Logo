"""
Frank Cwitkowitz

Created: 10/23/16
Revised: 12/22/2018

The fourth graphic.
"""

from utils import *

from turtle import *
from math import *

PEN_COLOR = '#FFFFFF'
BG_COLOR  = '#C1C0CC'
WIN_SIZE  = 500
SAVE_IMG  = 1

RADIUS    = 100
SCALE = 0.15
SEC_COLOR = 'purple'
CIRC_COLS = ['black', 'purple', 'black', BG_COLOR]

"""
Outer function that will handle each piece of the project altogether.
"""
def main():
    graphicInit(PEN_COLOR, BG_COLOR, WIN_SIZE)
    drawFigure(RADIUS, SCALE)
    graphicFin('graphic4', SAVE_IMG)

def drawFigure(radius, scale):
    radius = 100
    left(120)
    drawCenterPiece(radius)
    right(80)
    drawAppendage(radius, scale)
    right(180)
    drawAppendage(radius, scale)
    right(100)

"""
Function to draw the middle circle and
any fills.
"""
def drawCenterPiece(radius):
    # Big outer circle
    right(90)
    fd(radius)
    left(90)
    drawLayeredCircle(radius, 360, [2, 3, 2], CIRC_COLS)
    right(90)
    back(radius)
    left(90)

    # Small inner circle
    right(90)
    fd(.35 * radius)
    left(90)
    drawLayeredCircle((.35 * radius), 360, [2, 3, 2], CIRC_COLS)
    right(90)
    back(.35 * radius)
    left(90)

    # Draw the semi-circle lines at four different lengths
    drawOuterFill(radius, .82)
    drawCenterFill(radius, .67)
    drawInnerFill(radius, .48)
    drawInnerCircleFill(radius, .2)

"""
Function to draw the tracings of the
outermost fill.
"""
def drawOuterFill(radius, scale):
    right(30)
    fd(scale * radius)
    left(90)
    drawThickenedCircle((scale * radius), 87, 2)
    right(90)
    back(scale * radius)
    left(30)

    left(165)
    fd(scale * radius)
    left(90)
    drawThickenedCircle((scale * radius), 30, 2)
    right(90)
    back(scale * radius)
    right(165)

    left(105)
    fd(scale * radius)
    left(90)
    drawThickenedCircle((scale * radius), 20, 2)
    right(90)
    back(scale * radius)
    right(105)

"""
Function to draw the tracings of the
center fill.
"""
def drawCenterFill(radius, scale):
    right(117)
    fd(scale * radius)
    left(90)
    drawThickenedCircle((scale * radius), 30, 2)
    right(90)
    back(scale * radius)
    left(117)

    right(73)
    fd(scale * radius)
    left(90)
    drawThickenedCircle((scale * radius), 30, 2)
    right(90)
    back(scale * radius)
    left(73)

    left(62)
    fd(scale * radius)
    left(90)
    drawThickenedCircle((scale * radius), 28, 2)
    right(90)
    back(scale * radius)
    right(62)

"""
Function to draw the tracings of the
innermost fill.
"""
def drawInnerFill(radius, scale):
    right(210)
    fd(scale * radius)
    left(90)
    drawThickenedCircle((scale * radius), 87, 2)
    right(90)
    back(scale * radius)
    left(210)

    right(30)
    fd(scale * radius)
    left(90)
    drawThickenedCircle((scale * radius), 60, 2)
    right(90)
    back(scale * radius)
    left(30)


"""
Function to draw the tracings of the fill inside
of the smaller concentric circle.
"""
def drawInnerCircleFill(radius, scale):
    right(60)
    fd(scale * radius)
    left(90)
    drawThickenedCircle((scale * radius), 140, 2)
    right(90)
    back(scale * radius)
    left(60)

    left(140)
    fd(scale * radius)
    left(90)
    drawThickenedCircle((scale * radius), 100, 2)
    right(90)
    back(scale * radius)
    right(140)

"""
Function to draw a triangular appendage.
"""
def drawAppendage(scale, radius):
    # Straight line and mini circle
    drawLayeredLine((2.3 * scale), [1, 2, 1], CIRC_COLS)
    fd(radius * scale)
    left(90)
    drawLayeredCircle((radius * scale), 360, [1, 2, 1], CIRC_COLS)
    right(90)
    back(radius * scale)

    drawFills(scale)

    # Side slants
    back(2.3 * scale)
    left(90)
    fd(.65 * scale)
    right(90)
    right(90 - degrees(atan((2.3 * scale) / (.65 * scale))))
    drawLayeredLine(((.65 * scale) / cos(radians(degrees(atan((2.3 * scale) / (.65 * scale)))))), [1, 2, 1], CIRC_COLS)
    back((.65 * scale) / cos(radians(degrees(atan((2.3 * scale) / (.65 * scale))))))
    left(90 - degrees(atan((2.3 * scale) / (.65 * scale))))
    left(90)
    back(2 * (.65 * scale))
    right(degrees(atan((2.3 * scale) / (.65 * scale))))
    drawLayeredLine(((.65 * scale) / cos(radians(degrees(atan((2.3 * scale) / (.65 * scale)))))), [1, 2, 1], CIRC_COLS)
    back((.65 * scale) / cos(radians(degrees(atan((2.3 * scale) / (.65 * scale))))))
    left(degrees(atan((2.3 * scale) / (.65 * scale))))
    fd(.65 * scale)
    right(90)

"""
Draws the fills inside of the appendages.
"""
def drawFills(scale):
    right(180)

    # Right
    fd(.6 * scale)
    right(90)
    fd(.07 * scale)
    left(90)
    drawThickenedLine((.6 * scale), 2)
    right(86)
    drawThickenedCircle(1.1 * scale, 12, 2)
    left(86)
    back(.6 * scale)
    right(90 - degrees(atan((2.3 * scale) / (.65 * scale))))
    right(90)
    fd(.02 * scale)
    left(90)
    fd(.2 * scale)
    drawThickenedLine(.4 * scale, 2)
    back(.6 * scale)
    left(90)
    fd(.02 * scale)
    right(90)
    left(90 - degrees(atan((2.3 * scale) / (.65 * scale))))
    right(90)
    back(.07 * scale)
    left(90)
    back(.6 * scale)

    # Left
    fd(.6 * scale)
    left(90)
    fd(.07 * scale)
    right(90)
    drawThickenedLine((.6 * scale), 2)
    left(78)
    drawThickenedCircle(1.1 * scale, 11.7, 2)
    right(78)
    back(.6 * scale)
    left(90 - degrees(atan((2.3 * scale) / (.65 * scale))))
    left(90)
    fd(.02 * scale)
    right(90)
    fd(.2 * scale)
    drawThickenedLine(.37 * scale, 2)
    back(.57 * scale)
    right(90)
    fd(.02 * scale)
    left(90)
    right(90 - degrees(atan((2.3 * scale) / (.65 * scale))))
    left(90)
    back(.07 * scale)
    right(90)
    back(.6 * scale)

    right(180)

"""
Draws two loops around the center figure.
"""
def drawLoopsPlural(radius, scale):
    right(90)
    fd(2.3 * radius)
    left(90)
    fd(scale * radius)
    drawLoop(radius, scale)
    back(scale * radius)
    right(90)
    back(2 * 2.3 * radius)
    right(90)
    fd(scale * radius)
    drawLoop(radius, scale)
    back(scale * radius)
    left(90)
    back(2.3 * radius)
    left(180)

"""
Draws one loop around the center figure.
"""
def drawLoop(radius, scale):
    left(30)
    drawLayeredCircle((1.16 * 2.3 * radius), 120, [1, 2, 1], CIRC_COLS)
    right(30)

if __name__ == '__main__':
    main()
