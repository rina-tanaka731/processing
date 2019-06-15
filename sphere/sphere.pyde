def setup():
    size(600, 600, P3D)
    colorMode(HSB, 360, 100, 100, 100)
    background(0)
    blendMode(ADD)
    noFill()
    
def draw():
    colnoise = random(10)
    translate(width/2, height/2, 0)
    rotateY(frameCount * 0.002)
    rotateZ(frameCount * 0.003)
    rotateX(frameCount * 0.003)
    rotateX(noise(frameCount * 0.003))
    
    s = 0
    t = 0
    x = 0
    y = 0
    z = 0
    
    beginShape()
    radius = 200
    while s <= 180:
        t += 3
        s += 1
        radianS = radians(s)
        radianT = radians(t)
        
        x = radius * cos(radianS) * sin(radianT)
        y = radius * sin(radianS) * sin(radianT)
        z = radius * cos(radianT)
        stroke(noise(colnoise), 80, 60, 10)
        vertex(x,y,z)
        
    endShape()
    colnoise += 1
