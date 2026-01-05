import turtle
import sys
import math


def pythagoras_tree(t, order, size):
    if order == 0:
        return
    # each scaled down by a linear factor of √2/2
    new_size = size*(math.sqrt(2)/2)
    # draw trunk
    t.forward(size)
    # draw left branch
    t.left(45)
    pythagoras_tree(t, order-1, new_size)
    # draw right branch
    t.right(90)
    pythagoras_tree(t, order-1, new_size)
    # return to the bottom of the trunk
    t.left(45)
    t.backward(size)


def draw_pythagoras_tree(order, size=600):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, -size / 2)
    t.pendown()

    t.left(90)
    pythagoras_tree(t, order, size/3)

    t.hideturtle()  # The arrow disappears here

    window.mainloop()


def parse_args() -> int:
    if len(sys.argv) < 2:
        return 3  # default order

    try:
        order = int(sys.argv[1])
    except ValueError:
        raise ValueError("First argument must be an integer")

    if order <= 0:
        raise ValueError("First argument must be more than zero")

    return order


def main():
    order = parse_args()
    draw_pythagoras_tree(order)


if __name__ == "__main__":
    main()
