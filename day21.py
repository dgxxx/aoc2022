from tools import config, log,helper
today="21"

inputfile="input."+today

def puzzle_01():
    inputdata = helper.read_input(inputfile)
    result=0
    
    for item in inputdata:
        print(item)
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
puzzle_02()
print("-------------------------------")
