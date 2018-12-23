"""
Frank Cwitkowitz

Created: 12/27/2015
Revised: 12/22/2018

Utilities for my graphic designs. Mostly just common functions for drawing.
"""

from turtle import *

from PIL import Image

import os

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

def graphicFin(img_name):
    hideturtle()
    input("Press ENTER to quit.")
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

def drawFilledCircle(radius, extent, thickness, col):
    fillcolor(col)
    begin_fill()
    drawThickenedCircle(radius, extent, thickness)
    end_fill()

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
