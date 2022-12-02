#from tools import config, log

decisionmatrix={"R": {"X":"S","Y":"R","Z":"P"},
            "P":{"X":"R","Y":"P","Z":"S"},
            "S":{"X":"P","Y":"S","Z":"R"}
            }
playmatrix={"R": {"R":"Y","P":"Z","S":"X"},
            "P":{"R":"X","P":"Y","S":"Z"},
            "S":{"R":"Z","P":"X","S":"Y"}
            }
rpsmatrix={"R":1,"P":2,"S":3}
scorematrix={"X":0,"Y":3,"Z":6}

def read_input(name):
    with open(name, "r") as i:
        inputdata = i.read().splitlines()
    return inputdata

def transform(input):
    matrix={"A":"R","B":"P","C":"S","X":"R","Y":"P","Z":"S"}
    return matrix[input]

def rpc(oponent, me):
    result=0
    score=0
    #oponbnent:
    # # a= rock
    # b = paper
    # c = scissor
    # to play
    # x = rock
    # y = paper
    # z = scissor
    #print("op: {} me: {}".format(oponent,me))
    result=playmatrix[oponent][me]
    score=scorematrix[result]
    rpsscore=rpsmatrix[me]
    finalresult=score+rpsscore
    return finalresult
    

def day02_01():
    inputdata = read_input("input.2")
    result=0
    
    for item in inputdata:
        #print(item)
        oponent,me=item.split(" ")
        oponent=transform(oponent)
        me=transform(me)
        singleresult=rpc(oponent,me)
        result+=singleresult
    print("Day02-1: Result: {}".format(result))



def day02_02():

    inputdata = read_input("input.2")
    result=0
    
    for item in inputdata:
        #print(item)
        oponent,res=item.split(" ")
        oponent=transform(oponent)
        me=decisionmatrix[oponent][res]
        singleresult=rpc(oponent,me)
        result+=singleresult
    print("Day02-2: Max Result: {}".format(result))


print("-------------------------------")
print("Day 02 Results")
print("-------------------------------")
day02_01()
print("-------------------------------")
day02_02()
print("-------------------------------")
