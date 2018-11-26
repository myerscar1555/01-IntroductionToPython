"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Carter Myers.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow
########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
size = 100
wohlfie = rg.SimpleTurtle()
wohlfie.pen = rg.Pen('Hot Pink', 5)
wohlfie.speed = 7

michael = rg.SimpleTurtle()
michael.pen = rg.Pen('Green',5)
michael.speed = 2

for k in range(11):
    wohlfie.draw_circle(size)

    wohlfie.pen_up()
    wohlfie.right(90)
    wohlfie.forward(10)

    wohlfie.pen_down()
    size = size - 5

    michael.go_to(rg.Point(0,200))
    michael.pen_up()
    michael.right(45)
    michael.forward(2**k)
    michael.pen_down()

window.tracer(100)

