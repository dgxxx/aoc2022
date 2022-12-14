from tools import config, log, helper
import tools
today = "14"

inputfile = "input."+today

for y in range(500):
    for y in range()


def puzzle_01():
    inputdata = helper.read_input(inputfile)
    result = 0

    for path in inputdata:
        print(path)
        for point in path.split(" -> "):
            print(point)


def puzzle_02():

    inputdata = helper.read_input(inputfile)
    result = 0

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
