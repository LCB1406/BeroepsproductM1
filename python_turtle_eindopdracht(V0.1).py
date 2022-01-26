from turtle import *
import turtle

turtle = turtle.Turtle()

def drawTriangle(points,color,turtle):
    turtle.fillcolor(color)
    turtle.up()
    turtle.goto(points[0][0],points[0][1])
    turtle.down()
    turtle.begin_fill()
    turtle.goto(points[1][0],points[1][1])
    turtle.goto(points[2][0],points[2][1])
    turtle.goto(points[0][0],points[0][1])
    turtle.end_fill()

def sierpinski(points, n, turtle):
    colormap = ['blue','red','green','white','yellow', 'violet','orange']
    drawTriangle(points, colormap[n], turtle)

    if n > 0 :
        begin_fill()
        forward (points)
        left (120)
        forward (points)
        left (120)
        forward (points)
        left (120)
        end_fill()
        
    else :
        sierpinski (points/2, n-1)
        forward (points/2)
        sierpinski (points/2, n-1)
        left (120)
        forward (points/2)
        right (120)
        sierpinski (points/2, n-1)
        right (120)
        forward (points/2)
        left (120)

def main():
    speed (10)
    setup(700, 700)
    title ("Sierpinski Driehoek")
    cordinates = [[-100,-50], [0,100], [100,-50]]
    rang = 0
    rang = int(numinput("Sierpinski Driekhoek", "Welke groote (N)?", rang, minval=0, maxval=5))
    sierpinski(cordinates, rang, turtle)
    turtle.mainloop()

main()