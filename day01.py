from tools import config, log,helper
today="1"

inputfile="input."+today

def puzzle_01():
    inputdata = helper.read_input(inputfile)
    result=0
    
    maxcalories = 0
    calories = 0
    for item in inputdata:
        # print(item)
        if item == "":
            #print("Result: {}".format(calories))
            if calories > maxcalories:
                maxcalories = calories
            calories = 0
        else:
            calories += int(item)
            #print("calories: {} ".format(calories))
    result=maxcalories
    print("Puzzle-1: Result: {}".format(result))



def puzzle_02():

    inputdata = helper.read_input(inputfile)
    topelves = []
    maxcalories = 0
    calories = 0
    for item in inputdata:
        # print(item)
        if item == "":
            # print("Result: {}".format(calories))
            if calories > maxcalories:
                maxcalories = calories
            topelves.append(calories)
            calories = 0
        else:
            calories += int(item)
            # print("calories: {} ".format(calories))
    # print(topelves)
    topelves.sort(reverse=True)
    result = sum(topelves[0:3])
    print("Puzzle-2: Result: {}".format(result))


print("-------------------------------")
print("Day {} Results".format(today))
print("-------------------------------")
puzzle_01()
print("-------------------------------")
puzzle_02()
print("-------------------------------")