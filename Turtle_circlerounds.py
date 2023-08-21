import turtle
t=turtle.Turtle()
win=turtle.Screen()
colors=['red', 'yellow', 'green','purple', 'blue', 'orange', 'white']
turtle.speed(0.01)
turtle.bgcolor("black")

for i in range(100):
	t.pencolor(colors[i%8])
	t.circle(2*i)
	t.circle(-2*i)
	t.left(i)
t.exitonclick()

