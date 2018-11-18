# Sierpinski Triangle Program

import turtle
import math


def createTriangleShape(coords):
    
    turtle.penup()
    turtle.begin_poly()
    turtle.setposition(coords[0])
    turtle.setposition(coords[1])
    turtle.setposition(coords[2])
    turtle.setposition(coords[0])
    turtle.end_poly()

    tri_shape = turtle.get_poly()
    turtle.register_shape('my_triangle', tri_shape)


def triangleHeight(side):

    return math.sqrt(3) / 2 * side


def getLeftTrianglePosition(position, side):

    return (position[0] - side / 4, position[1] - triangleHeight(side) / 4)


def getRightTrianglePosition(position, side):

    return (position[0] + side / 4, position[1] - triangleHeight(side) / 4)


def getTopTrianglePosition(position, side):

    return (position[0], position[1] + triangleHeight(side) / 4)

        
def drawSierpinskiTriangle(t, len_side, levels):

    if levels == 0:

        # display triangle
        t.color('black')
        t.showturtle()
        t.stamp()

        return
    
    # resize triangle to half its size
    stretch_width, stretch_length, outline = t.turtlesize()
    t.turtlesize(0.5 * stretch_width, 0.5 * stretch_length, outline)

    # determine positions for each of the three embedded triangles
    left_triangle_position = getLeftTrianglePosition(t.position(), len_side)
    right_triangle_position = getRightTrianglePosition(t.position(), len_side)
    top_triangle_position = getTopTrianglePosition(t.position(), len_side)
    
    # recursively display left triangle
    t.setposition(left_triangle_position)
    drawSierpinskiTriangle(t, len_side / 2, levels - 1)
    t.turtlesize(0.5 * stretch_width, 0.5 * stretch_length, outline)
    
    # recursively display right triangle
    t.setposition(right_triangle_position)
    drawSierpinskiTriangle(t, len_side / 2, levels - 1)
    t.turtlesize(0.5 * stretch_width, 0.5 * stretch_length, outline)

    # recursively display top triangle
    t.setposition(top_triangle_position)
    drawSierpinskiTriangle(t, len_side / 2, levels - 1)
    t.turtlesize(0.5 * stretch_width, 0.5 * stretch_length, outline)
    

# ---- main

# set window size
turtle.setup(800, 600)

# get turtle
the_turtle = turtle.getturtle()

# init turtle
the_turtle.penup()
the_turtle.hideturtle()

# set the number of levels
num_levels = 3

# create triangle shape
coords = ((-240, 0), (240, 0), (0, 416))

createTriangleShape(coords)
len_side = 480

# create first triangle
the_turtle.shape('my_triangle')
the_turtle.setposition(0,-50)
the_turtle.setheading(90)

# call recursive function
drawSierpinskiTriangle(the_turtle, len_side, num_levels)
the_turtle.hideturtle()

# terminate program when close window
turtle.exitonclick()

