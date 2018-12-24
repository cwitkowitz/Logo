"""
Frank Cwitkowitz

Created: 07/18/2015
Revised: 12/22/2018

The one that started it all.
"""

from utils import *

from turtle import *
from math import *

PEN_COLOR = '#000000'
BG_COLOR  = '#C1C0CC'
WIN_SIZE  = 500
FILL_SHPS = 1

SCALE     = 115
SEC_COLOR = '#CCCCCC'
THR_COLOR = '#0F00CC'

"""
Outer function that will handle each piece of the project altogether.
"""
def main():
    graphicInit(PEN_COLOR, BG_COLOR, WIN_SIZE)
    drawFigure(SCALE)
    graphicFin('graphic1')

def drawFigure(scale):
    # Draw the large center circle
    right(90)
    fd(scale)
    left(90)
    if FILL_SHPS: shapeFillStart(THR_COLOR)
    drawThickenedCircle(scale, 360, 2)
    if FILL_SHPS: shapeFillEnd()
    left(90)
    fd(scale)

    # Draw the first repeated design six times
    for i in range(6):
        drawFirstVariant(scale, 2)
        right(60)

    right(30)
    # Draw the first repeated design six times
    for i in range(6):
        drawSecondVariant(scale, 2)
        right(60)

def drawInnerSlice(scale, tness):
    # Draw the inside of the spike outline
    left(15)
    fd(scale)
    right(180)
    if FILL_SHPS: shapeFillStart(SEC_COLOR)
    drawThickenedLine(scale, tness)
    left(150)
    drawThickenedLine(scale, tness)
    left(90)
    drawThickenedArc(scale, 30, tness)
    if FILL_SHPS:
        shapeFillEnd()
    drawThickenedArc(scale, 330, tness)
    right(90)
    back(scale)
    left(15)

def drawOuterSlice(scale, tness):
    # Draw the inside and outside spike outline
    right(15)
    fd(scale)
    left(90)
    if FILL_SHPS: shapeFillStart(PEN_COLOR)
    drawThickenedArc(scale, 30, tness)
    right(120)
    drawThickenedLine(scale, tness)
    right(150)
    drawThickenedLine(scale, tness)
    if FILL_SHPS:
        shapeFillEnd()
    left(150)
    back(scale)
    left(15)

def drawVs(scale, tness):
    vLength = 7 * scale / 15
    outerVLength = 3 * vLength / 4
    innerVLength = outerVLength / 3
    middleVLength = 2 * innerVLength

    # Draw inner "V"
    fd(3 * scale / 15)
    left(15)
    drawThickenedLine(vLength, tness)
    back(vLength)
    right(30)
    drawThickenedLine(vLength, tness)
    back(vLength)

    # Draw largest outer "V"
    left(30)
    if FILL_SHPS: shapeFillStart(PEN_COLOR)
    drawThickenedLine(outerVLength, tness)
    right(45)
    pointLength = outerVLength * (sin(radians(15)) / sin(radians(30)))
    drawThickenedLine(pointLength, tness)
    right(120)
    drawThickenedLine(pointLength, tness)
    right(45)
    drawThickenedLine(outerVLength, tness)
    if FILL_SHPS: shapeFillEnd()
    right(150)

    # Draw second-largest outer "V"
    if FILL_SHPS: shapeFillStart(SEC_COLOR)
    drawThickenedLine(middleVLength, tness)
    right(45)
    pointLength = middleVLength * (sin(radians(15)) / sin(radians(30)))
    drawThickenedLine(pointLength, tness)
    right(120)
    drawThickenedLine(pointLength, tness)
    right(45)
    drawThickenedLine(middleVLength, tness)
    if FILL_SHPS: shapeFillEnd()
    right(150)

    # Draw smallest outer "V"
    if FILL_SHPS: shapeFillStart(THR_COLOR)
    drawThickenedLine(innerVLength, tness)
    right(45)
    pointLength = innerVLength * (sin(radians(15)) / sin(radians(30)))
    drawThickenedLine(pointLength, tness)
    right(120)
    drawThickenedLine(pointLength, tness)
    right(45)
    drawThickenedLine(innerVLength, tness)
    if FILL_SHPS: shapeFillEnd()
    right(120)

    # Return to center
    right(45)
    back(3 * scale / 15)

