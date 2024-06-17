from turtle import *

#we want to draw house

speed(5)
speed(5)
shape("turtle")
width(7)
forward(200)

begin_fill()
color("green")
left(90)
forward(200)

left(90)
forward(200)

left(90)
forward(200)
end_fill()


#end of square


left(90)
forward(70)

begin_fill()
color("yellow")

left(90)
forward(100)


right(90)

forward(60)

right(90)
forward(100)

end_fill()


#end of the door

penup()
goto(200,200)
pendown()

begin_fill()
color("red")
right(150)
forward(200)
left(120)
forward(200)
end_fill()


#end of the roof


#starting windows)
color("white")
penup()
goto(120,130)
pendown()
right(150)
forward(30)

right(90)
forward(15)

right(90)
forward(30)

right(90)
forward(15)
right(180)
forward(30)
left(90)
forward(30)
left(90)
forward(15)
end_fill()


penup()
goto(80,130)
pendown()

forward(30)
right(90)
forward(30)
right(90)
forward(15)
right(90)
forward(30)
left(90)
forward(15)
left(90)
forward(30)
left(90)
forward(15)

penup()
goto(300,300)
pendown()



exitonclick()