import sys
import random
import math

def setup():
    size(1100, 800)
    background(255)
    pixelDensity(displayDensity())
def drawLineAngle(color, start, angle, length, width):
    angle += 180 # make up zero degrees
    end = (start[0] + math.sin(math.radians(angle)) * length, start[1] + math.cos(math.radians(angle)) * length)
    stroke(*color)
    if width:
        strokeWeight(width)
    else:
        noStroke()
    line(*(start + end))
    return end
def drawLeaf(location):
    stroke(0, 50, 0)
    fill(100, 255, 100)
    strokeWeight(0.5)
    ellipse(location[0],location[1],20,20)
    
    
def drawTree(start,leaf, i = 0, angle = 0, width_counter = 15, length_counter = 60):
    global num
    if i == 6:
        return None
    else:
        end = drawLineAngle((0,0,0),start,angle,length_counter, width_counter)
    drawTree(end, leaf, i+1, angle + 20, width_counter/1.5, length_counter-1)
    drawTree(end, leaf, i+1, angle - 20, width_counter/1.5, length_counter-1)
    if leaf:
        drawLeaf(end)
        drawLeaf(end)
        fill(0,0,0)
        text (str(num), end[0], end[1])
        num+=1
        
def keyPressed():
    global leaf
    if key=="l":
        leaf = not leaf
def setup():
    global num
    global leaf
    leaf=True
def draw():
    global num
    num = 0
    clear()
    background(255)
    drawTree((550,800),leaf)