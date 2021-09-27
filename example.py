import turtle

bob = turtle.Turtle()
turtle.Screen().bgcolor("black")
bob.color('yellow', 'red')
bob.speed(0)

bob.begin_fill()

for i in range(10):
    for i in range(2):
        bob.forward(100)
        bob.right(60)
        bob.forward(100)
        bob.right(120)
    bob.right(36)

bob.end_fill()

turtle.done()