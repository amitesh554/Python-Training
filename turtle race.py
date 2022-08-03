from turtle import Turtle,Screen
import random


b=Screen()

on_screen=True

user_inp=b.textinput(title="Turtle Race", prompt="Enter your bet:Choose which Turtle will win")
b.setup(width=500,height=400)
angle=[-70,-40,-10,20,50,80]
col=["blue","red","Yellow","green","orange","black"]
all_turtles=[]

for i in range(6):
    a=Turtle(shape="turtle")
    a.color(col[i])
    a.penup()
    a.goto(x=-250,y=angle[i])
    all_turtles.append(a)



while on_screen:
    for turtles in all_turtles:
        if turtles.xcor()>250:
            on_screen=False
            winning_col=turtles.pencolor()
            if(user_inp==winning_col):
                print(f'You have won. The winning color is {winning_col}')
            else:
                print(f'You have lost. The winning color is {winning_col}')
        dist=random.randint(0,10)
        turtles.forward(dist)


b.exitonclick()