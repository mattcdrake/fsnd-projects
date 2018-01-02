import turtle

def draw_square(some_turtle):
    for i in range(0, 4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_cool_thing(some_turtle):
    for i in range(0, 36):
        draw_square(some_turtle)
        some_turtle.right(10)

def draw_turtles():
    window = turtle.Screen()
    window.bgcolor("red")
   
    brad = turtle.Turtle()
    draw_cool_thing(brad) 
    
    angie = turtle.Turtle()
    angie.circle(200)

    window.exitonclick()

draw_turtles()
