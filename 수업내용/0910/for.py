for n in [1,3,4,5]:
    print(n)

for c in "py TEST":
    print(c)

for i in range(1,10+1):
    print(i)
    

sum=0

for i in range(1,100+1):
    sum= sum+i
    
print(sum)


import turtle as t

for x,y,r in [(200,200,50), (-200,-200,30), (100,100,50)]:
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.circle(r)
    t.write(str((x,y)))
