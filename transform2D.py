import turtle
import math

t = turtle.Turtle()

#draw_poly functie
def draw_poly(x, y, factor=6):
    t.setpos((x[0], y[0]))
    x, y = scale(x, y, factor)
    
    for i, j in zip(x, y):
        t.setpos(i, j)

#translate functie 
def translate(x, y, dx, dy):
    translatedX, translatedY = [], []
    for i, j in zip(x, y):
        # t.pendown()
        translatedX.append(i + dx)
        translatedY.append(j + dy)

    return translatedX, translatedY
  
#rotate functie
def rotate(x, y, theta):
    theta = math.radians(theta)
    rotatedX, rotatedY = [], []

    for i, j in zip(x, y):
        rotatedX.append(i * math.cos(theta) - j * math.sin(theta))
        rotatedY.append(j * math.cos(theta) + i * math.sin(theta))

    return rotatedX, rotatedY

#scale functie
def scale(x, y, alpha):
    scaledX, scaledY = [], []

    for i, j in zip(x, y):
        scaledX.append(i * alpha)
        scaledY.append(j * alpha)

    return scaledX, scaledY

#cordinaten
x = [0, 10, 10, 0, 0]
y = [0, 0, 20, 10, 0]

#Settings turtle
t.setpos(0, 0)
t.pen(pencolor="green", pensize=3)
draw_poly(x, y)


# TESTCODE
# Hieronder staat de code die je kunt gebruiken om je code te testen. Haal elke keer wanneer
# je klaar bent de betreffende code uit het commentaar om te checken of het resultaat 
# overeenkomst met wat je verwacht. Maak zelf ook andere testen om zeker te weten dat je
# code doet wat het moet doen.


"TEST VOOR `draw_poly`"
# t.setpos(0, 0)
# t.pen(pencolor="green", pensize=3)
# draw_poly(x, y)

"TEST VOOR `scale`"
t.pen(pencolor="green", pensize=3)
draw_poly(x, y)

t.pen(pencolor="red", pensize=3)
x, y = scale(x, y, 2, 2)
draw_poly(x, y)

"TEST VOOR `translate`" 
# t.pen(pencolor="red", pensize=3)
# x, y = translate(x, y, 20, 20)
# draw_poly(x, y)

"TEST VOOR `rotate`"
# t.pen(pencolor="red", pensize=3)
# x, y = rotate(x, y, 45)
# draw_poly(x, y)

# t.pen(pencolor="purple", pensize=3)
# x, y = rotate(x, y, 45)
# draw_poly(x, y)

# t.pen(pencolor="red", pensize=3)
# x, y = scale(x, y, 2)
# draw_poly(t, x, y)

## Deze regel is om ervoor te zorgen dat het scherm blijft staan
# wanneer de turtle klaar is met tekenen.
turtle.mainloop()
