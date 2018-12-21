"""
Use turtle to draw
Frank Cwitkowitz
12/27/2015
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
    turtle.up()


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
        turtle.fd(radius-(thickness/2))
        turtle.down()
        turtle.fd(thickness)
        turtle.up()
        turtle.back(radius+(thickness/2))
        turtle.right(angle/(angle))

    """Reset turtle"""
    turtle.left(angle)


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

    turtle.pencolor('red')
    drawArc(radius-(thickness/2)-(highlight/2), angle, highlight)
    turtle.pencolor('black')
    drawArc(radius, angle, thickness)
    turtle.pencolor('red')
    drawArc(radius+(thickness/2)+(highlight/2), angle, highlight)
    turtle.pencolor('black')


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
        turtle.down()
        turtle.fd(length)
        turtle.up()
        turtle.back(length)
        turtle.right(90)
        turtle.fd(1)
        turtle.left(90)
    turtle.right(90)
    turtle.back(thickness)
    turtle.left(90)


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
    turtle.left(90)
    turtle.fd(highlight)
    turtle.right(90)
    turtle.pencolor('red')
    drawLine(length, highlight)
    turtle.right(90)
    turtle.fd(thickness+highlight)
    turtle.left(90)
    drawLine(length, highlight)
    turtle.right(90)
    turtle.back(thickness)
    turtle.left(90)
    turtle.pencolor('black')


def finish():
    """
    removes the pen from the view

    pre-conditions:  turtle is facing up,
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

    ### SEMICICRLE EXAMPLE - turtle.circle(100,180) ###
    drawHighlightedArc(30, 360, 4, 2)
    drawHighlightedArc(100, 360, 4, 2)
    drawHighlightedLine(100, 100, 100)
    finish()
    input("Press ENTER to quit.")
    turtle.bye()

main()
