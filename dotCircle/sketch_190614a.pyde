def setup():
    size(1000, 1000)
    noStroke()
    background(0)
    myCircle1()
    myCircle2()
 
def myCircle1():
    count = 20000
    radius = 400
    for i in range(count):
        angle = random(TWO_PI)
        r = sqrt(1 - random(random(1)))
        x = width/2 + r * radius * cos(angle)
        y = height/2 + r * radius * sin(angle)
        circle(x, y, 2)
        fill(random(125), random(255), random(255))
        
def myCircle2():
    count = 20000
    radius = 400
    for i in range(count):
        angle = random(TWO_PI)
        r = random(1)
        x = width/2 + r * radius * cos(angle)
        y = height/2 + r * radius * sin(angle)
        circle(x, y, 2)
        fill(random(225), random(125), random(255))
        
