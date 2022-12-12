import tools as tools

today="12"

inputfile="input."+today
grid=[]

def find_shortest():
    #maze = tools.maze.create_wall_maze( 20, 12 )
    maze = tools.maze.create_aoc_maze( grid )
    
    filled = tools.pathfinder.fill_shortest_path(maze.board, maze.start, maze.end)
    path=tools.pathfinder.backtrack_to_start(filled, maze.end)
    result=filled.at(maze.end).count
    finder = tools.draw.Finder()
    finder.set_path(path)
    finder.set_board(filled)
    finder.run()
    return result
def puzzle_01():
    inputdata = tools.helper.read_input(inputfile)
    for row in inputdata:
        l=[]
        for c in row:
            l.append(c)
        grid.append(l)
        
    result=find_shortest()

    print("Puzzle-1: Result: {}".format(result))



def puzzle_02():

    inputdata = tools.helper.read_input(inputfile)
    result=0
    
    print("Puzzle-2: Result: {}".format(result))


print("-------------------------------")
print("Day {} Results".format(today))
print("-------------------------------")
puzzle_01()
print("-------------------------------")
puzzle_02()
print("-------------------------------")
