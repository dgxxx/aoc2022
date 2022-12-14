from tools import config, log, helper
today = "13"

inputfile = "input."+today


def compare2(l, r, level=0):
    prefix = "  "
    for n in range(level):
        prefix += "  "

    print(prefix+"- Compare {} vs {}".format(l, r))
    if type(l) == int:
        if type(r) == int:
            return l-r
        else:
            return compare2([l], y)
    else:
        if type(r) == int:
            return compare2(l, [r])
    print(zip(l, r))
    exit()
    for l1, r1 in


def compare(l, r, level=0):

    status = "wrong"
    prefix = "  "
    for n in range(level):
        prefix += "  "

    print(prefix+"- Compare {} vs {}".format(l, r))

    if type(l) == int and type(r) == list:
        l = [l]
        print(prefix+"- Compare {} vs {}".format(l, r))
    if type(l) == list and type(r) == int:
        r = [r]
        print(prefix+"- Compare {} vs {}".format(l, r))
    if type(l) == int and type(r) == int:
        if l < r:
            status = "right"
            print(prefix + "- Left side is smaller, so inputs are in the right order ")
        elif l == r:
            status = "same"
            # print("==")
        else:
            status = "wrong"
            print(prefix + "- Left side is bigger, so inputs are in the wrong order ")
    elif type(l) == list and type(r) == list:

        res = "=="
        maxitems = len(l)
        if len(r) > maxitems:
            maxitems = len(r)
        #print(prefix + "{} - {} - {}".format(len(l), len(r), maxitems))
        if len(r) == 0:
            res = "wrong"
            print(
                prefix + "Right side ran out of items, so inputs are not in the right order")
            return res
        for item in range(maxitems):
            if item < len(l) and item < len(r):
                l1 = l[item]
                r1 = r[item]
                res = compare(l1, r1, level+1)
            elif item <= len(l) and item > len(r):
                res = "wrong"
                print(
                    prefix + "Right side ran out of items, so inputs are not in the right order")
            else:
                print(prefix + "Left Side ran out of items. Order is right")
                res = "right"
            # print(prefix+"res: {}".format(res))
            if res == "right" or res == "wrong":
                return res
        if len(r) > len(l):
            return "right"
        return res
    else:
        print(prefix + "- Something wrong ")
    return status


def puzzle_01():
    inputdata = helper.read_input(inputfile)
    result = 0
    for index, group in enumerate(inputdata.strip().split("\n\n")):
        print("== Pair {} ==".format(index+1))

        left, right = group.splitlines()
        left = eval(left)
        right = eval(right)

        print("- Compare {} vs {}".format(left, right))

        for itemindex, items in enumerate(zip(left, right)):
            litem, ritem = items

            res = compare2(litem, ritem)
            if res < 0:
                result += index+1

        print("result: {}".format(result))

    print("Puzzle-1: Result: {}".format(result))


def puzzle_02():

    result = 0
    print("Puzzle-2: Result: {}".format(result))


print("-------------------------------")
print("Day {} Results".format(today))
print("-------------------------------")
puzzle_01()
print("-------------------------------")
puzzle_02()
print("-------------------------------")
