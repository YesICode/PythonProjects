import turtle


def sierpinski(t, order, size, colorChangeDepth):

        if order == 0:
                for angle in [ 120, 120,120]:
                        t.forward(size)
                        t.left(angle)
        else:
                if colorChangeDepth == 0:
                        t.color("red")
                sierpinski(t, order - 1, size/2, colorChangeDepth - 1)
                t.penup()
                t.forward(size/2)
                t.pendown()

                if colorChangeDepth == 0:
                        t.color("blue")
                sierpinski(t, order - 1, size/2, colorChangeDepth - 1)
                t.penup()
                t.left(120)
                t.forward(size/2)
                t.pendown()

                if colorChangeDepth == 0:
                        t.color("magenta")
                sierpinski(t, order - 1, size/2, colorChangeDepth - 1)
                t.penup()
                t.left(-120)
                t.forward(size/2)
                t.left(120)
                t.pendown()

rec = int(input("Please enter the recursion depth: "))

colorChangeDepth = int(input("Please enter the color change depth: "))

if (colorChangeDepth < 0) or (rec < colorChangeDepth):
        colorChangeDepth = -1

wn = turtle.Screen()
wn.screensize(500,500)
wn.bgcolor("lightgreen")
wn.title("Sierpinski triangle")

tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(3)

tess.penup()
tess.forward(-200)
tess.right(90)
tess.forward(200)
tess.left(90)
tess.pendown()

sierpinski(tess, rec, 400, colorChangeDepth)

wn.mainloop()

