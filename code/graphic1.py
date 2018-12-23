"""
Frank Cwitkowitz

Created: 07/18/2015
Revised: 12/22/2018

The one that started it all.
"""

from utils import *

from turtle import *

PEN_COLOR = '#FFFFFF'
BG_COLOR  = '#C1C0CC'
WIN_SIZE  = 500

SCALE     = 100
FILL_SHPS = 1

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
    drawThickenedCircle(scale, 360, 1)
    left(90)
    fd(scale)

    # Draw the same repeated design six times
    for i in range(0, 6):
        drawFirstVariant(scale, 2)
        right(30)
        drawSecondVariant(scale, 2)
        right(30)

def drawFirstVariant(scale, tness):
    # TODO - I am not sure how I calculated these lengths and angles...
    #        My calculations are buried in a journal somewhere and I will
    #        update these when I find them. For now the magic number are just
    #        used to scale the parameters.
    innerCircleDiameter = 6.028856829 * scale / 15
    firstOuterCircleRadius = 2.97 * scale / 15
    secondOuterCircleRadius = 1.59 * scale / 15
    thirdOuterCircleRadius = 0.92 * scale / 15
    largeDiamondSide = 2.360429691 * scale / 15
    smallDiamondSide = 1.299271607 * scale / 15
    stemLineLength = 7.567010114 * scale / 15
    stemLineAngle = 82.36925982

    # Draw the inside and outside spike outline
    right(15)
    drawThickenedLine(scale, tness)
    left(30)
    drawThickenedLine(scale, tness)
    left(150)
    drawThickenedLine(scale, tness)
    left(30)
    drawThickenedLine(scale, tness)
    left(165)

    # Draw the center line of the variant and the inner circle
    drawThickenedLine(scale, tness)
    back(innerCircleDiameter)
    right(90)
    drawThickenedCircle(innerCircleDiameter / 2, 360, tness)
    left(90)
    back(scale - innerCircleDiameter)

    # Draw overlapping squares
    fd(7 * scale / 15)
    left(45)
    if FILL_SHPS:
        fillcolor(PEN_COLOR)
        begin_fill()
    drawThickenedLine(scale / 10, tness - 1)
    right(90)
    drawThickenedLine(scale / 10, tness - 1)
    right(90)
    drawThickenedLine(scale / 10, tness - 1)
    right(90)
    drawThickenedLine(scale / 10, tness - 1)
    right(135)
    fd(scale / 15)
    left(45)
    drawThickenedLine(scale / 10, tness - 1)
    right(90)
    drawThickenedLine(scale / 10, tness - 1)
    right(90)
    drawThickenedLine(scale / 10, tness - 1)
    right(90)
    drawThickenedLine(scale / 10, tness - 1)
    if FILL_SHPS:
        end_fill()
    right(135)
    back(8 * scale / 15)

    # Draw the three outer circles
    fd(scale)
    right(90)
    drawThickenedCircle(firstOuterCircleRadius, 360, tness)
    left(90)
    fd(2 * firstOuterCircleRadius)
    right(90)
    drawThickenedCircle(secondOuterCircleRadius, 360, tness)
    left(90)
    fd(2 * secondOuterCircleRadius)
    right(90)
    drawThickenedCircle(thirdOuterCircleRadius, 360, tness)
    left(90)
    back(scale + 2 * firstOuterCircleRadius + 2 * secondOuterCircleRadius)

    # Draw diamonds linking circles
    fd(scale + firstOuterCircleRadius)
    left(15)
    if FILL_SHPS:
        fillcolor(PEN_COLOR)
        begin_fill()
    drawThickenedLine(largeDiamondSide, tness - 1)
    right(30)
    drawThickenedLine(largeDiamondSide, tness - 1)
    right(150)
    drawThickenedLine(largeDiamondSide, tness - 1)
    right(30)
    drawThickenedLine(largeDiamondSide, tness - 1)
    right(165)
    fd(firstOuterCircleRadius + secondOuterCircleRadius)
    left(15)
    drawThickenedLine(smallDiamondSide, tness - 1)
    right(30)
    drawThickenedLine(smallDiamondSide, tness - 1)
    right(150)
    drawThickenedLine(smallDiamondSide, tness - 1)
    right(30)
    drawThickenedLine(smallDiamondSide, tness - 1)
    if FILL_SHPS:
        end_fill()
    right(165)
    back(scale + 2 * firstOuterCircleRadius + secondOuterCircleRadius)

    # Draw two stems from center of inner circle
    fd(scale - innerCircleDiameter / 2)
    right(stemLineAngle)
    drawThickenedLine(stemLineLength, tness - 1)
    back(stemLineLength)
    left(2 * stemLineAngle)
    drawThickenedLine(stemLineLength, tness - 1)
    back(stemLineLength)
    right(stemLineAngle)
    back(scale - innerCircleDiameter / 2)

def drawSecondVariant(scale, tness):
    # TODO - I am not sure how I calculated these lengths and angles...
    #        My calculations are buried in a journal somewhere and I will
    #        update these when I find them. For now the magic number are just
    #        used to scale the parameters.
    largeCircleRadius = 3.8 * scale / 15
    wingAngle = 120 - 66.20602311
    wingLength = 18.58970512 * scale / 15
    innerVLength = 1.1 * scale / 15
    middleVLength = 1.8 * scale / 15
    outerVLength = 2.6 * scale / 15
    smallCircleRadius = 1.65 * scale / 15
    smallCircleChord = 2.9 * scale / 15

    # Draw the larger circle of this variant
    fd(scale - largeCircleRadius)
    right(90)
    drawThickenedCircle(largeCircleRadius, 360, tness)
    left(90)
    back(scale - largeCircleRadius)

    # Draw left and right connection to other variant
    fd(scale)
    left(wingAngle)
    drawThickenedLine(wingLength, tness)
    back(wingLength)
    right(2 * wingAngle)
    drawThickenedLine(wingLength, tness)
    back(wingLength)
    left(wingAngle)
    back(scale)

    # Draw inner "V"
    fd(3 * scale / 15)
    left(15)
    drawThickenedLine(7 * scale / 15, tness - 1)
    back(7 * scale / 15)
    right(30)
    drawThickenedLine(7 * scale / 15, tness - 1)
    back(7 * scale / 15)
    left(15)
    back(3 * scale / 15)

    # Draw middle "V" point
    fd(8 * scale / 15)
    right(30)
    back(middleVLength)
    drawThickenedLine(middleVLength, tness)
    left(60)
    back(middleVLength)
    drawThickenedLine(middleVLength, tness)
    right(30)
    back(8 * scale / 15)

    # Draw outer "V" point
    fd(10 * scale / 15)
    right(30)
    back(outerVLength)
    drawThickenedLine(outerVLength, tness)
    left(60)
    back(outerVLength)
    drawThickenedLine(outerVLength, tness)
    right(30)
    back(10 * scale / 15)

    # Draw inner "V" point
    fd(6 * scale / 15)
    right(30)
    back(innerVLength)
    drawThickenedLine(innerVLength, tness)
    left(60)
    back(innerVLength)
    drawThickenedLine(innerVLength, tness)
    right(30)
    back(6 * scale / 15)

    # Draw circle with "V"
    fd(scale - largeCircleRadius)
    right(90)
    drawThickenedCircle(smallCircleRadius, 360, tness)
    left(115)
    drawThickenedLine(smallCircleChord, tness - 1)
    back(smallCircleChord)
    right(50)
    drawThickenedLine(smallCircleChord, tness - 1)
    back(smallCircleChord)
    left(25)
    back(scale - largeCircleRadius)

if __name__ == '__main__':
    main()
