from tools import config, log,helper
today="8"

inputfile="input."+today#+".test"
field=[]
f={}

def genv(gridsize):
    v={}
    for l in range(0,gridsize):
        v[l]={}
        for r in range(0,gridsize):
            v[l][r]=0
    return v

def checklines(gridsize,f,v):
    clipsize=0

    for l in range(0,gridsize):
        clipsize=0
        for r in range(0,gridsize):
        
            if int(f[l][r])>clipsize or clipsize==0:
                clipsize=int(f[l][r])
                v[l][r]=1
            print("l: {} r: {} clipsize: {} , val: {} vis: {}".format(l,r,clipsize,int(f[l][r]),v[l][r]))
        clipsize=0

        for r in range(gridsize-1,0,-1):
            #print(clipsize,int(f[l][r]))
            if int(f[l][r])>clipsize or clipsize==0:
                clipsize=int(f[l][r])
                v[l][r]=1
    return v


def checkrows(gridsize,f,v):
    clipsize=0

    for r in range(0,gridsize):
        clipsize=0
        for l in range(0,gridsize):
        
            if int(f[l][r])>clipsize or clipsize==0:
                clipsize=int(f[l][r])
                v[l][r]=1
            print("l: {} r: {} clipsize: {} , val: {} vis: {}".format(l,r,clipsize,int(f[l][r]),v[l][r]))
        clipsize=0

        for l in range(gridsize-1,0,-1):
            #print(clipsize,int(f[l][r]))
            if int(f[l][r])>clipsize or clipsize==0:
                clipsize=int(f[l][r])
                v[l][r]=1
    return v

def pr(d):

    for i in range(0,len(d)):
        
        for j in range(0,len(d)):
            print("{}".format(d[i][j]), end=" ")
            #print(i,j)
        print()

def puzzle_01():
    inputdata = helper.read_input(inputfile)

    result=0
    
    l=0
    gridsize=len(inputdata[0])
    #print(gridsize)
    v=genv(gridsize)
    for item in inputdata:
        f[l]={}
        r=0
        for i in item:
            f[l][r]=i
            r+=1
        field.append(item)
        l+=1

    v=checklines(gridsize,f,v)
    pr(v)
    v=checkrows(gridsize,f,v)
    pr(v)
    for l in range(0,gridsize):
        for r in range(0,gridsize):
            result+=v[l][r]
    print("Puzzle-1: Result: {}".format(result))



def puzzle_02():

    inputdata = helper.read_input(inputfile)
    result=0
    
    for item in inputdata:
        print(item)
    print("Puzzle-2: Result: {}".format(result))


print("-------------------------------")
print("Day {} Results".format(today))
print("-------------------------------")
puzzle_01()
print("-------------------------------")
#puzzle_02()
print("-------------------------------")
