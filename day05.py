from tools import config, log,helper
today="5"

inputfile="input."+today

def puzzle_01():
    inputdata = helper.read_input(inputfile)
    result=0
    stacks={}
    stacknr=9
    for m in range(1,stacknr+1):
        stacks[m]=[]
    
    for item in inputdata:
        if item.find("move")>=0:
            #print("move: {}".format(item))
            todo=item.replace("move|from|to","").split(" ")
            amount=int(todo[1])
            f=int(todo[3])
            t=int(todo[5])
            for x in range(1,amount+1):
                field=stacks[f].pop()
                stacks[t].append(field)
            
        elif item=="" or item.find("[")<0:
            next
            
        else:
            m=1
            for n in range(1,stacknr*4,4):
                field=item[n]
                if field != " ":
                    stacks[m].insert(0,field)
                m+=1
        result=""
    for n in range(1,stacknr+1):
        #print(n,": ",stacks[n])
        result+=stacks[n].pop()
    print("Puzzle-1: Result: {}".format(result))



def puzzle_02():

    inputdata = helper.read_input(inputfile)
    result=0
    stacks={}
    stacknr=9
    for m in range(1,stacknr+1):
        stacks[m]=[]
    
    for item in inputdata:
        if item.find("move")>=0:
            print("move: {}".format(item))
            todo=item.replace("move|from|to","").split(" ")
            amount=int(todo[1])
            f=int(todo[3])
            t=int(todo[5])
            fields=stacks[f][-amount:]
            print(fields)
            stacks[t].extend(fields)
            for x in range(1,amount+1):
                stacks[f].pop()
            
        elif item=="" or item.find("[")<0:
            next
            
        else:
            m=1
            
            for n in range(1,stacknr*4,4):
                field=item[n]
                if field != " ":
                    stacks[m].insert(0,field)
                m+=1
        result=""
    for n in range(1,stacknr+1):
        #print(n,": ",stacks[n])
        result+=stacks[n].pop()

    print("Puzzle-2: Result: {}".format(result))


print("-------------------------------")
print("Day {} Results".format(today))
print("-------------------------------")
puzzle_01()
print("-------------------------------")
puzzle_02()
print("-------------------------------")
