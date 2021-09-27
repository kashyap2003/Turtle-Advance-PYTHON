import turtle

kashyap = turtle.Turtle()
turtle.Screen().bgcolor("black")
kashyap.color("Red")
kashyap.speed(10)

for i in range(100):
    kashyap.circle(i*2)
    kashyap._rotate(5)