import tools as tools

today="12"

inputfile="input."+today


def find_starts(grid):
    startingpoints=[]
    for i,y in enumerate(grid) :
        for j,x in enumerate(y):
            if x=="a":
                startingpoints.append([j,i])
    return startingpoints
    
def find_shortest(matrix,point=None):
    #maze = tools.maze.create_wall_maze( 20, 12 )
    maze = tools.maze.create_aoc_maze( matrix ,point)
    
    filled = tools.pathfinder.fill_shortest_path(maze.board, maze.start, maze.end)
    #path=tools.pathfinder.backtrack_to_start(filled, maze.end)
    result=filled.at(maze.end).count
    #finder = tools.draw.Finder()
    #finder.set_board(filled)
    # finder.run()
    return result
def puzzle_02():
    grid=[]
    inputdata = tools.helper.read_input(inputfile)
    for row in inputdata:
        l=[]
        for c in row:
            l.append(c)
        grid.append(l)
    res=[]
    startingpoints=find_starts(grid)
    #print(grid)
    #print(startingpoints)
    #print(find_shortest(grid))
    #print(grid)
    #print(find_shortest(grid))
    #exit()
    for point in startingpoints:
        print(point)
        count=find_shortest(grid,point)
        print(count)
        res.append(count)
    print(res)
    res.sort()
    result=res[0]

    print("Puzzle-2: Result: {}".format(result))





print("-------------------------------")
print("Day {} Results".format(today))
print("-------------------------------")
puzzle_02()
print("-------------------------------")
