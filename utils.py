"""
Frank Cwitkowitz

Created: 12/27/2015
Revised: 12/22/2018

Utilities for my graphic designs. Mostly just common functions for drawing.
"""

from turtle import *

##############################################################################
# Setup and Cleanup                                                          #
##############################################################################

def graphicInit(p_col, b_col, winSize):
    """
    init initializes the drawing by establishing its pre-conditions

    post conditions: turtle is at origin,
                     turtle is facing right,
                     turtle is pen-down.
    """

    speed(0)
    pencolor(p_col)
    bgcolor(b_col)
    setup(winSize, winSize, None, None)
    up()


def graphicFin():
    """
    removes the pen from the view

    pre-conditions:  turtle is facing up,
                     turtle is pen-up.

    post conditions: turtle is outside of the screen,
                     turtle is facing up,
                     turtle is pen-up.
    """

    up()
    forward(1000)
    input("Press ENTER to quit.")
    bye()

##############################################################################
# Drawing Tools                                                              #
##############################################################################

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
It will end where it starts.
"""
def drawThickenedCircle(radius, extent, thickness):
    pensize(thickness)
    down()
    circle(radius, extent)
    up()
    circle(radius, (360 - extent))
    pensize(1)

def drawCorner(scale, hyp, tness, in_units, out_units, width_units):
    left(135)
    drawThickenedLine(in_units * scale, tness)
    right(90)
    fd(width_units * scale)
    right(90)
    drawThickenedLine(out_units * scale, tness)
    right(90)
    drawThickenedLine(out_units * scale, tness)
    right(90)
    fd(width_units * scale)
    right(90)
    drawThickenedLine(in_units * scale, tness)
    right(45)
