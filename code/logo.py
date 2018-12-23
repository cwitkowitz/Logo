"""
Frank Cwitkowitz

Created: Unknown - Sometime during late 2018
Revised: 12/22/2018

Functions to draw my logo with letters.
"""

from turtle import *
from math import *

"""
Outer function that will handle
each piece of the project altogether.
"""
def draw_Logo(height, windowXSize):
#    init(windowXSize)

    # These should begin with the
    # turtle up, centered and facing up.
    ### Be weary, there are a lot of things to
    ### change in order to re-scale these outlines
    firstQuadrant(height)
    thirdQuadrant(height)
    secondQuadrant(height)
    fourthQuadrant(height)

#    deInit()


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
"""
def drawThickenedCircle(radius, extent, thickness):
    pensize(thickness)
    down()
    circle(radius, extent)
    up()
    pensize(1)


"""
Function that sets up the project.
"""
def init(windowXSize):
    setup(windowXSize, (windowXSize * 1.5), None, None)
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


##########################################################################################
################################  QUADRANT OUTLINE START  ################################
##########################################################################################
###  BE VERY CAREFUL WHEN MODIFYING THESE; THEIR SCALING IS INGRANED IN THE FUNCTIONS  ###
##########################################################################################


"""
Function that draws the top-right section
using the given hypotenuse length.
"""
def firstQuadrant(height):
    drawThickenedLine(height, 3)
    right(180 - 19)
    drawThickenedLine((height / cos(radians(19))), 3)
    back(height / cos(radians(19)))
    left(180 - 19)
    back(height * .05)
    right(180 - 19)
    right(5)
    drawThickenedLine(((height - (height * .05)) / cos(radians(14))), 2)
    back((height - (height * .05)) / cos(radians(14)))
    right(14)
    forward(height - (height * .05))
    left(180)

    firstQuadrantFill(height)


"""
Function that draws the bottom-right section
using the given hypotenuse length.
"""
def thirdQuadrant(height):

    thirdQuadrantFill(height)


"""
Function that draws the top-left section
using the given hypotenuse length.
"""
def secondQuadrant(height):
    drawThickenedLine(height, 3)
    left(180 - 20)

    # First piece outer
    drawThickenedLine((.67 * (height / cos(radians(20)))), 3)

    # Start first line slant
    left(180 - (90 - 20) - degrees(atan((height - (sin(radians(70)) * (.67 * (height / cos(radians(20)))))) /
                                        (cos(radians(70)) * (.67 * (height / cos(radians(20))))))))

    drawThickenedLine((.28 * (cos(radians(70)) * (.67 * (height / cos(radians(20))))) /
                       cos(radians(degrees(atan((height - (sin(radians(70)) * (.67 * (height / cos(radians(20)))))) /
                                                (cos(radians(70)) * (.67 * (height / cos(radians(20)))))))))), 2)

    fd(.15 * (cos(radians(70)) * (.67 * (height / cos(radians(20))))) /
       cos(radians(degrees(atan((height - (sin(radians(70)) * (.67 * (height / cos(radians(20)))))) /
                                (cos(radians(70)) * (.67 * (height / cos(radians(20))))))))))

    drawThickenedLine((.32 * (cos(radians(70)) * (.67 * (height / cos(radians(20))))) /
                       cos(radians(degrees(atan((height - (sin(radians(70)) * (.67 * (height / cos(radians(20)))))) /
                                                (cos(radians(70)) * (.67 * (height / cos(radians(20)))))))))), 2)

    back(.75 * (cos(radians(70)) * (.67 * (height / cos(radians(20))))) /
         cos(radians(degrees(atan((height - (sin(radians(70)) * (.67 * (height / cos(radians(20)))))) /
                                  (cos(radians(70)) * (.67 * (height / cos(radians(20))))))))))

    right(180 - (90 - 20) - degrees(atan((height - (sin(radians(70)) * (.67 * (height / cos(radians(20)))))) /
                                         (cos(radians(70)) * (.67 * (height / cos(radians(20))))))))
    # End first line slant

    fd((.1 * (height / cos(radians(20)))))

    # Start arc
    left(180 - (90 - 20) - degrees(atan((height - (sin(radians(70)) * (.77 * (height / cos(radians(20)))))) /
                                        (cos(radians(70)) * (.77 * (height / cos(radians(20))))))))

    fd((cos(radians(70)) * (.77 * (height / cos(radians(20))))) /
       cos(radians(degrees(atan((height - (sin(radians(70)) * (.77 * (height / cos(radians(20)))))) /
                                (cos(radians(70)) * (.77 * (height / cos(radians(20))))))))))

    right(180)

    fd(.86 * (cos(radians(70)) * (.77 * (height / cos(radians(20))))) /
       cos(radians(degrees(atan((height - (sin(radians(70)) * (.77 * (height / cos(radians(20)))))) /
                                (cos(radians(70)) * (.77 * (height / cos(radians(20))))))))))

    left(90)

    drawThickenedCircle(.86 * (cos(radians(70)) * (.77 * (height / cos(radians(20))))) /
                        cos(radians(degrees(atan((height - (sin(radians(70)) * (.77 * (height / cos(radians(20)))))) /
                                                 (cos(radians(70)) * (.77 * (height / cos(radians(20))))))))), 17, 2)

    circle(.86 * (cos(radians(70)) * (.77 * (height / cos(radians(20))))) /
           cos(radians(degrees(atan((height - (sin(radians(70)) * (.77 * (height / cos(radians(20)))))) /
                                    (cos(radians(70)) * (.77 * (height / cos(radians(20))))))))), 328)

    drawThickenedCircle(.86 * (cos(radians(70)) * (.77 * (height / cos(radians(20))))) /
                        cos(radians(degrees(atan((height - (sin(radians(70)) * (.77 * (height / cos(radians(20)))))) /
                                                 (cos(radians(70)) * (.77 * (height / cos(radians(20))))))))), 15, 2)

    right(90)

    back(.86 * (cos(radians(70)) * (.77 * (height / cos(radians(20))))) /
         cos(radians(degrees(atan((height - (sin(radians(70)) * (.77 * (height / cos(radians(20)))))) /
                                  (cos(radians(70)) * (.77 * (height / cos(radians(20))))))))))

    left(180)

    back((cos(radians(70)) * (.77 * (height / cos(radians(20))))) /
         cos(radians(degrees(atan((height - (sin(radians(70)) * (.77 * (height / cos(radians(20)))))) /
                                  (cos(radians(70)) * (.77 * (height / cos(radians(20))))))))))

    right(180 - (90 - 20) - degrees(atan((height - (sin(radians(70)) * (.77 * (height / cos(radians(20)))))) /
                                         (cos(radians(70)) * (.77 * (height / cos(radians(20))))))))
    # End arc

    fd((.1 * (height / cos(radians(20)))))

    # Second piece outer

    # Start second line slant
    left(180 - (90 - 20) - degrees(atan((height - (sin(radians(70)) * (.87 * (height / cos(radians(20)))))) /
                                        (cos(radians(70)) * (.87 * (height / cos(radians(20))))))))

    drawThickenedLine((.38 * (cos(radians(70)) * (.87 * (height / cos(radians(20))))) /
                       cos(radians(degrees(atan((height - (sin(radians(70)) * (.87 * (height / cos(radians(20)))))) /
                                                (cos(radians(70)) * (.87 * (height / cos(radians(20)))))))))), 2)

    back(.38 * (cos(radians(70)) * (.87 * (height / cos(radians(20))))) /
         cos(radians(degrees(atan((height - (sin(radians(70)) * (.87 * (height / cos(radians(20)))))) /
                                  (cos(radians(70)) * (.87 * (height / cos(radians(20))))))))))

    right(180 - (90 - 20) - degrees(atan((height - (sin(radians(70)) * (.87 * (height / cos(radians(20)))))) /
                                         (cos(radians(70)) * (.87 * (height / cos(radians(20))))))))
    # End second line slant

    drawThickenedLine((.13 * (height / cos(radians(20)))), 3)
    back(height / cos(radians(20)))
    right(180 - 20)
    back(height * .05)
    left(180 - 20)
    left(6)

    # First piece inner
    drawThickenedLine((.8 * ((height - (height * .05)) / cos(radians(14)))), 2)
    left(90 + 14)
    drawThickenedLine((cos(radians(90 - 14)) * (.8 * ((height - (height * .05)) / cos(radians(14))))), 2)
    back((cos(radians(90 - 14)) * (.8 * ((height - (height * .05)) / cos(radians(14))))))
    right(90 + 14)

    fd((.11 * (height / cos(radians(14)))))

    # Second piece inner
    left(90 + 14)
    drawThickenedLine((cos(radians(90 - 14)) * (.91 * ((height - (height * .05)) / cos(radians(14))))), 2)
    back((cos(radians(90 - 14)) * (.91 * ((height - (height * .05)) / cos(radians(14))))))
    right(90 + 14)
    drawThickenedLine((.09 * ((height - (height * .05)) / cos(radians(14)))), 2)

    back((height - (height * .05)) / cos(radians(14)))
    left(14)
    forward(height - (height * .05))
    right(180)

    secondQuadrantFill(height)


"""
Function that draws the bottom-left section
using the given hypotenuse length.
"""
def fourthQuadrant(height):
    down()
    right(180)

    drawThickenedLine(height, 3)
    left(180 - 19)
    drawThickenedLine((height / cos(radians(19))), 3)
    back(height / cos(radians(19)))
    right(180 - 19)
    back(height * .05)
    left(180 - 19)
    left(5)
    drawThickenedLine(((height - (height * .05)) / cos(radians(14))), 2)
    back((height - (height * .05)) / cos(radians(14)))
    left(14)
    forward(height - (height * .05))
    down()
    right(180)

    drawThickenedLine(height, 3)
    right(180 - 20)

    # First piece outer
    drawThickenedLine((.55 * (height / cos(radians(20)))), 3)

    # Start first line slant
    right(180 - (90 - 20) - degrees(atan((height - (sin(radians(70)) * (.55 * (height / cos(radians(20)))))) /
                                         (cos(radians(70)) * (.55 * (height / cos(radians(20))))))))

    drawThickenedLine((.25 * (cos(radians(70)) * (.55 * (height / cos(radians(20))))) /
                       cos(radians(degrees(atan((height - (sin(radians(70)) * (.55 * (height / cos(radians(20)))))) /
                                                (cos(radians(70)) * (.55 * (height / cos(radians(20)))))))))), 2)

    back(.25 * (cos(radians(70)) * (.55 * (height / cos(radians(20))))) /
         cos(radians(degrees(atan((height - (sin(radians(70)) * (.55 * (height / cos(radians(20)))))) /
                                  (cos(radians(70)) * (.55 * (height / cos(radians(20))))))))))

    left(180 - (90 - 20) - degrees(atan((height - (sin(radians(70)) * (.55 * (height / cos(radians(20)))))) /
                                        (cos(radians(70)) * (.55 * (height / cos(radians(20))))))))
    # End first line slant

    fd((.12 * (height / cos(radians(20)))))

    # Second piece outer

    # Start second line slant
    right(180 - (90 - 20) - degrees(atan((height - (sin(radians(70)) * (.67 * (height / cos(radians(20)))))) /
                                         (cos(radians(70)) * (.67 * (height / cos(radians(20))))))))

    drawThickenedLine((.29 * (cos(radians(70)) * (.67 * (height / cos(radians(20))))) /
                       cos(radians(degrees(atan((height - (sin(radians(70)) * (.67 * (height / cos(radians(20)))))) /
                                                (cos(radians(70)) * (.67 * (height / cos(radians(20)))))))))), 2)

    back(.29 * (cos(radians(70)) * (.67 * (height / cos(radians(20))))) /
         cos(radians(degrees(atan((height - (sin(radians(70)) * (.67 * (height / cos(radians(20)))))) /
                                  (cos(radians(70)) * (.67 * (height / cos(radians(20))))))))))

    left(180 - (90 - 20) - degrees(atan((height - (sin(radians(70)) * (.67 * (height / cos(radians(20)))))) /
                                        (cos(radians(70)) * (.67 * (height / cos(radians(20))))))))
    # End second line slant

    drawThickenedLine((.33 * (height / cos(radians(20)))), 3)
    back(height / cos(radians(20)))

    left(180 - 20)
    back(height * .05)
    right(180 - 20)

    # Start edge
    right(1)
    fd(.53 * (height / cos(radians(20))))
    drawThickenedLine((.11 * (height / cos(radians(20)))), 2)
    back(.64 * (height / cos(radians(20))))
    right(5)
    # End edge

    # Inner piece
    drawThickenedLine(((height - (height * .05)) / cos(radians(14))), 2)

    back((height - (height * .05)) / cos(radians(14)))
    right(14)
    forward(height - (height * .05))
    left(180)

    fourthQuadrantFill(height)


##########################################################################################
#################################  QUADRANT OUTLINE END  #################################
##########################################################################################
#####  YOU HAVE MADE IT AND YOU SHOULD NOT NEED TO MODIFY THESE TO SCALE UP OR DOWN  #####
##########################################################################################


##########################################################################################
#################################  QUADRANT FILLS START  #################################
##########################################################################################
###  BE VERY CAREFUL WHEN MODIFYING THESE; THEIR SCALING IS INGRANED IN THE FUNCTIONS  ###
##########################################################################################


"""
Function that fills in the top-right outline
using the given scale(hypotenuse) length.
"""
def firstQuadrantFill(scale):
    # Start outer slant
    fd(scale)
    right(180 - 16)
    fd(.75 * (scale / cos(radians(16))))
    drawThickenedLine((.15 * (scale / cos(radians(16)))), 1)
    back(.9 * (scale / cos(radians(16))))
    left(180 - 16)
    back(scale)
    # End outer slant

    # Start inner slant
    fd(scale - (scale * .05))
    right(180 - 8)
    fd(.57 * ((scale - (scale * .05)) / cos(radians(8))))
    drawThickenedLine((.26 * ((scale - (scale * .05)) / cos(radians(8)))), 1)
    back(.83 * ((scale - (scale * .05)) / cos(radians(8))))
    left(180 - 8)
    back(scale - (scale * .05))
    # End inner slant

    # Start middle slant
    fd(.2 * (scale - (scale * .05)))
    right(180)
    left(degrees(atan((sin(radians(180 - 8)) * ((scale - (scale * .05)) / cos(radians(8)))) /
                      (.2 * (scale - (scale * .05))))))
    drawThickenedLine(((.2 * (scale - (scale * .05))) /
                       cos(radians(degrees(atan((sin(radians(180 - 8)) * ((scale - (scale * .05)) /
                                                                          cos(radians(8)))) /
                                                (.2 * (scale - (scale * .05)))))))), 1)
    back((.2 * (scale - (scale * .05))) /
         cos(radians(degrees(atan((sin(radians(180 - 8)) * ((scale - (scale * .05)) /
                                                            cos(radians(8)))) / (.2 * (scale - (scale * .05))))))))
    right(degrees(atan((sin(radians(180 - 8)) * ((scale - (scale * .05)) / cos(radians(8)))) /
                       (.2 * (scale - (scale * .05))))))
    left(180)
    back(.2 * (scale - (scale * .05)))
    # End middle slant


"""
Function that fills in the bottom-right outline
using the given scale(hypotenuse) length.
"""
def thirdQuadrantFill(scale):
    right(180)

    # Start outer slant
    fd(scale)
    right(180 - 17)
    fd(.78 * (scale / cos(radians(17))))
    drawThickenedLine((.22 * (scale / cos(radians(17)))), 1)
    back(scale / cos(radians(17)))
    left(180 - 17)
    back(scale)
    # End outer slant

    # Start inner slant
    fd(scale - (scale * .05))
    right(180 - 8)
    fd(.56 * ((scale - (scale * .05)) / cos(radians(8))))
    drawThickenedLine((.44 * ((scale - (scale * .05)) / cos(radians(8)))), 1)
    back((scale - (scale * .05)) / cos(radians(8)))
    left(180 - 8)
    back(scale - (scale * .05))
    # End inner slant

    right(180)

    # Start horizontal line
    left(90)
    fd(.75 * (tan(radians(20)) * scale))
    drawThickenedLine(.09 * (tan(radians(20)) * scale), 1)
    back(.84 * (tan(radians(20)) * scale))
    right(90)
    # End horizontal line


"""
Function that fills in the top-left outline
using the given scale(hypotenuse) length.
"""
def secondQuadrantFill(scale):
    # Start two lines
    fd(.33 * scale)
    left(90)
    drawThickenedLine((.07 * scale), 1)
    back(.07 * scale)
    right(90)
    fd(.04 * scale)
    left(90)
    drawThickenedLine((.1 * scale), 1)
    back(.1 * scale)
    right(90)
    back(.37 * scale)
    # End two lines

    # Start circle line
    fd(scale)
    left(180 - 20)
    fd(.78 * (scale / cos(radians(20))))
    left(180 - (90 - 20) - degrees(atan((scale - (sin(radians(70)) * (.77 * (scale / cos(radians(20)))))) /
                                        (cos(radians(70)) * (.77 * (scale / cos(radians(20))))))))

    fd(.29 * (cos(radians(70)) * (.77 * (scale / cos(radians(20))))) /
       cos(radians(degrees(atan((scale - (sin(radians(70)) * (.77 * (scale / cos(radians(20)))))) /
                                (cos(radians(70)) * (.77 * (scale / cos(radians(20))))))))))

    drawThickenedLine((.17 * (cos(radians(70)) * (.77 * (scale / cos(radians(20))))) /
                       cos(radians(degrees(atan((scale - (sin(radians(70)) * (.77 * (scale / cos(radians(20)))))) /
                                                (cos(radians(70)) * (.77 * (scale / cos(radians(20)))))))))), 1)

    back(.46 * (cos(radians(70)) * (.77 * (scale / cos(radians(20))))) /
         cos(radians(degrees(atan((scale - (sin(radians(70)) * (.77 * (scale / cos(radians(20)))))) /
                                  (cos(radians(70)) * (.77 * (scale / cos(radians(20))))))))))

    right(180 - (90 - 20) - degrees(atan((scale - (sin(radians(70)) * (.77 * (scale / cos(radians(20)))))) /
                                         (cos(radians(70)) * (.77 * (scale / cos(radians(20))))))))

    back(.78 * (scale / cos(radians(20))))
    right(180 - 20)
    back(scale)
    # End circle line

    # Start outer slant
    fd(scale)
    left(180 - 17)
    fd(.93 * (scale / cos(radians(17))))
    drawThickenedLine((.07 * (scale / cos(radians(17)))), 1)
    back(scale / cos(radians(17)))
    right(180 - 17)
    back(scale)
    # End outer slant

    # Start inner slant
    fd(scale - (scale * .05))
    left(180 - 8)
    fd(.91 * ((scale - (scale * .05)) / cos(radians(8))))
    drawThickenedLine((.09 * ((scale - (scale * .05)) / cos(radians(8)))), 1)
    back((scale - (scale * .05)) / cos(radians(8)))
    right(180 - 8)
    back(scale - (scale * .05))
    # End inner slant


"""
Function that fills in the bottom-left outline
using the given scale(hypotenuse) length.
"""
def fourthQuadrantFill(scale):
    # Start outer slant
    fd(scale)
    left(180 - 16)
    fd(.75 * (scale / cos(radians(16))))
    drawThickenedLine((.15 * (scale / cos(radians(16)))), 1)
    back(.9 * (scale / cos(radians(16))))
    right(180 - 16)
    back(scale)
    # End outer slant

    # Start inner slant
    fd(scale - (scale * .05))
    left(180 - 8)
    fd(.56 * ((scale - (scale * .05)) / cos(radians(8))))
    drawThickenedLine((.24 * ((scale - (scale * .05)) / cos(radians(8)))), 1)
    fd(.06 * ((scale - (scale * .05)) / cos(radians(8))))

    """
    Middle slant
    """
    left(8)
    left(degrees(atan((sin(radians(180 - 8)) * ((scale - (scale * .05)) / cos(radians(8)))) /
                      (.2 * (scale - (scale * .05))))))
    fd(.04 * ((.2 * (scale - (scale * .05))) /
                       cos(radians(degrees(atan((sin(radians(180 - 8)) * ((scale - (scale * .05)) /
                                                                          cos(radians(8)))) /
                                                (.2 * (scale - (scale * .05)))))))))
    drawThickenedLine(.4 * ((.2 * (scale - (scale * .05))) /
                       cos(radians(degrees(atan((sin(radians(180 - 8)) * ((scale - (scale * .05)) /
                                                                          cos(radians(8)))) /
                                                (.2 * (scale - (scale * .05)))))))), 1)
    back(.4 * (.2 * (scale - (scale * .05))) /
         cos(radians(degrees(atan((sin(radians(180 - 8)) * ((scale - (scale * .05)) /
                                                            cos(radians(8)))) / (.2 * (scale - (scale * .05))))))))
    back(.04 * ((.2 * (scale - (scale * .05))) /
                       cos(radians(degrees(atan((sin(radians(180 - 8)) * ((scale - (scale * .05)) /
                                                                          cos(radians(8)))) /
                                                (.2 * (scale - (scale * .05)))))))))
    right(degrees(atan((sin(radians(180 - 8)) * ((scale - (scale * .05)) / cos(radians(8)))) /
                       (.2 * (scale - (scale * .05))))))
    right(8)
    """
    """

    drawThickenedLine((.15 * ((scale - (scale * .05)) / cos(radians(8)))), 1)
    back(1.01 * (scale - (scale * .05)) / cos(radians(8)))
    right(180 - 8)
    back(scale - (scale * .05))
    # End inner slant

    right(180)


##########################################################################################
##################################  QUADRANT FILLS END  ##################################
##########################################################################################
###  BE VERY CAREFUL WHEN MODIFYING THESE; THEIR SCALING IS INGRANED IN THE FUNCTIONS  ###
##########################################################################################