def drawSquares(scale, tness):
    # Draw overlapping squares
    fd(7 * scale / 15)
    left(45)
    if FILL_SHPS: shapeFillStart(PEN_COLOR)
    drawThickenedLine(scale / 10, tness)
    right(90)
    drawThickenedLine(scale / 10, tness)
    right(90)
    drawThickenedLine(scale / 10, tness)
    right(90)
    drawThickenedLine(scale / 10, tness)
    right(135)
    fd(scale / 15)
    left(45)
    drawThickenedLine(scale / 10, tness)
    right(90)
    drawThickenedLine(scale / 10, tness)
    right(90)
    drawThickenedLine(scale / 10, tness)
    right(90)
    drawThickenedLine(scale / 10, tness)
    if FILL_SHPS: shapeFillEnd()
    right(135)
    back(8 * scale / 15)

def drawCircles(scale, tness):
    firstOuterCircleRadius = 2.97 * scale / 15
    secondOuterCircleRadius = 1.59 * scale / 15
    thirdOuterCircleRadius = 0.92 * scale / 15
    largeDiamondSide = 2.360429691 * scale / 15
    smallDiamondSide = 1.299271607 * scale / 15

    # Draw the three outer circles
    fd(scale)
    right(90)
    if FILL_SHPS: shapeFillStart(SEC_COLOR)
    drawThickenedCircle(firstOuterCircleRadius, 360, tness)
    if FILL_SHPS: shapeFillEnd()
    left(90)
    fd(2 * firstOuterCircleRadius)
    right(90)
    if FILL_SHPS: shapeFillStart(SEC_COLOR)
    drawThickenedCircle(secondOuterCircleRadius, 360, tness)
    if FILL_SHPS: shapeFillEnd()
    left(90)
    fd(2 * secondOuterCircleRadius)
    right(90)
    if FILL_SHPS: shapeFillStart(SEC_COLOR)
    drawThickenedCircle(thirdOuterCircleRadius, 360, tness)
    if FILL_SHPS: shapeFillEnd()
    left(90)
    back(scale + 2 * firstOuterCircleRadius + 2 * secondOuterCircleRadius)

    # Draw diamonds linking circles
    fd(scale + firstOuterCircleRadius)
    left(15)
    if FILL_SHPS: shapeFillStart(PEN_COLOR)
    drawThickenedLine(largeDiamondSide, tness)
    right(30)
    drawThickenedLine(largeDiamondSide, tness)
    right(150)
    drawThickenedLine(largeDiamondSide, tness)
    right(30)
    drawThickenedLine(largeDiamondSide, tness)
    right(165)
    fd(firstOuterCircleRadius + secondOuterCircleRadius)
    left(15)
    drawThickenedLine(smallDiamondSide, tness)
    right(30)
    drawThickenedLine(smallDiamondSide, tness)
    right(150)
    drawThickenedLine(smallDiamondSide, tness)
    right(30)
    drawThickenedLine(smallDiamondSide, tness)
    if FILL_SHPS: shapeFillEnd()
    right(165)
    back(scale + 2 * firstOuterCircleRadius + secondOuterCircleRadius)

def drawVCircle(scale, tness):
    largeCircleRadius = 3.8 * scale / 15
    smallCircleRadius = 1.65 * scale / 15
    smallCircleChord = 2 * smallCircleRadius * cos(radians(25))

    # Draw circle with "V"
    fd(scale - largeCircleRadius)
    right(90)
    if FILL_SHPS: shapeFillStart(THR_COLOR)
    drawThickenedCircle(smallCircleRadius, 360, tness)
    if FILL_SHPS:
        shapeFillEnd()
        shapeFillStart(PEN_COLOR)
    left(65)
    drawThickenedLine(smallCircleChord, tness)
    left(65)
    drawThickenedArc(smallCircleRadius, 100, tness)
    left(65)
    drawThickenedLine(smallCircleChord, tness)
    if FILL_SHPS: shapeFillEnd()
    left(155)
    back(scale - largeCircleRadius)

