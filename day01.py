#from tools import config, log


def read_input(name):
    with open(name, "r") as i:
        inputdata = i.read().splitlines()
    return inputdata


def day01_01():
    inputdata = read_input("input.1.1")
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
    print("Day01-1: Max Result: {}".format(maxcalories))


def day01_02():

    inputdata = read_input("input.1.1")
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
    print("Day01-2: Max Result: {}".format(result))


print("-------------------------------")
print("Day 01 Results")
print("-------------------------------")
day01_01()
print("-------------------------------")
day01_02()
print("-------------------------------")
