"""
10/23/16
"""

from turtle import *
from math import *


"""
Outer function that will handle
each piece of the project altogether.
"""
def main(radius, scale, windowXSize):
    init(windowXSize)

    # should begin with the turtle
    # up, centered and facing up.
    draw(radius, scale)
    # test()

    bgcolor('#C1C0CC')

    deInit()


"""
Function to modularize main, in order to
provide an easy way to mess around.
"""
def draw(radius, scale):
    # Radius in scale have different meanings here
    drawCenterPiece(radius)
    right(80)
    drawAppendage(radius, scale)
    right(180)
    drawAppendage(radius, scale)
    right(100)
    """
    ### Just for fun! ###
    left(10)
    drawLoopsPlural(radius, scale)
    right(10)
    """


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
Function that draws a colored thickened line.
"""
def drawColoredLined(length, thickness, color):
    pencolor(color)
    drawThickenedLine(length, thickness)
    pencolor('black')


"""
Function to cover a line with
customizable thickness and color.
"""
def drawLayeredLine(length, thickness, color):
    if thickness[1] != 0:
        drawColoredLined(length, thickness[1], color[1])
    back(length)
    left(90)
    fd((thickness[1] / 2) + (thickness[0] / 2))
    right(90)
    if thickness[0] != 0:
        drawColoredLined(length, thickness[0], color[0])
    back(length)
    right(90)
    fd((thickness[1]) + (thickness[0] / 2) + (thickness[2] / 2))
    left(90)
    if thickness[2] != 0:
        drawColoredLined(length, thickness[2], color[2])
    back(length)
    left(90)
    fd((thickness[1] / 2) + (thickness[2] / 2))
    right(90)
    fd(length)


"""
Function that will draw a normal,
straight line with the provided thickness.
It will end where it starts.
"""
def drawThickenedCircle(radius, extent, thickness):
    pensize(thickness)
    down()
    circle(radius, extent)
    up()
    circle(radius, (360 - extent))
    pensize(1)


"""
Function that draws a colored thickened circle.
"""
def drawColoredCircle(radius, extent, thickness, color):
    pencolor(color)
    drawThickenedCircle(radius, extent, thickness)
    pencolor('black')


"""
Function to cover a circle with
customizable thickness and color.
"""
def drawLayeredCircle(radius, extent, thickness, color):
    if thickness[1] != 0:
        drawColoredCircle(radius, extent, thickness[1], color[1])
    right(90)
    back((thickness[1] / 2) + (thickness[0] / 2))
    left(90)
    if thickness[0] != 0:
        drawColoredCircle((radius - (thickness[1] / 2) - (thickness[0] / 2)), extent, thickness[0], color[0])
    left(90)
    back((thickness[1]) + (thickness[0] / 2) + (thickness[2] / 2))
    right(90)
    if thickness[2] != 0:
        drawColoredCircle((radius + (thickness[1] / 2) + (thickness[2] / 2)), extent, thickness[2], color[2])
    left(90)
    fd((thickness[1] / 2) + (thickness[2] / 2))
    right(90)


"""
Function that sets up the project.
"""
def init(windowXSize):
    setup(windowXSize, windowXSize, None, None)
    speed(0)
    pencolor('black')
    up()
    left(90)


"""
Function that handles the closing
cleanup of the project.
"""
def deInit():
    up()
    forward(1000)
    input("Press ENTER to quit.")
    bye()


"""
Function to draw the middle circle and
any fills.
"""
def drawCenterPiece(radius):
    # Small inner circle
    right(90)
    fd(.35 * radius)
    left(90)
    drawLayeredCircle((.35 * radius), 360, [2, 3, 2], ['black', 'purple', 'black'])
    right(90)
    back(.35 * radius)
    left(90)

    # Big outer circle
    right(90)
    fd(radius)
    left(90)
    drawLayeredCircle(radius, 360, [2, 3, 2], ['black', 'purple', 'black'])
    right(90)
    back(radius)
    left(90)

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
    drawLayeredLine((2.3 * scale), [1, 2, 1], ['black', 'purple', 'black'])
    fd(radius * scale)
    left(90)
    drawLayeredCircle((radius * scale), 360, [1, 2, 1], ['black', 'purple', 'black'])
    right(90)
    back(radius * scale)

    drawFills(scale)

    # Side slants
    back(2.3 * scale)
    left(90)
    fd(.65 * scale)
    right(90)
    right(90 - degrees(atan((2.3 * scale) / (.65 * scale))))
    drawLayeredLine(((.65 * scale) / cos(radians(degrees(atan((2.3 * scale) / (.65 * scale)))))), [1, 2, 1], ['black', 'purple', 'black'])
    back((.65 * scale) / cos(radians(degrees(atan((2.3 * scale) / (.65 * scale))))))
    left(90 - degrees(atan((2.3 * scale) / (.65 * scale))))
    left(90)
    back(2 * (.65 * scale))
    right(degrees(atan((2.3 * scale) / (.65 * scale))))
    drawLayeredLine(((.65 * scale) / cos(radians(degrees(atan((2.3 * scale) / (.65 * scale)))))), [1, 2, 1], ['black', 'purple', 'black'])
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
    drawLayeredCircle((1.16 * 2.3 * radius), 120, [1, 2, 1], ['black', 'purple', 'black'])
    right(30)


main(100, .15, 550)
