step = 0.02
myNoise = 0.0
start = 0.0

def setup():
    size(400,400)

def draw():
    background(255)
    myNoise = start
    for x in range(width):
        myColor = noise(myNoise)*255
        
        stroke(myColor,myColor,myColor)
        line(x,0,x,height)
        
        myNoise += step
