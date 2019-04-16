import turtle

colours = ["blue", "red", "yellow", "green", "pink", "black", "light blue"]
t = turtle.Pen()
t.speed(10)
t.color("blue")

for x in range(250):
    t.width(x/50)
    t.color(colours[x%4])
    t.forward(x)
    t.left(91)

