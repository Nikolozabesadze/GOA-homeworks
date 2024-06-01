from turtle import*

speed(100000000000000000000)

width(7)

#castle
begin_fill()
color("dark blue")
forward(400)
left(180)
forward(800)
right(90)
forward(200)
end_fill()

begin_fill()
color("dark red")
right(30)
forward(150)
right(120)
forward(150)
penup()
goto(-400,200)
pendown()
right(300)
forward(150)
end_fill()

begin_fill()
color("dark blue")
right(90)
forward(150)
right(180)
forward(220)
end_fill()

begin_fill()
color("dark red")
right(30)
forward(150)
right(120)
forward(150)
right(120)
forward(150)
right(180)
right(90)
left(90)
forward(150)
right(90)
end_fill()

begin_fill()
color("dark blue")
forward(250)
right(180)
forward(180)
end_fill()



begin_fill()
color("dark red")
right(30)
forward(150)
right(120)
forward(150)
right(120)
forward(150)
right(180)
forward(150)
right(90)
end_fill()


begin_fill()
color("dark blue")
forward(200)
end_fill()


begin_fill()
color("dark blue")
right(90)
forward(450)
right(90)
forward(200)
right(90)
forward(150)
right(90)
forward(200)
end_fill()

begin_fill()
color("dark blue")
right(180)
forward(270)
right(90)
forward(150)
right(90)
forward(270)
end_fill()


begin_fill()
color("dark blue")
right(180)
forward(200)
right(90)
forward(150)
right(90)
forward(200)
end_fill()

#door

penup()
goto(-200,0)
pendown()
begin_fill()
color("brown")
right(180)
forward(90)
right(90)
forward(30)
right(90)
forward(90)
right(90)
forward(30)
end_fill()

begin_fill()
color("brown")
right(180)
forward(60)
left(90)
forward(90)
left(90)
forward(60)
end_fill()

#end of door

#windows

penup()
goto(-355,150)
pendown()
begin_fill()
color("white")
right(90)
forward(25)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

color("grey")
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(25)
right(90)
forward(50)


penup()
goto(-200,200)
pendown()
begin_fill()
color("white")
forward(25)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

color("grey")
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(25)
left(90)
forward(50)



penup()
goto(-20,175)
pendown()
begin_fill()
color("white")
right(90)
forward(25)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

color("grey")
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(25)
right(90)
forward(50)

#making king

penup()
goto(100,0)
pendown()

begin_fill()
color("black")
forward(15)
right(90)
forward(30)
right(90)
forward(15)
right(90)
forward(30)
end_fill()

penup()
goto(115,15)
pendown()

begin_fill()
color("blue")
right(90)
forward(50)
right(90)
forward(15)
right(90)
forward(50)
right(90)
forward(15)
end_fill()

penup()
goto(130,0)
pendown()

begin_fill()
color("black")
right(90)
forward(15)
right(90)
forward(30)
right(90)
forward(15)
right(90)
forward(30)
end_fill()


penup()
goto(130,15)
pendown()

begin_fill()
color("blue")
right(90)
forward(50)
right(90)
forward(15)
right(90)
forward(50)
right(90)
forward(15)
end_fill()


penup()
goto(130,65)
pendown()

begin_fill()
color("red")
forward(15)
right(90)
forward(25)
left(90)
forward(15)
right(90)
forward(25)
right(90)
forward(60)
right(90)
forward(25)
right(90)
forward(15)
left(90)
forward(25)
right(90)
forward(30)
end_fill()

color("black")
right(180)
forward(30)


color("red")

penup()
goto(160,90)
pendown()

left(180)
forward(1)



width(3)
begin_fill()
color("orange")
left(90)
forward(30)
right(90)
forward(10)
right(90)
forward(15)
right(90)
penup()
goto(101,90)
pendown()
begin_fill()
color("orange")
forward(10)
end_fill()


penup()
goto(101,90)
begin_fill()
color("orange")
pendown()
right(90)
forward(30)
left(90)
forward(10)
left(90)
forward(15)
left(90)
forward(10)
end_fill()



right(90)
forward(15)
right(90)
forward(10)
right(90)
forward(30)
right(90)
forward(10)
right(90)
forward(30)
end_fill()


penup()
goto(159,90)
begin_fill()
color("orange")
pendown()
left(90)
forward(10)
left(90)
forward(30)
left(90)
forward(10)
left(90)
forward(30)
end_fill()


penup()
goto(101,90)
pendown()
begin_fill()
color("orange")
right(90)
forward(10)
right(90)
forward(30)
right(90)
forward(10)
right(90)
forward(30)
end_fill()


penup()
goto(150,115)
pendown()
begin_fill()
color("orange")
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

penup()
goto(120,140)
pendown()
color("brown")
right(90)
forward(1)
right(90)
forward(1)
right(90)
forward(1)
right(90)
forward(1)
forward(1)
right(90)
forward(1)
right(90)
forward(1)
right(90)
forward(1)
right(90)
forward(1)
right(90)
forward(1)
right(90)
forward(1)
right(90)
forward(1)
right(90)
forward(1)
right(90)
forward(1)
right(90)
forward(1)
right(90)
forward(1)
right(90)
forward(1)
right(90)



penup()
goto(140,140)
pendown()
color("brown")
left(90)
forward(1)
left(90)
forward(1)
left(90)
forward(1)
left(90)
forward(1)
forward(1)
left(90)
forward(1)
left(90)
forward(1)
left(90)
forward(1)
left(90)
forward(1)
left(90)
forward(1)
left(90)
forward(1)
left(90)
forward(1)
left(90)
forward(1)
left(90)
forward(1)
left(90)
forward(1)
left(90)
forward(1)
left(90)
forward(1)
left(90)


penup()
goto(120,125)
pendown()
right(90)
forward(3)
left(30)
forward(2)
left(30)
forward(5)
left(30)
forward(2)
left(30)
forward(3)

penup()
goto(110,155)
pendown()
begin_fill()
color("yellow")
left(45)
forward(15)
right(140)
forward(15)
left(130)
forward(25)
right(130)
forward(25)
left(130)
forward(15)
right(140)
forward(15)
right(105)
forward(40)
end_fill()

#making queen

penup()
goto(200,0)
pendown()

begin_fill()
color("pink")
right(120)
forward(65)
right(60)
forward(40)
right(60)
forward(65)
right(120)
forward(105)
end_fill()

begin_fill()
penup()
goto(233,57)
right(90)
forward(25)
left(90)
forward(15)
right(90)
forward(25)
right(90)
forward(70)
right(90)
forward(25)
right(90)
forward(15)
left(90)
forward(25)
end_fill()


begin_fill()
penup()
goto(233,107)
pendown()
color("orange")
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()
left(180)
forward(40)
right(90)
forward(20)


begin_fill()
color("brown")
left(90)
forward(10)
left(90)
forward(40)
left(90)
forward(128)
left(150)
forward(40)
left(30)
forward(18)
left(90)
forward(15)
right(90)
forward(25)
right(90)
forward(15)
left(90)
forward(40)
right(90)
forward(20)
end_fill()

left(90)
begin_fill()
color("brown")

forward(10)
right(90)
forward(40)
right(90)
forward(128)
right(150)
forward(40)
right(30)
forward(18)
right(90)
forward(15)
left(90)
forward(25)
left(90)
forward(15)
right(90)
forward(40)
right(90)
forward(20)
end_fill()




width(3)



















































































exitonclick()