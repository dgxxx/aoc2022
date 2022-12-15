from tools import config, log, helper
import tools
import time
import os
today = "14"

inputfile = "input."+today


class pointClass():
    def __init__(self, x, y):
        self.x = x
        self.y = y


def pr(d):
    os.system("clear")
    for i in d:

        for j in d[i]:

            print("{}".format(d[i][j]), end=" ")
            # print(i,j)
        print()
    print("--------------------------------------")


def puzzle_02():
    inputdata = helper.read_input(inputfile)
    result = 0
    mx = 0
    lx = 20000
    my = 0
    for i in inputdata:
        xh = max([list(map(int, point.split(",")))[0]
                 for point in i.split(" -> ")])
        y = max([list(map(int, point.split(",")))[1]
                 for point in i.split(" -> ")])
        xl = min([list(map(int, point.split(",")))[0]
                 for point in i.split(" -> ")])

        if xh > mx:
            mx = xh
        if xl < lx:
            lx = xl
        if y > my:
            my = y
    #print(lx, mx, my)

    abyss = my+2
    print("Abyss: {}".format(abyss))
    input("Press Enter to continue...")
    # print(max(map(int, i.split(",")) for i in inputdata.split(" -> ")))

    grid = {}
    #abyss = 0
    for y in range(my+5):
        grid[y] = {}
        for x in range(lx-300, mx+300):

            grid[y][x] = "."
    grid[0][500] = "+"
    for x in grid[abyss]:
        grid[abyss][x] = "#"
    for path in inputdata:

        points = [list(map(int, point.split(",")))
                  for point in path.split(" -> ")]
        # print(points)
        # pr(grid)

        for n in range(len(points)-1):
            # print(
            #    " {}:{} - {}:{}".format(points[n][0], points[n][1], points[n+1][0], points[n+1][1]))
            if points[n][0] == points[n+1][0]:
                #print("y range")
                if points[n][1] > points[n+1][1]:
                    step = -1
                else:
                    step = 1
                for m in range(points[n][1], points[n+1][1]+step, step):
                    # print(m)
                    grid[m][points[n][0]] = "#"
                    # pr(grid)
            elif points[n][1] == points[n+1][1]:
                #print("x range")
                if points[n][0] > points[n+1][0]:
                    step = -1
                else:
                    step = 1
                #print(points[n][0], points[n+1][0])
                for m in range(points[n][0], points[n+1][0]+step, step):
                    # print(m)
                    grid[points[n][1]][m] = "#"
                    # pr(grid)
        # grid is defined
        # now start with sand
    input("Press Enter to continue...")
    sandcorn = 0
    finished = False
    #print("Going to abyss:{}".format(abyss))
    while not finished:
        sandcorn += 1
        sandcornstatus = True
        posx = 500
        posy = 0
        oposx = 500
        oposy = 0
        #print(posx, posy)
        grid[0][500] = "+"
        while sandcornstatus:

            #print(posx, posy, abyss)

            if grid[posy+1][posx] == ".":
                grid[posy+1][posx] = "o"
                grid[posy][posx] = "."
                grid[0][500] = "+"
                posy += 1
                #grid[oposy][oposx] = "."
            elif grid[posy+1][posx] != ".":
                if grid[posy+1][posx+1] != "." and grid[posy+1][posx-1] != ".":
                    grid[posy][posx] = "o"
                    sandcornstatus = False
                    #input("Press Enter to continue...")
                elif grid[posy+1][posx-1] == ".":
                    grid[posy][posx] = "."
                    posy += 1
                    posx -= 1

                    grid[posy][posx] = "o"
                elif grid[posy+1][posx+1] == ".":
                    grid[posy][posx] = "."

                    posy += 1
                    posx += 1
                    grid[posy][posx] = "o"
            # pr(grid)
            # time.sleep(0.05)
            if posy == 0:
                print("Abyss reached with {} sandcorns".format(sandcorn-1))
                result = sandcorn
                finished = True
                sandcornstatus = False

    print("Puzzle-2: Result: {}".format(result))


print("-------------------------------")
print("Day {} Results".format(today))
print("-------------------------------")
# puzzle_01()
print("-------------------------------")
puzzle_02()
print("-------------------------------")
