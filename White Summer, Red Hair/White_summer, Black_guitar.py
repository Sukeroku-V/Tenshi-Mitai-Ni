import turtle

White_summer = turtle.Turtle()
turtle.bgcolor("black")
White_summer.speed(0)
colors = ["Red", "Green", "White", "Blue", "Yellow", "Orange"]

White_summer.pensize(2)  

for i in range(300):  
    White_summer.pencolor(colors[i % 6])
    White_summer.forward(i * 2) 
    White_summer.right(61)

turtle.done()