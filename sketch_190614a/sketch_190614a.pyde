def setup():
    size(600, 600)
    background(0)
    noStroke()
    myCircle(width/2, height/2, 500)
    
def myCircle(centerX, centerY, diameter):
    radius = diameter/2
    count = 50000
    for i in range(count):
        angle = random(TWO_PI)
        r = random(1)
        x = centerX + r * radius * cos(angle)
        y = centerY + r * radius * sin(angle)
        circle(x, y, 1.5)
        fill(random(125),random(225),random(255))
