import turtle
import math

def arc(t, radius, angle):
    arc_length = 2 * math.pi * radius * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

def move(t, length):
            t.pu()
            t.fd(length)
            t.pd()

def petal(t, radius, angle):
    for i in range(2):
        arc(t, radius, angle)
        t.lt(180 - angle)

def flower(t, n, radius, angle):
    for i in range(n):
        petal(t, radius, angle)
        t.lt(360.0 / n)

t = turtle.Turtle()
t.speed(0)

flower(t, 7, 60.0, 60.0)

turtle.exitonclick()
