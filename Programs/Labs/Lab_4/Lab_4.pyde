import random

grid = [[False]*50 for n in range (50)]
grid2 = [[False]*50 for n in range (50)]
check = False
w = 10

def setup():
    size(500,500)
    x,y = 0,0
    for row in range(len(grid)):
        for col in range(len(grid)):
            r = random.randint(0,2)
            if r == 0:
                stroke(0)
                fill(255)
            else:
                stroke(255)
                fill(0)
                grid[row][col] = True
            rect(col*w,row*w,w,w)

def draw():
    global grid
    global grid2
    checker = 0
    for row in range(len(grid)):
        for col in range (len(grid)):
            #-------------------------------#
            try:
                if grid[row-1][col] == True:
                    checker += 1
                if grid[row-1][col-1] == True:
                    checker += 1
                if grid[row][col-1] == True:
                    checker +=1
                if grid[row+1][col] == True:
                    checker +=1
                if grid[row+1][col+1] == True:
                    checker += 1
                if grid[row][col+1] == True:
                    checker += 1
                if grid[row-1][col+1] == True:
                    checker += 1
                if grid[row+1][col-1] == True:
                    checker += 1
            except IndexError:
                continue
            #------------------------------#
            if grid[row][col] == True:
                if checker == 1:
                    fill(0,0,255)
                if checker == 2:
                    fill(204,102,0)
                elif checker == 3:
                    fill(77,255,0)
                grid2[row][col] = True
            elif grid[row][col] == False and checker == 3:
                fill(255,255,0)
                grid2[row][col] = True
            else:
                stroke(0)
                fill(255)
                grid2[row][col] = False
                
            #     c=random.choice([(204,102,0),(255,0,0),(77,255,0),(255,255,0)])
            #     print(c[0],c[1],c[2])
            #     fill(c[0],c[1],c[2])
            rect(col*w,row*w,w,w)
            checker = 0
    grid2, grid = grid, grid2

def keyPressed():
    global check
    if key ==' ':
        if check == False:
            noLoop()
            check = True
        else:
            loop()
            check = False

def mouseClicked():
    global grid
    grid[mouseX//10][mouseY//10] = not grid[mouseX//10][mouseY//10]
    print(mouseX//10,mouseY//10)
        
    
    