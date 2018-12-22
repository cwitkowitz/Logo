"""
Frank Cwitkowitz

Created: 12/16/2015
Revised: 12/22/2018

The trace for the manual drawing of the second graphic.
"""

from turtle import *


def init():
    """
    init initializes the drawing by establishing its pre-conditions

    post conditions: turtle is at origin,
                     turtle is facing right,
                     turtle is pen-down.
    """

    speed(0)
    pencolor('gray')
    up()


def ring(ringSize):
    """
    draws small ring in the middle

    pre-conditions:  turtle is at bottom of the ring
                     turtle is facing right,
                     turtle is pen-up.

    post conditions: turtle is at the center of the ring,
                     turtle is facing up,
                     turtle is pen-up.
    """

    down()
    circle(ringSize)
    up()
    left(90)
    fd((3*ringSize)/8)
    right(90)
    down()
    circle((5*ringSize)/8)
    up()
    left(90)
    fd((5*ringSize)/8)


def halfTrace(length, ringSize):
    """
    draws a half of a trace for a leaf

    pre-conditions:  turtle is at center of the ring
                     turtle is facing in the direction of the trace,
                     turtle is pen-up.

    post conditions: turtle is at the center of the ring,
                     turtle is facing in the direction of the trace,
                     turtle is pen-up.
    """

    """First Half Middle Trace"""
    down()
    fd(length/2)

    """Middle Trace Cross"""
    left(90)
    fd((3*ringSize)/2)
    back(3*ringSize)
    fd((3*ringSize)/2)
    right(90)

    """Second Half Middle Trace"""
    fd(length/2)
    up()
    back(length)

    """Right Trace"""
    right(90)
    fd(ringSize)
    left(90)
    down()
    fd(length)
    up()
    back(length)

    """Left Trace"""
    left(90)
    fd(2*ringSize)
    right(90)
    down()
    fd(length)
    up()
    back(length)

    """Re-Position"""
    right(90)
    fd(ringSize)
    left(90)


def fullTrace(length, ringSize):
    """
    draws a full trace for a leaf

    pre-conditions:  turtle is at center of the ring
                     turtle is facing in the direction of the half trace,
                     turtle is pen-up.

    post conditions: turtle is at the center of the ring,
                     turtle is facing in the direction of the full trace,
                     turtle is pen-up.
    """

    halfTrace(length, ringSize)
    right(180)
    halfTrace(length, ringSize)
    right(180)


def drawTraces(length, ringSize, spreadAngle, numTraces):
    """
    draws all of the traces

    pre-conditions:  turtle is at center of the ring
                     turtle is facing in the direction of the half trace,
                     turtle is pen-up.

    post conditions: turtle is at the center of the ring,
                     turtle is facing up,
                     turtle is pen-up.
    """

    numSideTraces = (numTraces-1)//2

    """Vertical Trace"""
    fullTrace(length, ringSize)

    """Top-Left and Bottom-Right Traces"""
    for x in range(numSideTraces):
        left(spreadAngle)
        fullTrace(length, ringSize)
    """Re-Position"""
    for x in range(numSideTraces):
        right(spreadAngle)

    """Top-Right and Bottom-Left Traces"""
    for x in range(numSideTraces):
        right(spreadAngle)
        fullTrace(length, ringSize)
    """Re-Position"""
    for x in range(numSideTraces):
        left(spreadAngle)


def finish():
    """
    removes the pen from the view

    pre-conditions:  turtle is at the center of the ring,
                     turtle is facing up,
                     turtle is pen-up.

    post conditions: turtle is outside of the screen,
                     turtle is facing up,
                     turtle is pen-up.
    """

    fd(1000)

def main():
    """
    draws as much of the design / trace as it can
    """

    init()
    ringSize = 25
    length = 200
    spreadAngle = 25

    """numTraces should be an odd integer"""
    numTraces = 5

    ring(ringSize)
    drawTraces(length, ringSize, spreadAngle, numTraces)
    finish()
    input("Press ENTER to quit.")
    bye()

main()
