"""
Frank Cwitkowitz

Created: 12/27/2015
Revised: 12/22/2018

Utilities for my graphic designs. Mostly just common functions for drawing.
"""

from turtle import *

from PIL import Image

##############################################################################
# Setup and Cleanup                                                          #
##############################################################################

def graphicInit(p_col, b_col, winSize):
    speed(0)
    pencolor(p_col)
    setup(winSize, winSize, None, None)
    up()
    fd(winSize)
    left(90)
    drawFilledCircle(winSize, 360, 1, b_col)
    right(90)
    back(winSize)

def graphicFin(img_name, save):
    hideturtle()
    input("Press ENTER to quit.")
    if save:
        ps_path = '../output/postscript/' + img_name + '.eps'
        png_path = '../output/imgs/' + img_name + '.png'
        getscreen().getcanvas().postscript(file = ps_path)
        img = Image.open(ps_path)
        img.save(png_path, 'png')
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
Function that draws a colored thickened line.
"""
def drawColoredLine(length, thickness, color):
    pencolor(color)
    drawThickenedLine(length, thickness)
    pencolor('black')

"""
Function to cover a line with
customizable thickness and color.
"""
def drawLayeredLine(length, thickness, color):
    left(90)
    fd((thickness[1] // 2) + (thickness[0] // 2))
    right(90)
    shapeFillStart(color[1])
    drawColoredLine(length, thickness[0], color[0])
    right(90)
    fd((thickness[0] // 2) + thickness[1] + (thickness[2] // 2))
    right(90)
    drawColoredLine(length, thickness[2], color[2])
    shapeFillEnd()
    back(length)
    left(90)
    back((thickness[1] // 2) + (thickness[2] // 2))
    left(90)

def drawThickenedArc(radius, extent, thickness):
    pensize(thickness)
    down()
    circle(radius, extent)
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

"""
Function that draws a colored thickened circle.
"""
def drawColoredCircle(radius, extent, thickness, color):
    pencolor(color)
    drawThickenedCircle(radius, extent, thickness)
    pencolor('black')

def drawFilledCircle(radius, extent, thickness, col):
    fillcolor(col)
    begin_fill()
    drawThickenedCircle(radius, extent, thickness)
    end_fill()

"""
Function to cover a circle with
customizable thickness and color.
"""
def drawLayeredCircle(radius, extent, thickness, color):
    shapeFillStart(color[1])
    drawColoredCircle(radius, extent, thickness[0], color[0])
    shapeFillEnd()
    left(90)
    fd((thickness[0] // 2) + thickness[1] + (thickness[2] // 2))
    right(90)
    shapeFillStart(color[3])
    drawColoredCircle(radius - (thickness[0] // 2) - thickness[1] - (thickness[2] // 2), extent, thickness[2], color[2])
    shapeFillEnd()
    right(90)
    fd((thickness[0] // 2) + thickness[1] + (thickness[2] // 2))
    left(90)

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

def shapeFillStart(col):
    fillcolor(col)
    begin_fill()

def shapeFillEnd():
    end_fill()
