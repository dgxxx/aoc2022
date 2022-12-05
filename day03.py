from tools import config, log,helper
today="3"

inputfile="input."+today

def prio(c):
    if c.isupper():
        prio=ord(c)-38
    else:
        prio=ord(c)-96
    return prio

def puzzle_01():
    inputdata = helper.read_input(inputfile)
    result=0
    

    for item in inputdata:

        x=len(item)
        h=int(x/2)
        compartment1,compartment2=item[:h],item[h:]

        commonDict = set(compartment1) & set(compartment2)
       
        if len(commonDict) > 0:
            commonChar = list(commonDict)[0]
            p=prio(commonChar)
            result+=p
            
    print("Puzzle-1: Result: {}".format(result))



def puzzle_02():

    inputdata = helper.read_input(inputfile)
    result=0
    counter=0
    while counter<len(inputdata):
        set1=inputdata[counter]
        set2=inputdata[counter+1]
        set3=inputdata[counter+2]
        counter+=3
        s1=set(set1)
        s2=set(set2)
        s3=set(set3)
        commonDict=s1&s2&s3

        c=list(commonDict)[0]
        p=prio(c)
        result+=p

    print("Puzzle-2: Result: {}".format(result))


print("-------------------------------")
print("Day {} Results".format(today))
print("-------------------------------")
puzzle_01()
print("-------------------------------")
puzzle_02()
print("-------------------------------")
