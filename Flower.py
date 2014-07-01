import turtle

def draw_square(some_turtle):
    for i in range (1,5):
        some_turtle.forward(160)
        some_turtle.right(90)
def draw_triangle(some_turtle):
    for i in range (1,4):
        some_turtle.back(160)
        some_turtle.left(120)
def draw_line(some_turtle):
    some_turtle.forward(400)

def drawing():
    window = turtle.Screen()
    window.bgcolor("white")

    sharp = turtle.Turtle()
    sharp.shape("classic")
    sharp.color("green")
    sharp.speed(150)
    for i in range(1,73):
        draw_square(sharp)
        sharp.right(5)
    sharp.right(90)
    draw_line(sharp)
    
    #izzy = turtle.Turtle()
    #izzy.shape("triangle")
    #izzy.color("blue")
    #izzy.speed(5)
    #izzy.circle(90)

    #pointy = turtle.Turtle()
    #pointy.shape("turtle")
    #pointy.color("purple")
    #pointy.speed(3)
    #draw_triangle(pointy)
    sharp.hideturtle()
    window.exitonclick()

drawing()
