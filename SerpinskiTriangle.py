import turtle
import random

# set up turtle
t = turtle.Pen()
t.speed(100)
t.penup()
t.width(1)
# t.hideturtle()

# triangle points
a = (0, 300)
b = (-300, -300)
c = (300, -300)
points = [a, b, c]

# draw triangle
for i in range(3):
    t.setposition(points[i][0], points[i][1])
    t.pendown()
    t.dot()
    t.penup()

# randomly place first position
t.setposition(random.randint(-300, 300), random.randint(-300, 300))

while 1 == 1:
    # randomly choose point of triangle
    point = points[random.randint(0, 2)]

    # calculate halfway point between point and current position
    t.setposition((t.position()[0] + point[0]) / 2, (t.position()[1] + point[1]) / 2)
    # make a dot
    t.pendown()
    t.dot()
    t.penup()
