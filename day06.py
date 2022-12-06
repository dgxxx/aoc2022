from tools import config, log,helper
today="6"

inputfile="input."+today

def checkmarker(window):
    res=False

    return res
def puzzle_01():
    inputdata = helper.read_input(inputfile)[0]
    result=0
    c=0
    #print(inputdata)
    max=len(inputdata)-3
    windowsize=4
    while c<max:

        window=inputdata[c:c+4]
        #print(len(window))
        #print(len(set(window)))
        print("w: {} l: {} s: {}".format(window,len(window),len(set(window))))
        if len(set(window))==windowsize:
            print("found window: {}".format(window))
            result=c+4
            break
        c+=1
    print("Puzzle-1: Result: {}".format(result))



def puzzle_02():

    inputdata = helper.read_input(inputfile)[0]
    result=0
    c=0
    windowsize=14
    #print(inputdata)
    max=len(inputdata)-14
    while c<max:

        window=inputdata[c:c+windowsize]
        #print(len(window))
        #print(len(set(window)))
        print("w: {} l: {} s: {}".format(window,len(window),len(set(window))))
        if len(set(window))==windowsize:
            print("found window: {}".format(window))
            result=c+windowsize
            break
        c+=1
    
    print("Puzzle-2: Result: {}".format(result))


print("-------------------------------")
print("Day {} Results".format(today))
print("-------------------------------")
puzzle_01()
print("-------------------------------")
puzzle_02()
print("-------------------------------")
