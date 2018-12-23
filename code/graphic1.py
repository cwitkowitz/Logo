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

SCALE = 150

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
        drawSecondVariant(scale, 1)
        right(30)

def drawFirstVariant(scale, tness):
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
    innerCircleDiameter = 60.28856829 # TODO - figure out how this was calculated
    back(innerCircleDiameter)
    right(90)
    drawThickenedCircle(innerCircleDiameter / 2, 360, tness)
    left(90)
    back(scale - innerCircleDiameter)

    # Draw overlapping squares
    fd(7 * scale / 15)
    left(45)
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
    right(135)
    back(8 * scale / 15)

    # Draw the three outer circles
    fd(scale)
    right(90)
    firstOuterCircleRadius = 29.7
    secondOuterCircleRadius = 15.9
    thirdOuterCircleRadius = 9.2
    drawThickenedCircle(firstOuterCircleRadius, 360, tness - 1)
    left(90)
    fd(2 * firstOuterCircleRadius)
    right(90)
    drawThickenedCircle(secondOuterCircleRadius, 360, tness - 1)
    left(90)
    fd(2 * secondOuterCircleRadius)
    right(90)
    drawThickenedCircle(thirdOuterCircleRadius, 360, tness - 1)
    left(90)
    back(241.2)

    # Draw diamonds linking circles
    fd(179.7)
    left(15)
    drawThickenedLine(23.60429691, tness - 1)
    right(30)
    drawThickenedLine(23.60429691, tness - 1)
    right(150)
    drawThickenedLine(23.60429691, tness - 1)
    right(30)
    drawThickenedLine(23.60429691, tness - 1)
    right(165)
    fd(45.6)
    left(15)
    drawThickenedLine(12.99271607, tness - 1)
    right(30)
    drawThickenedLine(12.99271607, tness - 1)
    right(150)
    drawThickenedLine(12.99271607, tness - 1)
    right(30)
    drawThickenedLine(12.99271607, tness - 1)
    right(165)
    back(225.3)

    # Draw two stems from center of inner circle
    fd(119.8557159)
    right(82.36925982)
    drawThickenedLine(75.67010114, tness - 1)
    back(75.67010114)
    left(2 * 82.36925982)
    drawThickenedLine(75.67010114, tness - 1)
    back(75.67010114)
    right(82.36925982)
    back(119.8557159)

def drawSecondVariant(scale, tness):
    # Draw the larger circle of this variant
    fd(150-38)
    right(90)
    down()
    circle(38)
    up()
    left(90)
    back(150-38)

    # Draw left and right connection to other variant
    fd(150)
    left(120-66.20602311)
    down()
    fd(185.8970512)
    up()
    back(185.8970512)
    right((120-66.20602311)*2)
    down()
    fd(185.8970512)
    up()
    back(185.8970512)
    left(120-66.20602311)
    back(150)

    # Draw inner "V"
    fd(30)
    left(15)
    down()
    fd(70)
    back(70)
    right(30)
    fd(70)
    back(70)
    up()
    left(15)
    back(30)

    # Draw middle "V" point
    fd(80)
    right(30)
    down()
    back(18)
    fd(18)
    left(60)
    back(18)
    fd(18)
    up()
    right(30)
    back(80)

    # Draw outer "V" point
    fd(100)
    right(30)
    down()
    back(26)
    fd(26)
    left(60)
    back(26)
    fd(26)
    up()
    right(30)
    back(100)

    # Draw inner "V" point
    fd(60)
    right(30)
    down()
    back(11)
    fd(11)
    left(60)
    back(11)
    fd(11)
    up()
    right(30)
    back(60)

    # Draw circle with "V"
    fd(112)
    right(90)
    down()
    circle(16.5)
    left(115)
    fd(29)
    back(29)
    right(50)
    fd(29)
    back(29)
    up()
    left(25)
    back(112)

if __name__ == '__main__':
    main()
