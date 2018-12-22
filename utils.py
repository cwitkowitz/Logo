"""
Frank Cwitkowitz

Created: 12/27/2015
Revised: 12/22/2018

Utilities for my graphic designs. Mostly just common functions for drawing.
"""

from turtle import *

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

def drawArc(radius, angle, thickness):
    """
    draws an arc

    pre-conditions:  turtle is at the center of the arc,
                     turtle is facing in the direction of the left part of the arc,
                     turtle is pen-up.

    post conditions: turtle is at the center of the arc,
                     turtle is facing in the direction of the left part of the arc,
                     turtle is pen-up.
    """

    """Draw arc"""
    for x in range(angle):
        fd(radius-(thickness/2))
        down()
        fd(thickness)
        up()
        back(radius+(thickness/2))
        right(angle/(angle))

    """Reset turtle"""
    left(angle)


def drawHighlightedArc(radius, angle, thickness, highlight):
    """
    draws a highlighted arc

    pre-conditions:  turtle is at the center of the arc,
                     turtle is facing in the direction of the left part of the arc,
                     turtle is pen-up.

    post conditions: turtle is at the center of the arc,
                     turtle is facing in the direction of the left part of the arc,
                     turtle is pen-up.
    """

    pencolor('red')
    drawArc(radius-(thickness/2)-(highlight/2), angle, highlight)
    pencolor('black')
    drawArc(radius, angle, thickness)
    pencolor('red')
    drawArc(radius+(thickness/2)+(highlight/2), angle, highlight)
    pencolor('black')


def drawLine(length, thickness):
    """
    draws a thick line

    pre-conditions:  turtle is at the start of the line,
                     turtle is facing in the direction of the line,
                     turtle is pen-up.

    post conditions: turtle is at the start of the line,
                     turtle is facing in the direction of the line,
                     turtle is pen-up.
    """

    for x in range(thickness):
        down()
        fd(length)
        up()
        back(length)
        right(90)
        fd(1)
        left(90)
    right(90)
    back(thickness)
    left(90)


def drawHighlightedLine(length, thickness, highlight):
    """
    draws a thick highlighted line

    pre-conditions:  turtle is at the start of the line,
                     turtle is facing in the direction of the line,
                     turtle is pen-up.

    post conditions: turtle is at the start of the line,
                     turtle is facing in the direction of the line,
                     turtle is pen-up.
    """

    drawLine(length, thickness)
    left(90)
    fd(highlight)
    right(90)
    pencolor('red')
    drawLine(length, highlight)
    right(90)
    fd(thickness+highlight)
    left(90)
    drawLine(length, highlight)
    right(90)
    back(thickness)
    left(90)
    pencolor('black')

def main():
    """
    draws as much of the design / trace as it can
    """

    init()

    ### SEMICICRLE EXAMPLE - turtle.circle(100,180) ###
    drawHighlightedArc(30, 360, 4, 2)
    drawHighlightedArc(100, 360, 4, 2)
    drawHighlightedLine(100, 100, 100)
    finish()
    input("Press ENTER to quit.")
    bye()
