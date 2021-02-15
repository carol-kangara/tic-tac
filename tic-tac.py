import turtle
import math
#function for drawing the grid the game will be played on
def drawBoard():
#to draw both tha horizontal and the vertical lines
for i in range(2):
    drawer.penup()
    drawer.goto(-300,100-200*i)
    drawer.pendown()
    drawer.foward(600) 
drawer.right(90)
for i in range(2):
    drawer.penup()
    drawer.goto(-100 +200*i,300)
    drawer.pendown()
    drawer.foward(600)   
#adding numbers to the top coners
num=1
for i in range(3):
    for j in range(3):
        drawer.penup()
        drawer.goto(-290+j*200,280-i*200)
        drawer.pendown()
drawer.write(num,font=("Roboto",12)) 
num+=1
#this functiondrawscentered at the input coordinates
def drawX(x,y):
#move to the correct  spot
drawer.penip()
drawer.goto(x,y)
drawer.pendown()

drawer.setheading(60)
#drawing the lines of the x
for i in range(2):
    drawer.foward(75)
    drawer.backward(150)
    drawer.forward(75)
    drawer.left(60)
#screen update
screen.update()
#function to draw "o"centere at the inputted coordinates
def drawO(x,y):
    #move to the correct  spot
drawer.penip()
drawer.goto(x,y +75)
drawer.pendown()

drawer.setheading(0)

#draw a circle
for i in range(180)
drawer.forward(150*math.pi)/180
drawer.right(2)

#screen update
screen.update() 
#creating turtle
drawer=turtle.Turtle()
drawer.pensize(10)
drawer.ht
#add screen
screen=turtle.Screen()
screen.tracer(0)
#call function
drawBoard() 