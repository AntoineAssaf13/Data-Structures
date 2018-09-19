class Disc:
    def __init__(self,w, xcoord, ycoord):
        self.w = w
        self.l = 20
        self.xcoord = xcoord
        self.ycoord = ycoord
    def draw(self):
        fill(250)
        rect(self.xcoord, self.ycoord, self.w, self.l)
        
    

class Tower:
    def __init__(self,xcoord,num):
        self.w = 8
        self.l = 250
        self.xcoord = xcoord
        self.ycoord = 10
        self.discs = []
        for i in range (num):
            d = Disc((100-(i*10)),(xcoord + 5),(self.ycoord*25-(i*20)))
            self.discs.append(d)
    def push(self):
        self.discs.append((100-(i*10)),(xcoord + 5),(self.ycoord*25-(i*20)))
    def top():
        return self.discs[-1]
    def pop(self):
        r = self.discs[-1]
        self.top_val = self.discs[-2]
        del self.discs[-1]
        return r
        
    def draw(self):
        fill(87)
        rect(self.xcoord, self.ycoord, self.w, self.l)
        for ele in self.discs:
            rectMode(CENTER)
            ele.draw()
        rectMode(CORNER)
        

class Board:
    def __init__(self,lst):
        self.towers = []
        for i,num in enumerate(lst):
            t = Tower((i+1)*200,num)
            self.towers.append(t)
    def draw(self):
        for ele in self.towers:
            ele.draw()
        


def setup():
    global GBoard
    size(800,300)
    background(209)
    fill(0,0,0)
    rect(0,250,799,50)
    GBoard = Board([10,0,0])

def draw():
    global GBoard
    GBoard.draw()
    