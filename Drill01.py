def move_forward():
    turtle.forward(50)
    turtle.stamp()


def move_backward():
    turtle.backward(50)
    turtle.stamp()


def turn_left():
    turtle.left(90)


def turn_right():
    turtle.right(90)


def restart():
    turtle.reset()


import turtle

turtle.shape("turtle")
turtle.stamp()
turtle.onkey(move_forward, 'w')
turtle.onkey(move_backward, 's')
turtle.onkey(turn_left, 'a')
turtle.onkey(turn_right, 'd')
turtle.onkey(restart, 'Escape')
turtle.listen()
turtle.exitonclick()




