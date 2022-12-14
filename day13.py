from tools import config, log, helper
today = "13"

inputfile = "input."+today


def compare(l, r, level=0):

    prefix = "  "
    for n in range(level):
        prefix += "  "

    print(prefix+"- Compare {} ({}) vs {} ({}".format(l, type(l), r, type(r)))

    if type(l) == int:
        if type(r) == int:
            return l-r

        else:
            return compare([l], r, level+1)
    else:
        if type(r) == int:
            return compare(l, [r], level+1)

    # both list

    maxitems = len(l)
    # print(maxitems)
    for n in range(maxitems):
        print("{}- n: {} ".format(prefix, n))
        if len(r) > n:
            res2 = compare(l[n], r[n], level+1)
            if res2 != 0:
                print("{}- returning {}".format(prefix, res2))
                return res2
            else:
                print("{}- res= {}".format(prefix, res2))
        else:
            return 1
    return len(l)-len(r)


def puzzle_01():
    inputdata = helper.read_input(inputfile)
    result = 0
    for index, group in enumerate(inputdata.strip().split("\n\n")):
        print("== Pair {} ==".format(index+1))

        left, right = group.splitlines()
        left = eval(left)
        right = eval(right)

        print("- Compare {} vs {}".format(left, right))
        res = compare(left, right)
        if res < 0:
            result += index+1

        ''' for itemindex, items in enumerate(zip(left, right)):
            litem, ritem = items

            res = compare(litem, ritem)
            if res < 0:
                print("correct order")
                result += index+1
                break
            elif res > 0:
                print("wrong order")
                break
            else:
                print("same")
        print("Checking after group")
        if res == 0:
            print("left is empty")
            if len(litem) < len(ritem):
                print(" correct routing")
                result += index+1
            else:
                lf = len(litem)-len(ritem)
                print("length: {}".format(lf)) '''

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
