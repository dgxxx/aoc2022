import tools as tools
from collections import deque

today="12"

inputfile="input."+today



def puzzle_01():
    inputdata = tools.helper.read_input(inputfile)
    grid=[list(x) for x in inputdata]
    #  print(grid)
    for r, row in enumerate(grid):
        for c,col in enumerate(row):
            if col=="S":
                startr=r
                startc=c
                grid[r][c]="a"
            elif col=="E":
                endr=r
                endc=c
                grid[r][c]="z"
                
    q = deque()
    q.append((0,startr,startc))
    #print(q)
    visited={(startr,startc)}
    while q:
        d,r,c=q.popleft()
        print("{} {} {}".format(d,r,c))
        for nbr,nbc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
            print("  {} {}".format(nbr,nbc))
            if nbr <0 or nbc <0 or nbr >=len(grid) or nbc >= len(grid[0]):
                continue
                # neighbour out of limits
            if (nbr,nbc) in visited:
                continue
            if ord(grid[nbr][nbc])-ord(grid[r][c])>1:
                continue
                # step too hgh
            if nbr==endr and nbc == endc:
                # endpoint reached
                d=d+1
                result=d
                
                break
            visited.add((nbr,nbc))
            q.append((d+1,nbr,nbc))
            print("  {} {}".format(nbr,nbc))
            print(visited)
            print(q)
    result=0
    print("Puzzle-1: Result: {}".format(result))
    


def puzzle_02():

    inputdata = tools.helper.read_input(inputfile)
    result=0
    
    print("Puzzle-2: Result: {}".format(result))


print("-------------------------------")
print("Day {} Results".format(today))
print("-------------------------------")
puzzle_01()
print("-------------------------------")
#puzzle_02()
print("-------------------------------")
