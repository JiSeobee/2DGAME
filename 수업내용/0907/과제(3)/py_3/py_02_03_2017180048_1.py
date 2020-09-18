import turtle

def move(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def jaeum_mieum():
    move(-500,500)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)

def moeum_u():
    move(-525,350)
    turtle.right(90)
    turtle.forward(150)
    move(-450,350)
    turtle.right(90)
    turtle.forward(80)

def jaeum_nieun():
    move(-500,300)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(110)

def jaeum_jieut():
    move(-300,450)
    turtle.forward(100)
    turtle.right(130)
    turtle.forward(130)
    move(-190,350)
    turtle.right(110)
    turtle.forward(75)

def moeum_i():
    move(-150,475)
    turtle.left(150)
    turtle.forward(150)

def jaeum_siot():
    move(0,450)
    turtle.right(40)
    turtle.forward(100)
    move(30,375)
    turtle.right(100)
    turtle.forward(73)

def moeum_eo():
    move(80,475)
    turtle.left(140)
    turtle.forward(125)
    move(80,425)
    turtle.right(90)
    turtle.forward(40)

def jaeum_bieup():
    move(-25,325)
    turtle.left(90)
    turtle.forward(75)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(75)
    move(75,290)
    turtle.left(90)
    turtle.forward(100)
    
jaeum_mieum()
moeum_u()
jaeum_nieun()
jaeum_jieut()
moeum_i()
jaeum_siot()
moeum_eo()
jaeum_bieup()

turtle.exitonclick()


    
    
    
    


    

