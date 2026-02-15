import turtle
import math

def triangle(t, leg, angle):
    chord = 2 * leg * math.sin(math.radians(angle) / 2)
    base_angle = (180 - angle) / 2

    t.forward(leg)
    t.left(180 - base_angle)
    t.forward(chord)
    t.left(180 - base_angle)
    t.forward(leg)
    t.left(180)

def draw_pie(segments, radius):
    t = turtle.Turtle()
    t.speed(0)
    angle = 360 / segments
    for i in range(segments):
        triangle(t, radius, angle)

t = turtle.Turtle()

screen = turtle.Screen()
screen.bgcolor("white")

draw_pie(6, 100)

turtle.exitonclick()