def drawCrossDetails(scale, tness):
    largeCircleRadius = 3.8 * scale / 15
    stemLineLength = 7.567010114 * scale / 15
    stemLineAngle = 90 - 82.36925982 + 45

    # Draw two stems from center of inner circle
    fd(scale)
    right(stemLineAngle)

    back(largeCircleRadius)
    right(90)
    if FILL_SHPS: shapeFillStart(PEN_COLOR)
    drawThickenedArc(largeCircleRadius, 2 * stemLineAngle, tness)
    left(90)
    drawThickenedLine(largeCircleRadius, tness)
    left(180 - 2 * stemLineAngle)
    drawThickenedLine(largeCircleRadius, tness)
    if FILL_SHPS: shapeFillEnd()

    right(180)
    back(stemLineLength - largeCircleRadius)
    drawThickenedLine(stemLineLength, tness)
    left(2 * stemLineAngle)
    back(stemLineLength)
    drawThickenedLine(stemLineLength, tness)
    right(stemLineAngle)
    back(scale)

def drawOuterWing(scale, tness):
    wingAngle = 120 - 66.20602311
    wingLength = 18.58970512 * scale / 15
    # Draw left and right connection to other variant
    fd(scale)
    left(90)
    if FILL_SHPS: shapeFillStart(THR_COLOR)
    drawThickenedArc(scale, 30, tness)
    right(90 + wingAngle)
    drawThickenedLine(wingLength, tness)
    left(wingAngle - 30)
    right(180)
    left(0.5 * (180 - 2 * ((90 - wingAngle) + 30)))
    drawThickenedLine(wingLength, tness)
    if FILL_SHPS: shapeFillEnd()
    left(180 - wingAngle)
    back(scale)
    left(30)

def drawFirstVariant(scale, tness):
    # TODO - I am not sure how I calculated these lengths and angles...
    #        My calculations are buried in a journal somewhere and I will
    #        update these when I find them. For now the magic number are just
    #        used to scale the parameters.
    innerCircleDiameter = 6.028856829 * scale / 15

    drawOuterWing(scale, tness)

    drawOuterSlice(scale, tness)

    # Draw the center line of the variant and the inner circle
    drawThickenedLine(scale - innerCircleDiameter, tness)
    right(90)
    if FILL_SHPS: shapeFillStart(SEC_COLOR)
    drawThickenedCircle(innerCircleDiameter / 2, 360, tness)
    if FILL_SHPS: shapeFillEnd()
    left(90)
    back(scale - innerCircleDiameter)

    drawSquares(scale, tness)

    drawCircles(scale, tness)

def drawSecondVariant(scale, tness):
    # TODO - I am not sure how I calculated these lengths and angles...
    #        My calculations are buried in a journal somewhere and I will
    #        update these when I find them. For now the magic number are just
    #        used to scale the parameters.
    largeCircleRadius = 3.8 * scale / 15
    wingAngle = 120 - 66.20602311
    wingLength = 18.58970512 * scale / 15

    drawInnerSlice(scale, tness)

    # Draw the larger circle of this variant
    fd(scale - largeCircleRadius)
    right(90)
    if FILL_SHPS: shapeFillStart(SEC_COLOR)
    drawThickenedCircle(largeCircleRadius, 360, tness)
    if FILL_SHPS: shapeFillEnd()
    left(90)
    back(scale - largeCircleRadius)

    drawVs(scale, tness)

    drawCrossDetails(scale, tness)

    drawVCircle(scale, tness)

    # Fill in left side of eye
    fd(scale)
    left(90)
    if FILL_SHPS: shapeFillStart(PEN_COLOR)
    drawThickenedArc(scale, 15, tness)
    drawThickenedArc(scale, -15, tness)
    right(90 - wingAngle)
    drawThickenedLine(largeCircleRadius, tness)
    left(90)
    drawThickenedArc(largeCircleRadius, wingAngle - 7.5, tness)
    if FILL_SHPS: shapeFillEnd()
    drawThickenedArc(largeCircleRadius, -(wingAngle - 7.5), tness)
    right(90)
    back(largeCircleRadius)
    left(90 - wingAngle)
    right(90)
    back(scale)

    # Fill in right side of eye
    fd(scale)
    left(90)
    if FILL_SHPS: shapeFillStart(PEN_COLOR)
    drawThickenedArc(scale, -15, tness)
    drawThickenedArc(scale, 15, tness)
    right(90 + wingAngle)
    drawThickenedLine(largeCircleRadius, tness)
    left(90)
    drawThickenedArc(largeCircleRadius, -(wingAngle - 7.5), tness)
    if FILL_SHPS: shapeFillEnd()
    drawThickenedArc(largeCircleRadius, wingAngle - 7.5, tness)
    right(90)
    back(largeCircleRadius)
    left(wingAngle)
    back(scale)

if __name__ == '__main__':
    main()
