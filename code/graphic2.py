"""
Frank Cwitkowitz

Created: 12/16/2015
Revised: 12/22/2018

The trace for the manual drawing of the second graphic.
"""

from utils import *

from turtle import *

PEN_COLOR = '#CCCCCC'
BG_COLOR  = '#FFFFFF'
WIN_SIZE  = 500

RING_SIZE = 25
WING_LEN  = 200
WING_ANG  = 25
WING_NUM  = 5 # Should be a odd integer

"""
Outer function that will handle each piece of the project altogether
"""
def main():
    graphicInit(PEN_COLOR, BG_COLOR, WIN_SIZE)
    drawFigure()
    graphicFin('graphic2')

def drawFigure():
    drawRing(RING_SIZE, 1)

    numSideTraces = WING_NUM // 2

    # Draw a full trace (top and bottom wings) which is not angled
    drawFullTrace(WING_LEN, RING_SIZE, 1)

    for x in range(numSideTraces):
        left(WING_ANG)
        drawFullTrace(WING_LEN, RING_SIZE, 1)
    right(numSideTraces * WING_ANG)

    # Draw the full traces which are rotated to the left
    for x in range(numSideTraces):
        right(WING_ANG)
        drawFullTrace(WING_LEN, RING_SIZE, 1)
    left(numSideTraces * WING_ANG)

def drawRing(radius, tness):
    # Draw the ring around the center of the trace
    drawThickenedCircle(radius, 360, tness)
    left(90)
    fd((3 * radius) / 8)
    right(90)
    drawThickenedCircle((5 * radius) / 8, 360, tness)
    left(90)
    fd((5 * radius) / 8)

def drawFullTrace(length, radius, tness):
    # Draw both the top and bottom wing of a full trace
    drawHalfTrace(length, radius, tness)
    right(180)
    drawHalfTrace(length, radius, tness)
    right(180)

def drawHalfTrace(length, radius, tness):
    # Draw the first half of the center line
    drawThickenedLine(length / 2, tness)

    # Draw the cross line perpendicular to the center line
    left(90)
    drawThickenedLine((3 * radius) / 2, tness)
    back(3 * radius)
    drawThickenedLine((3 * radius) / 2, tness)
    right(90)

    # Draw the second half of the center line
    drawThickenedLine(length / 2, tness)
    back(length)

    # Draw the right line
    right(90)
    drawThickenedLine(radius, tness)
    left(90)
    drawThickenedLine(length, tness)
    back(length)

    # Draw the left line
    left(90)
    drawThickenedLine(2 * radius, tness)
    right(90)
    drawThickenedLine(length, tness)
    back(length)

    # Re-position the pen at the center of the trace
    right(90)
    fd(radius)
    left(90)

if __name__ == '__main__':
    main()
