from tools import config, log,helper
today="11"

inputfile="input."+today

monkeys={}
inspects=[]
def puzzle_01():
    inputdata = helper.read_input(inputfile)
    result=0
    
    for item in inputdata:
        print(item)
        if item.startswith("Monkey"):
            monkey=int(item.split(" ")[1].replace(":",""))
            print("Monkey: {}".format(monkey))
            monkeys[monkey]={}
            startitems=[]
            value=0
            operand=""
            divisor=0
            truemonkey=0
            falsemonkey=0
            monkeys[monkey]["inspect"]=0
            inspects.append(0)
        elif item.startswith("  Starting items"):
            startitems=[]
            startitems=item.replace(",","").split(" ")[4:]
            print("startitems: {}".format(startitems))
            #monkeys[monkey]["startitems"]=[]
            monkeys[monkey]["startitems"]=startitems
        elif item.startswith("  Operation:"):
            value=item.split(" ")[-1]    
            operand=item.split(" ")[-2]
            print("operand: {}".format(operand))
            print("value: {}".format(value))
            monkeys[monkey]["op"]=operand
            monkeys[monkey]["value"]=value
        elif item.startswith("  Test"):
            divisor=int(item.split(" ")[-1])
            print("divisor: {}".format(divisor))
            monkeys[monkey]["test"]=divisor
        elif item.startswith("    If true"):
            truemonkey=int(item.split(" ")[-1])
            print("truemonkey:{}".format(truemonkey))
            monkeys[monkey]["true"]=truemonkey
        elif item.startswith("    If false"):    
            falsemonkey=int(item.split(" ")[-1])
            print("falsemonkey:{}".format(falsemonkey))
            monkeys[monkey]["false"]=falsemonkey
    
    
    
    
    
    print(monkeys)
    ### run rounds
    
    for round in range(20):
        
        for m in range(len(monkeys)):
            print("round: {}".format(round))
            print(" Monkey: {}".format(m))
            print("monkey:{}".format(monkeys[m]))
            while monkeys[m]["startitems"]:
                monkeys[m]["inspect"]+=1
                inspects[m]+=1
                old=monkeys[m]["startitems"].pop()

                operand=monkeys[m]["op"]
                value=monkeys[m]["value"]
                if operand =="*":
                    if value=="old":
                        new=int(old)*int(old)
                    else:
                        new=int(old)*int(value)
                if operand =="+":
                    if value=="old":
                        new=int(old)+int(old)
                    else:
                        new=int(old)+int(value)
                new=int(new/3)
                divisor=monkeys[m]["test"]
                if new%divisor==0:
                    newmonkey=monkeys[m]["true"]
                else:
                    newmonkey=monkeys[m]["false"]
                monkeys[newmonkey]["startitems"].append(new)
                
    for m in range(len(monkeys)):
        print(monkeys[m])
    print(inspects)
    inspects.sort(reverse=True)
    print(inspects)
    result=inspects[0]*inspects[1]
    print("Puzzle-1: Result: {}".format(result))



def puzzle_02():


    inputdata = helper.read_input(inputfile)
    result=0
    
    for item in inputdata:
        print(item)
        if item.startswith("Monkey"):
            monkey=int(item.split(" ")[1].replace(":",""))
            print("Monkey: {}".format(monkey))
            monkeys[monkey]={}
            startitems=[]
            value=0
            operand=""
            divisor=0
            truemonkey=0
            falsemonkey=0
            monkeys[monkey]["inspect"]=0
            inspects.append(0)
        elif item.startswith("  Starting items"):
            startitems=[]
            startitems=item.replace(",","").split(" ")[4:]
            print("startitems: {}".format(startitems))
            #monkeys[monkey]["startitems"]=[]
            monkeys[monkey]["startitems"]=startitems
        elif item.startswith("  Operation:"):
            value=item.split(" ")[-1]    
            operand=item.split(" ")[-2]
            print("operand: {}".format(operand))
            print("value: {}".format(value))
            monkeys[monkey]["op"]=operand
            monkeys[monkey]["value"]=value
        elif item.startswith("  Test"):
            divisor=int(item.split(" ")[-1])
            print("divisor: {}".format(divisor))
            monkeys[monkey]["test"]=divisor
        elif item.startswith("    If true"):
            truemonkey=int(item.split(" ")[-1])
            print("truemonkey:{}".format(truemonkey))
            monkeys[monkey]["true"]=truemonkey
        elif item.startswith("    If false"):    
            falsemonkey=int(item.split(" ")[-1])
            print("falsemonkey:{}".format(falsemonkey))
            monkeys[monkey]["false"]=falsemonkey
    
    
    
    
    
    #print(monkeys)
    ### run rounds
    
    for round in range(10000):
        print("round: {}".format(round))
        for m in range(len(monkeys)):
            
            print(" Monkey: {} {}".format(m,len(monkeys[m]["startitems"])),end="")
            #print("monkey:{}".format(monkeys[m]))
            while monkeys[m]["startitems"]:
                #monkeys[m]["inspect"]+=1
                inspects[m]+=1
                old=monkeys[m]["startitems"].pop()

                operand=monkeys[m]["op"]
                value=monkeys[m]["value"]
                if operand =="*":
                    if value=="old":
                        new=int(old)*int(old)
                    else:
                        new=int(old)*int(value)
                if operand =="+":
                    if value=="old":
                        new=int(old)+int(old)
                    else:
                        new=int(old)+int(value)
                #new=int(new/3)
                divisor=monkeys[m]["test"]
                if new%divisor==0:
                    newmonkey=monkeys[m]["true"]
                else:
                    newmonkey=monkeys[m]["false"]
                    
                monkeys[newmonkey]["startitems"].append(new)
                print("-> {}".format(newmonkey),end="")
            print()
            #for m in range(len(monkeys)):
            #    print("Monkey {} : {}".format(m,monkeys[m]["startitems"])      )   
        print("inspects: {}".format(inspects))
    for m in range(len(monkeys)):
        print(monkeys[m])
    #print(inspects)
    inspects.sort(reverse=True)
    print(inspects)
    result=inspects[0]*inspects[1]


    print("Puzzle-2: Result: {}".format(result))


print("-------------------------------")
print("Day {} Results".format(today))
print("-------------------------------")
#puzzle_01()
print("-------------------------------")
puzzle_02()
print("-------------------------------")
