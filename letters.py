"""
Frank Cwitkowitz

Created: Unknown - Sometime during late 2018
Revised: 12/22/2018

Functions to draw letters.
"""

from turtle import *
from math import *
from Logo import draw_Logo

VERT  = 50
HOR   = 20
MARG  = 7
THIC  = 4
DOT   = 2
SEP   = MARG
TRAIL = 10

"""
Assume bottom left, facing right, turtle off
TODO - Clean up if posting on GitHub
"""

def main():
    bgcolor("#F0F0F0")
    speed(0)
    pensize(THIC)
    draw_F()
    draw_r()
    fd(HOR)
    left(90)
    back(MARG / 2)
    draw_Logo(VERT + MARG, None)
    fd(MARG / 2)
    right(90)
    # TODO - Shouldn't have to change pensize again
    pensize(THIC)
    back(3 * HOR + 2 * MARG)
    left(90)
    back(VERT + MARG)
    right(90)
    draw_C()
    draw_w()
    fd(1000)
    input("Press ENTER to quit.")
    bye()

"""
def main():
    speed(0)
    pensize(THIC)
    draw_F()
    draw_r()
    fd(HOR)
    left(90)
    back(MARG / 2)
    draw_Logo(VERT + MARG, None)
    fd(MARG / 2)
    right(90)
    # TODO - Shouldn't have to change pensize again
    pensize(THIC)
    fd(HOR + MARG)
    draw_n()
    draw_k()
    back(6 * HOR + 5 * MARG)
    left(90)
    back(VERT + MARG)
    right(90)
    draw_C()
    draw_w()
    fd(2 * HOR + MARG)
    draw_t()
    draw_k()
    draw_o()
    draw_w()
    draw_i()
    draw_t()
    draw_z()
    down()
    back(MARG)
    fd(MARG + TRAIL)
    input("Press ENTER to quit.")
    bye()
"""

def draw_z():
    down()
    fd(HOR)
    back(HOR)
    theta = degrees(atan((VERT / 2) / HOR))
    left(theta)
    diag = HOR / cos(radians(theta))
    fd(diag)
    right(theta)
    back(HOR)
    up()
    left(90)
    back(VERT / 2)
    right(90)
    fd(HOR + MARG)

def draw_i():
    fd(HOR / 2)
    left(90)
    down()
    fd(VERT / 2)
    up()
    fd(SEP)
    right(90)
    fd(DOT)
    left(90)
    fd(DOT)
    down()
    circle(DOT)
    up()
    back(DOT)
    right(90)
    back(DOT)
    left(90)
    back(SEP + VERT / 2)
    right(90)
    fd(HOR / 2 + MARG)

def draw_o():
    fd(HOR / 2)
    down()
    circle(HOR / 2)
    up()
    fd(HOR / 2 + MARG)
    

def draw_t():
    fd(HOR / 2)
    left(90)
    down()
    fd(VERT)
    back(VERT / 2)
    right(90)
    fd(HOR / 2)
    back(HOR)
    fd(HOR / 2)
    left(90)
    back(VERT / 2)
    up()
    right(90)
    fd(HOR / 2 + MARG)

def draw_w():
    left(90)
    fd(VERT / 2)
    theta = degrees(atan((HOR / 3) / (VERT / 2)))
    right(180 - theta)
    down()
    leg1 = (VERT / 2) / cos(radians(theta))
    fd(leg1)
    right(theta)
    left(90)
    left(90 - theta)
    leg2 = (VERT / 4) / cos(radians(theta))
    fd(leg2)
    right(180 - 2 * theta)
    fd(leg2)
    left(180 - 2 * theta)
    fd(leg1)
    left(theta)
    up()
    back(VERT / 2)
    right(90)
    fd(MARG)

def draw_C():
    fd(HOR)
    left(90)
    fd(VERT - HOR / 2)
    down()
    circle((HOR / 2), 180)
    fd(VERT - HOR)
    circle((HOR / 2), 180)
    up()
    back(HOR / 2)
    right(90)
    fd(MARG)

def draw_k():
    down()
    left(90)
    fd(VERT)
    back(VERT / 2)
    right(30)
    fd(VERT / 2)
    back(VERT / 2)
    left(30)
    right(180)
    theta = degrees(atan((VERT / 2) / HOR))
    left(90 - theta)
    diag = HOR / cos(radians(theta))
    fd(diag)
    back(diag)
    up()
    right(90 - theta)
    fd(VERT / 2)
    left(90)
    fd(HOR + MARG)

def draw_n():
    down()
    left(90)
    fd(VERT / 2)
    back(VERT / 4)
    right(90)
    up()
    fd(HOR)
    left(90)
    down()
    back(VERT / 4)
    fd(VERT / 4)
    circle((HOR / 2), 180)
    up()
    fd(VERT / 4)
    left(90)
    fd(HOR + MARG)

def draw_r():
    down()
    left(90)
    fd(VERT / 2)
    back(VERT / 4)
    right(90)
    up()
    fd(HOR)
    left(90)
    down()
    circle((HOR / 2), 180)
    up()
    fd(VERT / 4)
    left(90)
    fd(HOR + MARG)

def draw_F():
    down()
    left(90)
    fd(VERT)
    right(90)
    fd(HOR)
    back(HOR)
    left(90)
    back(VERT / 2)
    right(90)
    fd(HOR / 2)
    back(HOR / 2)
    left(90)
    back(VERT / 2)
    right(90)
    up()
    fd(HOR + MARG)

main()
