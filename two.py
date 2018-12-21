"""
Use turtle to draw a symmetrical, clean trace to draw on.
Frank Cwitkowitz
12/16/2015
"""

import turtle


def init():
    """
    init initializes the drawing by establishing its pre-conditions

    post conditions: turtle is at origin,
                     turtle is facing right,
                     turtle is pen-down.
    """

    turtle.speed(0)
    turtle.pencolor('gray')
    turtle.up()


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

    turtle.down()
    turtle.circle(ringSize)
    turtle.up()
    turtle.left(90)
    turtle.fd((3*ringSize)/8)
    turtle.right(90)
    turtle.down()
    turtle.circle((5*ringSize)/8)
    turtle.up()
    turtle.left(90)
    turtle.fd((5*ringSize)/8)


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
    turtle.down()
    turtle.fd(length/2)

    """Middle Trace Cross"""
    turtle.left(90)
    turtle.fd((3*ringSize)/2)
    turtle.back(3*ringSize)
    turtle.fd((3*ringSize)/2)
    turtle.right(90)

    """Second Half Middle Trace"""
    turtle.fd(length/2)
    turtle.up()
    turtle.back(length)

    """Right Trace"""
    turtle.right(90)
    turtle.fd(ringSize)
    turtle.left(90)
    turtle.down()
    turtle.fd(length)
    turtle.up()
    turtle.back(length)

    """Left Trace"""
    turtle.left(90)
    turtle.fd(2*ringSize)
    turtle.right(90)
    turtle.down()
    turtle.fd(length)
    turtle.up()
    turtle.back(length)

    """Re-Position"""
    turtle.right(90)
    turtle.fd(ringSize)
    turtle.left(90)


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
    turtle.right(180)
    halfTrace(length, ringSize)
    turtle.right(180)


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
        turtle.left(spreadAngle)
        fullTrace(length, ringSize)
    """Re-Position"""
    for x in range(numSideTraces):
        turtle.right(spreadAngle)

    """Top-Right and Bottom-Left Traces"""
    for x in range(numSideTraces):
        turtle.right(spreadAngle)
        fullTrace(length, ringSize)
    """Re-Position"""
    for x in range(numSideTraces):
        turtle.left(spreadAngle)


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

    turtle.fd(1000)

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
    turtle.bye()

main()
