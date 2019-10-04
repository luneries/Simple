#Getting a Random Color:
def RandomColor():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    colorToReturn = (red, green, blue)
    return colorToReturn
    
#Drawing a Square:
def DrawASquare(SquareSize):
    for i in range(4):
        t.forward(SquareSize)
        t.left(90)
    return

#Drawing Square with Color
def DrawASquareWithColor(SquareSize,color):
    t.fillcolor(color) 
    t.begin_fill()
    DrawASquare(SquareSize)
    t.end_fill()
    return

#Drawing a Triangle:
def DrawATriangle(TriangleSize):
    for i in range(3):
        t.forward(TriangleSize)
        t.left(120)
        t.forward(TriangleSize)
    return

#Drawing a Triangle With Color
def DrawATriangleWithColor(TriangleSize,color):
    t.fillcolor(color)
    t.begin_fill()
    DrawATriangle(TriangleSize)
    t.end_fill()

#Drawing a Hexagon
def DrawAHexagon(HexagonSize):
    for i in range(6):
        t.forward(HexagonSize)
        t.left(60)
    return

#Drawing a Hexagon with Color
def DrawAHexagonWithColor(HexagonSize,color):
    t.fillcolor(color)
    t.begin_fill()
    DrawAHexagon(HexagonSize)
    t.end_fill()
    return

#TOPLEVEL

import random
import turtle as t

###
t.colormode(255)
###

#Hiding Turtle Pointer Icon in Turtle
t.hideturtle()

#Faster Speed of Pen in Turtle
t.speed(100)

#Thicker Width of Pen in Turtle
t.width(3)

#Calling DrawASquare to create object in the middle
for i in range(18):
    t.pencolor("Red")
    DrawASquareWithColor(100,"Pink")
    t.left(20)

#Calling DrawATriangleWithColor to create object on the left side
t.penup()
t.backward(200)
t.right(100)
t.pendown()
for i in range(9):
    col = RandomColor()
    t.pencolor("Black")
    DrawATriangleWithColor(80,col)
    t.right(40)
    DrawATriangleWithColor(80,col)

#Calling DrawAHexagon to draw hexagons on left side
t.penup()
t.left(20)
t.pendown()
t.pencolor("Grey")
for i in range(3):
    DrawAHexagonWithColor(20,"Yellow")
    t.left(120)

#Calling DrawATriangleWithColor to create object on the right side
t.penup()
t.left(80)
t.forward(400)
t.pendown()
for i in range(9):
    col = RandomColor()
    t.pencolor("Black")
    DrawATriangleWithColor(80,col)
    t.right(40)
    DrawATriangleWithColor(80,col)

#Calling DrawAHexagon to draw hexagons on right side
t.penup()
t.left(20)
t.pendown()
t.pencolor("Grey")
for i in range(3):
    DrawAHexagonWithColor(20,"Yellow")
    t.left(120)

print("THE END!")

#End of Program



