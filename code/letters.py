"""
Frank Cwitkowitz

Created: Unknown - Sometime during late 2018
Revised: 12/22/2018

Functions to draw letters.
"""

from utils import *

from turtle import *
from math import *

def draw_z(v, h, m, d, t):
    drawThickenedLine(h, t)
    theta = degrees(atan((v / 2) / h))
    left((90 - theta) + 90)
    diag = h / cos(radians(theta))
    drawThickenedLine(diag, t)
    right((90 - theta) + 90)
    drawThickenedLine(h, t)
    right(90)
    fd(v / 2)
    left(90)
    fd(m)

def draw_i(v, h, m, d, t):
    fd(h / 2)
    left(90)
    drawThickenedLine(v / 2, t)
    fd(m)
    right(90)
    fd(d)
    left(90)
    fd(d)
    drawThickenedCircle(d, 360, t)
    back(d)
    right(90)
    back(d)
    left(90)
    back(m + (v / 2))
    right(90)
    fd((h / 2) + m)

def draw_o(v, h, m, d, t):
    fd(h / 2)
    drawThickenedCircle(h / 2, 360, t)
    fd((h / 2) + m)

def draw_t(v, h, m, d, t):
    fd(h / 2)
    left(90)
    down()
    drawThickenedLine(v, t)
    back(v / 2)
    right(90)
    drawThickenedLine(h / 2, t)
    back(h)
    drawThickenedLine(h / 2, t)
    left(90)
    back(v / 2)
    right(90)
    fd((h / 2) + m)

def draw_w(v, h, m, d, t):
    left(90)
    fd(v / 2)
    theta = degrees(atan((h / 3) / (v / 2)))
    right(180 - theta)
    leg1 = (v / 2) / cos(radians(theta))
    leg2 = (v / 4) / cos(radians(theta))
    drawThickenedLine(leg1, t)
    right(theta)
    left(180 - theta)
    drawThickenedLine(leg2, t)
    right(180 - 2 * theta)
    drawThickenedLine(leg2, t)
    left(180 - 2 * theta)
    drawThickenedLine(leg1, t)
    left(theta)
    back(v / 2)
    right(90)
    fd(m)

def draw_C(v, h, m, d, t):
    fd(h)
    left(90)
    fd(v - (h / 2))
    drawThickenedArc((h / 2), 180, t)
    drawThickenedLine(v - h, t)
    drawThickenedArc((h / 2), 180, t)
    back(h / 2)
    right(90)
    fd(m)

def draw_k(v, h, m, d, t):
    theta = degrees(atan((v / 2) / h))
    left(90)
    drawThickenedLine(v, t)
    back(v / 2)
    right(30)
    drawThickenedLine(v / 2, t)
    back(v / 2)
    left(30)
    right(180)
    left(90 - theta)
    diag = h / cos(radians(theta))
    drawThickenedLine(diag, t)
    back(diag)
    right(90 - theta)
    fd(v / 2)
    left(90)
    fd(h + m)

def draw_n(v, h, m, d, t):
    left(90)
    drawThickenedLine(v / 2, t)
    back(v / 4)
    right(90)
    fd(h)
    left(90)
    drawThickenedCircle((h / 2), 180, t)
    right(180)
    drawThickenedLine(v / 4, t)
    left(90)
    fd(m)

def draw_r(v, h, m, d, t):
    left(90)
    drawThickenedLine(v / 2, t)
    back(v / 4)
    right(90)
    fd(h)
    left(90)
    drawThickenedCircle((h / 2), 180, t)
    right(180)
    fd(v / 4)
    left(90)
    fd(m)

def draw_F(v, h, m, d, t):
    left(90)
    drawThickenedLine(v, t)
    right(90)
    drawThickenedLine(h, t)
    back(h)
    left(90)
    back(v / 2)
    right(90)
    drawThickenedLine(h / 2, t)
    back(h / 2)
    left(90)
    back(v / 2)
    right(90)
    fd(h + m)
