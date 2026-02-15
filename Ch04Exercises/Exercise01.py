import turtle

def rectangle(width, height):
    t = turtle.Turtle()
    t.pendown()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.penup()

rectangle(80, 40)

turtle.Screen().exitonclick()