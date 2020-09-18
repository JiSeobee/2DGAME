import turtle

turtle.penup()
turtle.goto(-250,-250)

length=-250

while(length<=250):
    turtle.penup()
    turtle.goto(-250,length)
    turtle.pendown()
    turtle.goto(250,length)
    length=length+100

length=250
    
while(length>=-250):
    turtle.penup()
    turtle.goto(length,250)
    turtle.pendown()
    turtle.goto(length,-250)
    length=length-100

turtle.exitonclick()
    
