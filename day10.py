from tools import config, log,helper
today="10"

inputfile="input."+today

def puzzle_01():
    inputdata = helper.read_input(inputfile)
    result=0
    cycle=1
    register=1
    points=[20,60,100,140,180,220]
    for item in inputdata:
        

        if item.startswith("noop"):
            command="noop"
            value=""
            #print(command,value)
            #print("c: {} x: {}".format(cycle,register,))
            if cycle in points:
                result+=cycle*register
                #print("res:{}".format(result))
            cycle+=1

        else:
            command,value=item.split()
            #print(command,value)
            #print("c: {} x: {} add 1".format(cycle,register,))
            if cycle in points:
                result+=cycle*register
                #print("res:{}".format(result))
            cycle+=1
            #print("c: {} x: {} add 2".format(cycle,register,))
            if cycle in points:
                result+=cycle*register
                #print("res:{}".format(result))
            cycle+=1
            register+=int(value)
        
     
    print("Puzzle-1: Result: {}".format(result))



def puzzle_02():

    inputdata = helper.read_input(inputfile)
    result=0
    cycle=1
    register=1

    
    crt=[]
    for r in range(6):
        line=[]
        for c in range(40):
            line.append(" ")
        crt.append(line)

    def drawcrt(d):

        for i in d:
            
            for j in i:
                print("{}".format(j) ,end=" ")
                #print(i,j)
            print()
    def drawpixel(cycle,pos):
        
        c=cycle-1
        col=c%40
        row=int(c/40)
        print("CRT POS: {} {}".format(row,col))
        draw=False
        for n in range(-1,2):
            
            if pos+n == col:
                draw=True
            print("cycle: {} pos: {} draw: {} ".format(cycle,pos+n,draw))
        
        if draw:
                c=cycle-1
                col=c%40
                row=int(c/40)
                crt[row][col]="#"
                print("drawing on {} {}".format(row,col))
        else: 
            print("Not drawing on {} {}".format(row,col))
    #def drawcrt():
    #    for r in range(6):
    #       print(crt[r])

    for item in inputdata:
        

        if item.startswith("noop"):
            command="noop"
            value=""
            print(command,value)
            print("c: {} x: {}".format(cycle,register,))
            drawpixel(cycle,register)
            cycle+=1

        else:
            command,value=item.split()
            print(command,value)
            print("c: {} x: {} add 1".format(cycle,register,))
            drawpixel(cycle,register)
            cycle+=1
            print("c: {} x: {} add 2".format(cycle,register,))
            drawpixel(cycle,register)
            cycle+=1
            register+=int(value)
    drawcrt(crt)
    print("Puzzle-2: Result: {}".format(result))


print("-------------------------------")
print("Day {} Results".format(today))
print("-------------------------------")
puzzle_01()
print("-------------------------------")
puzzle_02()
print("-------------------------------")
