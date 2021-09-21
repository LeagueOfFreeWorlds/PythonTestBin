'''
Created on Sep 9, 2021

@author: nathan-host
'''
import turtle
turtle.bgcolor("black")
turtle.color("white")
drawing_area = turtle.Screen()
drawing_area.setup(width=650, height=650)
# Begin Turtle drawings:
turtle.pensize(5)
turtle.penup()
turtle.color("gray")
turtle.begin_fill()
turtle.goto(0, -100)
turtle.pendown()
turtle.begin_fill()
turtle.circle(200)
turtle.penup()
turtle.end_fill()
turtle.color("white")
turtle.goto(-60, 125)
turtle.pendown()
turtle.begin_fill()
turtle.circle(25)
turtle.penup()
turtle.goto(60, 125)
turtle.pendown()
turtle.circle(25)
turtle.penup()
turtle.end_fill()
turtle.goto(-60, 20)
turtle.color("red")
turtle.pendown()
turtle.pensize(9)
#turtle.cum()
# Semi-circle for mouth.
turtle.setheading(315)
turtle.circle(90, 90)
turtle.done()