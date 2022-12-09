from tools import config, log,helper
today="9"

inputfile="input."+today#+".test"


def calc_tpos(h,t):
    #print("calc h: {} t: {}".format(h,t))
    if abs(h["x"]-t["x"])<=1 and abs(h["y"]-t["y"])<=1:
        #print("No move")
        return t
    elif h["x"]-t["x"] ==0:
        if h["y"]-t["y"]>1:
            t["y"]+=1
            #print("Move U")
        elif h["y"]-t["y"]<-1:
            t["y"]-=1
            #print("Move D")
    elif h["y"]-t["y"]==0:
        if h["x"]-t["x"] >1:
            t["x"]+=1
            #print("Move R")
        elif h["x"]-t["x"] <-1:
            t["x"]-=1
            #print("Move L")
    elif h["x"]-t["x"]>0 and h["y"]-t["y"]>0:
        #print("jump UR")
        t["x"]+=1
        t["y"]+=1
    elif h["x"]-t["x"]>0 and h["y"]-t["y"]<0:
        #print("Jump DR")
        t["x"]+=1
        t["y"]-=1
    elif h["x"]-t["x"]<0 and h["y"]-t["y"]<0:
        #print("Jump DL")
        t["x"]-=1
        t["y"]-=1
    elif h["x"]-t["x"]<0 and h["y"]-t["y"]>0:
        #print("Jump UL")
        t["x"]-=1
        t["y"]+=1
    else:
        print("Something Wrong")
    #print(t)
    return t

def puzzle_02():
   
    

    def calc_result1():
        result=0
        for l in visited:
            for c in visited[l]:
                result+=visited[l][c]
            #for r in range(0,matrixsize):
        return result

    def genv():
        if matrixsize>20:
            return
        v={}
        
        for l in range(matrixsize):
            v[l]={}
            for c in range(matrixsize):
                v[l][c]="."
        
        for n in range(taillength-1,-1,-1):
            v[tail[n]["x"]][tail[n]["y"]]=n
        v[hpos["x"]][hpos["y"]]="H"
        pr(v)

    def pr(d):
        if matrixsize>20:
            return
        maxx=maxy=matrixsize#int(hpos["x"])
        for i in range(matrixsize-1,-1,-1):
            
            for j in range(matrixsize):
                print("{}".format(d[j][i]), end=" ")
                ##print(i,j)
            print()
        print("--------------------------------------")

    def calc_tail():
        #print("tail H - 0")
        tail[0]=calc_tpos(hpos,tail[0])
        
        for n in range(taillength-1):
            #print("tail: {}".format(tail))
            #print("Tail {} - {}".format(n,n+1))
            tail[n+1]=calc_tpos(tail[n],tail[n+1])
        #print("tail: {}".format(tail))
        visited[tail[taillength-1]["x"]][tail[taillength-1]["y"]]=1
    
        
##################################
    inputdata = helper.read_input(inputfile)
    result=0
    matrixsize=1000
    hpos={"x":matrixsize/2,"y":matrixsize/2}
    tpos={"x":matrixsize/2,"y":matrixsize/2}
    tail=[]
    taillength=9
    for n in range(taillength):
        tail.append({"x":matrixsize/2,"y":matrixsize/2})
    
    visited={}
    for l in range(0,matrixsize):
        visited[l]={}
        for c in range(0,matrixsize):
            visited[l][c]=0
##################################           
    genv()
    count=1
    max=len(inputdata)
    for item in inputdata:
        
        print("item: {}/{}".format(count,max),end="\r")
        count+=1
        d,c=item.split(" ")
        c=int(c)
        #print("###################################")
        #print("Start {} - {}".format(hpos,tpos))
        #print("Move:"+d,c)
        if d =="U":
            for n in range(c):
                
                hpos["y"]+=1
                #print("{} - {}".format(hpos,tpos))
                
                calc_tail()
                genv()
        elif d=="D":
            for n in range(c):
                hpos["y"]-=1
                #print("{} - {}".format(hpos,tpos))
                genv()
                calc_tail()
                genv()
        elif d=="R":
            for n in range(c):
                hpos["x"]+=1
                #print("{} - {}".format(hpos,tpos))
                genv()
                calc_tail()
                genv()
        elif d=="L":
            for n in range(c):
                hpos["x"]-=1
                #print("{} - {}".format(hpos,tpos))
                genv()
                calc_tail()
                genv()
    pr(visited)
    result=calc_result1()
    print("Puzzle-2: Result: {}".format(result))


print("-------------------------------")
print("Day {} Results".format(today))
print("-------------------------------")
#puzzle_01())
print("-------------------------------")
puzzle_02()
print("-------------------------------")
