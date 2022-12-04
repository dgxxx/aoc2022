from tools import config, log,helper
today="4"

inputfile="input."+today

def lp(p):
    lp=[]
    pl,ph=p.split("-")
    for n in range(int(pl),int(ph)+1):
        lp.append(n)
    return lp
def puzzle_01():
    inputdata = helper.read_input(inputfile)
    result=0
    l=[]
    
    for item in inputdata:
        p1,p2=item.split(",")
        
        
        lp1=lp(p1)
        lp2=lp(p2)
        print(len(lp1-lp2)," ",len(lp2-lp1))
        if all(n in lp1 for n in lp2) or all(n in lp2 for n in lp1):
            result+=1
        
    print("Puzzle-1: Result: {}".format(result))



def puzzle_02():

    inputdata = helper.read_input(inputfile)
    result=0
    
    for item in inputdata:
        p1,p2=item.split(",")
        
        
        lp1=lp(p1)
        lp2=lp(p2)
        
        if any(n in lp1 for n in lp2):
            #or all(n in lp2 for n in lp1):
            result+=1
    print("Puzzle-2: Result: {}".format(result))


print("-------------------------------")
print("Day {} Results".format(today))
print("-------------------------------")
puzzle_01()
print("-------------------------------")
puzzle_02()
print("-------------------------------")
