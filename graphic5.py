"""
Frank Cwitkowitz

Created: Unknown - Sometime during early 2017
Revised: 12/22/2018

The fifth graphic.
"""

from utils import *

from turtle import *
from math import *

PEN_COLOR = '#FFFFFF'
BG_COLOR  = '#C1C0CC'
WIN_SIZE  = 500

SCALE = 20

"""
Outer function that will handle each piece of the project altogether.
"""
def main(scale):
    graphicInit(PEN_COLOR, BG_COLOR, WIN_SIZE)
    drawFigure(scale)
    graphicFin()

def drawFigure(scale):
    # Assuming 45 degree angles, compute the length of the hypotenuse w.r.t. the scale provided
    hyp = scale * sqrt(2)

    # Draw the same repeated design four times
    left(90)
    for i in range(4):
        drawSmallCorner(scale, hyp, 1)
        drawLargeCorner(scale, hyp, 3)
        drawFrame(scale, hyp, 3)
        left(90)

def drawSmallCorner(scale, hyp, tness):
    # Position pen away from center in diagonal direction
    left(45)
    fd(1.5 * hyp)

    # Draw small corner close to center
    drawCorner(scale, hyp, tness, 1, 2, 1)

    # Re-position pen at center of graphic
    back(1.5 * hyp)
    right(45)

def drawLargeCorner(scale, hyp, tness):
    # Position pen away from center in diagonal direction
    left(45)
    fd(3.5 * hyp)

    # Draw the inside of the larger corner
    drawCorner(scale, hyp, tness - 1, 2, 3, 1)

    # Position pen for outside of corner while drawing edge
    drawThickenedLine(hyp, tness - 1)

    # Draw the outside of the larger corner
    drawCorner(scale, hyp, tness, 4, 5, 1)

    # Re-position pen at center of graphic
    back(4.5 * hyp)
    right(45)

def drawFrame(scale, hyp, tness):
    # Draw long line in between corners and across corners
    drawThickenedLine(10 * scale, tness)
    left(135)
    drawThickenedLine(4.5 * hyp, tness)
    fd(hyp)
    drawThickenedLine(4.5 * hyp, tness)
    back(10 * hyp)
    right(135)
    back(10 * scale)

    # Draw inside lines for both center bars in this quadrant
    left(45)
    fd(hyp / 2)
    right(45)
    drawThickenedLine(3 * scale, tness)
    fd(scale)
    drawThickenedLine(4 * scale, tness)
    back(8 * scale)
    left(90)
    drawThickenedLine(3 * scale, tness)
    fd(scale)
    drawThickenedLine(4 * scale, tness)
    back(8 * scale)
    right(45)
    back(hyp / 2)
    right(45)

    # Prepare to draw inner bar
    left(45)
    fd(hyp / 2)

    # Draw inner bar
    right(45)
    fd(3 * scale)
    left(135)
    drawThickenedLine(hyp, tness)
    fd(hyp)
    drawThickenedLine(hyp, tness)
    back(3 * hyp)
    right(135)
    fd(scale)
    left(135)
    drawThickenedLine(4 * hyp, tness)
    back(4 * hyp)
    right(135)
    back(4 * scale)
    left(45)

    # Reset after drawing inner bar
    back(hyp / 2)
    right(45)

    # Prepare to draw outer bar
    left(45)
    fd(hyp / 2)

    # Draw outer bar
    right(45)
    fd(7 * scale)
    left(135)
    drawThickenedLine(2 * hyp, tness)
    fd(3 * hyp)
    drawThickenedLine(2 * hyp, tness)
    back(7 * hyp)
    right(135)
    fd(scale)
    left(135)
    drawThickenedLine(3 * hyp, tness)
    fd(2 * hyp)
    drawThickenedLine(3 * hyp, tness)
    back(8 * hyp)
    right(135)
    back(8 * scale)
    left(45)

    # Reset after drawing outer bar
    back(hyp / 2)
    right(45)

if __name__ == '__main__':
    main(SCALE)
