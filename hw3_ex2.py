import turtle

def koch_snowflake(turtle, iterations, length):
    if iterations == 0:
        turtle.forward(length)
    else:
        length /= 3.0
        koch_snowflake(turtle, iterations - 1, length)
        turtle.left(60)
        koch_snowflake(turtle, iterations - 1, length)
        turtle.right(120)
        koch_snowflake(turtle, iterations - 1, length)
        turtle.left(60)
        koch_snowflake(turtle, iterations - 1, length)

def draw_snowflake():
    recursion_depth = int(input("Глибина рекурсії: "))
    window = turtle.Screen()
    window.bgcolor("white")
    koch_turtle = turtle.Turtle()
    koch_turtle.speed(0)  
    koch_turtle.penup()
    koch_turtle.goto(-150, 90)
    koch_turtle.pendown()

    for i in range(3):
        koch_snowflake(koch_turtle, recursion_depth, 300)
        koch_turtle.right(120)
    window.mainloop()

draw_snowflake()
