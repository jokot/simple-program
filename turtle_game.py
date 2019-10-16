import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)

def square(lenght,angle):
    
    for i in range(4):
        my_turtle.forward(lenght)
        my_turtle.left(angle)
    

for i in range(7200):
    square(100,90)
    my_turtle.left(7)

