'''
testing
'''
import turtle
for x in range(-175, 176):
    turtle.goto(x, 50 * math.sin((x /100) * 2 * math.pi))
