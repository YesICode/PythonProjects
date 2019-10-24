import turtle


def cesaro_line(t, order, size, a):
        if order == 0:
                t.forward(size)
        else:
                for angle in [90-a, -2*(90-a), 90-a, 0]:
                        cesaro_line(t, order - 1, size / 3, a)
                        t.left(angle)

def cesaro_square(t, order, size, a):
        for angle in [90, 90, 90, 0]:
                cesaro_line(t, order, size, a)
                t.left(angle)

angle = int(input("Please enter the angle: "))
rec = int(input("Please enter the recursion depth: "))

wn = turtle.Screen()
wn.screensize(500,500)

