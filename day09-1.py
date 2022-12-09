from tools import config, log,helper
today="9"

inputfile="input."+today#+".test"



def puzzle_01():
   
    inputdata = helper.read_input(inputfile)
    result=0
    hpos={"x":500,"y":500}
    tpos={"x":500,"y":500}
    
    matrixsize=1000
    visited={}
    for l in range(0,matrixsize):
        visited[l]={}
        for r in range(0,matrixsize):
            visited[l][r]=0

    def calc_result1():
        result=0
        for l in visited:
            for r in visited[l]:
                result+=visited[l][r]
            #for r in range(0,matrixsize):
        return result

    def genv():
        v={}
        
        for l in range(matrixsize):
            v[l]={}
            for r in range(0,matrixsize):
                v[l][r]="."
        v[hpos["x"]][hpos["y"]]="H"
        #v["1"]["1"]="H"
        v[tpos["x"]][tpos["y"]]="T"
        pr(v)

    def pr(d):
        maxx=int(hpos["x"])
        if maxx<10:
            maxx=10
        maxy=int(hpos["y"])
        
        if maxy<10:
            maxy=10
        for i in range(maxy+10,maxy-10,-1):
            
            for j in range(maxx-10,maxx+10):
                print("{}".format(d[i][j]), end=" ")
                #print(i,j)
            print()
        print("--------------------------------------")


    def calc_tpos():
        if abs(hpos["x"]-tpos["x"])<=1 and abs(hpos["y"]-tpos["y"])<=1:
            print("no need to move t")


        elif hpos["x"]-tpos["x"] ==0:
            if hpos["y"]-tpos["y"]>1:
                tpos["y"]+=1
            elif hpos["y"]-tpos["y"]<-1:
                tpos["y"]-=1
        elif hpos["y"]-tpos["y"]==0:
            if hpos["x"]-tpos["x"] >1:
                tpos["x"]+=1
            elif hpos["x"]-tpos["x"] <-1:
                tpos["x"]-=1
        elif hpos["x"]-tpos["x"]>0 and hpos["y"]-tpos["y"]>0:
            tpos["x"]+=1
            tpos["y"]+=1
        elif hpos["x"]-tpos["x"]>0 and hpos["y"]-tpos["y"]<0:
            tpos["x"]+=1
            tpos["y"]-=1
        elif hpos["x"]-tpos["x"]<0 and hpos["y"]-tpos["y"]<0:
            tpos["x"]-=1
            tpos["y"]-=1
        elif hpos["x"]-tpos["x"]<0 and hpos["y"]-tpos["y"]>0:
            tpos["x"]-=1
            tpos["y"]+=1
        visited[tpos["x"]][tpos["y"]]=1


    for item in inputdata:
        d,c=item.split(" ")
        c=int(c)
        print(d,c)
        

        if d =="U":
            for n in range(c):
                hpos["y"]+=1
                print("{} - {}".format(hpos,tpos))
                #genv()
                calc_tpos()
                #genv()
        elif d=="D":
            for n in range(c):
                hpos["y"]-=1
                print("{} - {}".format(hpos,tpos))
                #genv()
                calc_tpos()
                #genv()
        elif d=="R":
            for n in range(c):
                hpos["x"]+=1
                print("{} - {}".format(hpos,tpos))
                #genv()
                calc_tpos()
                #genv()
        elif d=="L":
            for n in range(c):
                hpos["x"]-=1
                print("{} - {}".format(hpos,tpos))
                #genv()
                calc_tpos()
                #genv()
    pr(visited)
    result=calc_result1()
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
