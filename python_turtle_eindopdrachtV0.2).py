from hashlib import new
from math import sqrt
from turtle import *
import turtle
turtle = turtle.Turtle()
size = 100
colormap = ['blue','red','green','white','yellow', 'violet','orange']
def get_height():
    return 1/2 * size * sqrt(3)
def drawTriangle(points, color, turtle):
    turtle.fillcolor(color)
    turtle.up()
    turtle.goto(points[0][0],points[0][1])
    turtle.down()
    turtle.begin_fill()
    turtle.goto(points[1][0],points[1][1])
    turtle.goto(points[2][0],points[2][1])
    turtle.goto(points[0][0],points[0][1])
    turtle.end_fill()
def sierpinski(left_under_point, n, turtle):
    print (left_under_point)
    points = [
        left_under_point,
        [left_under_point[0]+size, left_under_point[1]],
        [left_under_point[0]/2, left_under_point[1]+get_height()]
    ]
    drawTriangle(points, colormap[n], turtle)
    if n == 0 :
        begin_fill()
        forward (points)
        left (120)
        forward (points)
        left (120)
        forward (points)
        left (120)
        end_fill()
    else :
        new_left_under_point = [
            left_under_point[0] - (size/4),
            get_height() / 2
        ]
        #new_x = (points[0]/4)-100
        #new_y = 25*10
        sierpinski (new_left_under_point, n-1, turtle)
        #forward (points/2)
        #sierpinski (points/2, n-1)
        #left (120)
        #forward (points/2)
        #right (120)
        #sierpinski (points/2, n-1)
        #right (120)
        #forward (points/2)
        #left (120)
def main():
    myWin = turtle.Screen()
    speed (10)
    setup(700, 700)
    title ("Sierpinski Driehoek")
    cordinates = [-100,-50]
    rang = 3
    #rang = int(numinput("Sierpinski Driekhoek", "Welke grootte (N)?", rang, minval=0, maxval=5))
    sierpinski(cordinates, rang, turtle)
    myWin.exitonclick()
    turtle.mainloop()
main()