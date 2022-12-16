import turtle

s= turtle.Screen()
t=turtle.Turtle()

s.bgcolor('grey')

#A
t.penup()
t.goto(-30,50) 
t.pendown()
t.pensize(10)
t.pencolor('black')

t.right(65)
t.forward(100)

t.setpos(-30,50)
t.right(50)
t.forward(100)

t.penup()
t.setpos(-50,-10)
t.right(65)
t.pendown()
t.backward(45)
t.penup()

#9
t.goto(30,-5)
t.pendown() 
t.circle(-20)
t.penup()
t.circle(-20,270)
t.pendown()
t.forward(40)
t.circle(-20,180)





s.exitonclick()










