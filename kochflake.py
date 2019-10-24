import turtle


def koch(t, order, size):
        if order == 0:
                t.forward(size)
        else:
                for angle in [60,-120, 60, 0]:
                        koch(t, order - 1, size / 3)
                        t.left(angle)

def koch_flake(t, order, size):
        for angle in [-120, -120, 0]:
                koch(t, order, size)
                t.left(angle)

wn = turtle.Screen()
wn.screensize(500,500)
wn.bgcolor("lightgreen")
wn.title("Koch Snowflake")
