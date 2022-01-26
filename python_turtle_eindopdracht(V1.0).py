from math import sqrt
from turtle import *
import turtle

turtlez = turtle.Turtle()
size = 100
colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']

def get_height(size):
    return 1 / 2 * size * sqrt(3)

def drawTriangle(points, color, turtle):
    turtle.fillcolor(color)
    turtle.up()
    turtle.goto(points[0][0], points[0][1])
    turtle.down()
    turtle.begin_fill()
    turtle.goto(points[1][0], points[1][1])
    turtle.goto(points[2][0], points[2][1])
    turtle.goto(points[0][0], points[0][1])
    turtle.end_fill()

def sierpinski(left_under_point, size, n, turtle):
    print(left_under_point)
    points = [
        left_under_point,
        [left_under_point[0] + size, left_under_point[1]],
        [left_under_point[0] + (size / 2), left_under_point[1] + get_height(size)]
    ]

    drawTriangle(points, colormap[n], turtle)

    if n == 0:
        drawTriangle(points, colormap[n], turtle)

    else:
        #bottemleft
        new_size = size / 2
        sierpinski(left_under_point, new_size, n-1, turtle)

        #bottomright
        new_left_under_point = [
            left_under_point[0] + (new_size),
            left_under_point[1]
        ]
   
        sierpinski(new_left_under_point, new_size, n - 1, turtle)

        #top
        new_left_under_point = [
            left_under_point[0]+(new_size/2),
            left_under_point[1] + get_height(new_size)
        ]

        sierpinski(new_left_under_point, new_size, n-1, turtle)

def main():
    myWin = turtle.Screen()
    speed(1)
    setup(500, 500)
    title("Sierpinski Driehoek")
    cordinates = [-100, -50]
    rang = 3
    rang = int(numinput("Sierpinski Driekhoek", "Welke grootte (N)?", rang, minval=0, maxval=5))
    sierpinski(cordinates, size, rang, turtlez)
    myWin.exitonclick()
    turtlez.mainloop()

main()