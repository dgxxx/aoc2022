from tools import config, log,helper
today="8"

inputfile="input."+today
field=[]
f={}

def genv(f):
    matrixsize=len(f)
    v={}
    for l in range(0,matrixsize):
        v[l]={}
        for r in range(0,matrixsize):
            v[l][r]=0
    return v
def pr(d):

    for i in range(0,len(d)):
        
        for j in range(0,len(d[i])):
            print("{}".format(d[i][j]), end=" ")
            #print(i,j)
        print()

def puzzle_01():
    inputdata = helper.read_input(inputfile)
    #matrix = [list(map(int, line)) for line in inputdata]
    matrix=[]
    for line in inputdata:
        matrix.append(list(map(int,line)))
    visibility=genv(matrix)

    result=0
    #pr(matrix)
    for r in range(0,len(matrix)):
        for c in range(0,len(matrix[r])):
            v=0
            k = matrix[r][c]
            if (all(matrix[r][x] < k for x in range(c))):
                visibility[r][c]=1
                v=1
            elif (all(matrix[r][x]< k for x in range(c+1,len(matrix[r])))):
                visibility[r][c]=1
                v=1 
            elif (all(matrix[x][c] < k for x in range(r))):
                visibility[r][c]=1
                v=1 
            elif (all(matrix[x][c]< k for x in range(r+1,len(matrix)))):
                visibility[r][c]=1
                v=1 
            result+=v
    print("-----------------")
    #pr(visibility)


    print("Puzzle-1: Result: {}".format(result))

def puzzle_02():

    inputdata = helper.read_input(inputfile)
    #matrix = [list(map(int, line)) for line in inputdata]
    matrix=[]
    for line in inputdata:
        matrix.append(list(map(int,line)))
    visibility=genv(matrix)

    result=0
    #pr(matrix)
    for r in range(0,len(matrix)):
        for c in range(len(matrix[r])):
            v=0
            k = matrix[r][c]
            L=R=T=B=0
            # to left
            for x in range(c-1,-1,-1):
                L+=1
                if matrix[r][x]>=k:
                    break
        # to right
            for x in range(c+1,len(matrix[r])):
                R+=1
                if matrix[r][x]>=k:
                    break
        # to top
            for x in range(r-1,-1,-1):
                T+=1
                if matrix[x][c]>=k:
                    break
            
        # to bottom
            for x in range(r+1,len(matrix)):
                B+=1
                if matrix[x][c]>=k:
                    break
            score=L*R*T*B
            if result < score:
                result=score
    print("-----------------")
    #pr(visibility)
    print("Puzzle-2: Result: {}".format(result))


print("-------------------------------")
print("Day {} Results".format(today))
print("-------------------------------")
puzzle_01()
print("-------------------------------")
puzzle_02()
print("-------------------------------")
