import turtle

t = turtle.Turtle()

def parallelogram(t, length1, length2, angle):
    for _ in range(2):
        t.forward(length1)
        t.left(angle)
        t.forward(length2)
        t.left(180 - angle)

def rectangle(t, width, height):
    parallelogram(t, width, height, 90)

def rhombus(t, side_length, angle):
    parallelogram(t, side_length, side_length, angle)

# rectangle(t, 100, 50)
# rhombus(t, 70, 60)
parallelogram(t, 120, 60, 60)

turtle.Screen().exitonclick()



