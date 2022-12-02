from tools import config, log,helper
today="2"

inputfile="input."+today

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
    



def puzzle_01():
    inputdata = helper.read_input(inputfile)
    result=0
    
    for item in inputdata:
        oponent,me=item.split(" ")
        oponent=transform(oponent)
        me=transform(me)
        singleresult=rpc(oponent,me)
        result+=singleresult
    print("Puzzle-1: Result: {}".format(result))



def puzzle_02():

    inputdata = helper.read_input(inputfile)
    result=0
    
    for item in inputdata:
        oponent,res=item.split(" ")
        oponent=transform(oponent)
        me=decisionmatrix[oponent][res]
        singleresult=rpc(oponent,me)
        result+=singleresult
    print("Puzzle-2: Result: {}".format(result))


print("-------------------------------")
print("Day {} Results".format(today))
print("-------------------------------")
puzzle_01()
print("-------------------------------")
puzzle_02()
print("-------------------------------")
