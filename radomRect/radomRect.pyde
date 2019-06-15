def setup():
    size(400,400)
    background(0)
    stroke(0)
    fill(255)
    frameRate(10)
    smooth()

def draw():
    k = 0
    l = 0
    while k <= width:
        while l <= height:
            rect(k,l,5,5)
            fill(random(255))
            l += 5
        l = 0
        k += 5
    
