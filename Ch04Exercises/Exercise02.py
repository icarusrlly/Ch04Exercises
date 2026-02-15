import turtle

def rhombus(side_length, interior_angle):
    other_angle = 180 - interior_angle
    for _ in range(2):
        turtle.forward(side_length)
        turtle.left(interior_angle)
        turtle.forward(side_length)
        turtle.left(other_angle)

rhombus(50, 60)

turtle.Screen().exitonclick()
