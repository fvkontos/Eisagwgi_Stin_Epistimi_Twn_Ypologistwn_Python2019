import random

def minesweeper(a):
    for line in a:
        brd = ' '.join(str(X) for X in line)
        print (brd)

def up(grid, X):
    return 1 if grid[X-10]=="*" else 0
def down(grid, X):
    return 1 if grid[X+10]=="*" else 0
def left(grid, X):
    return 1 if grid[X-1]=="*" else 0
def right(grid, X):
    return 1 if grid[X+1]=="*" else 0
def ul(grid, X):
    return 1 if grid[X-11]=="*" else 0
def ur(grid, X):
    return 1 if grid[X-9]=="*" else 0
def dl(grid, X):
    return 1 if grid[X+9]=="*" else 0
def dr(grid, X):
    return 1 if grid[X+11]=="*" else 0

bombs = int(input("Enter number of bombs(0-100): "))
while (bombs < 0 or bombs > 100):
    bombs= input("ERROR: Notice that you have to give a number from 0 to 100! ")
v = [0]*(100-bombs)
v += ["*"]*bombs
random.shuffle(v)

for b in range(100):
    if v[b]==0:
        if b==0:
            v[b] += down(v,b) + right(v,b) + dr(v,b)
        elif b==9:
            v[b] += down(v,b) + left(v,b) + dr(v,b)
        elif b==90:
            v[b] += up(v,b) + right(v,b) + ur(v,b)
        elif b==99:
            v[b] += up(v,b) + left(v,b) + ul(v,b)
        elif b<9:
            v[b] += left(v,b) + dl(v,b) + down(v,b) + dr(v,b) + right(v,b)
        elif b>90:
            v[b] += left(v,b) + ul(v,b) + up(v,b) + ur(v,b) + right(v,b)
        elif b%10==0:
            v[b] += up(v,b) + ur(v,b) + right(v,b) + dr(v,b) + down(v,b)
        elif b%10==9:
            v[b] += up(v,b) + ul(v,b) + left(v,b) + dl(v,b) + down(v,b)
        else:
            v[b] += up(v,b) + down(v,b) + right(v,b) + left(v,b) + ur(v,b) + \
                      dr(v,b) + ul(v,b) + dl(v,b)

grid = []
for x in range(10):
    grid += [v[10*x:10*x+10]]

minesweeper(grid)
