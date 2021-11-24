import turtle
turtle.setup(1000, 1000)
turtle.speed(0)
list_1 = []
with open("picture.txt") as picture:
    for line in picture:
        try:
            x, y = line.split(",")
            list_1.append((int(x), int(y)))
        except ValueError:
            list_1.append((0, 0))
turtle.penup()
for i in list_1:
    if i == (0, 0):
        turtle.penup()
        continue
    turtle.setpos(i)
    turtle.pendown()
turtle.done()
