import tools as tools
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.finder.dijkstra import DijkstraFinder

today="12"

inputfile="input."+today



def puzzle_01():
    inputdata = tools.helper.read_input(inputfile)
    matrix=[list(x) for x in inputdata]
    #  print(grid)
    for r, row in enumerate(matrix):
        for c,col in enumerate(row):
            if col=="S":
                startr=r
                startc=c
                matrix[r][c]="a"
                
            elif col=="E":
                endr=r
                endc=c
                matrix[r][c]="z"
            matrix[r][c]=ord(matrix[r][c])
    
    #matrix = [  [1, 1, 1],  [1, 0, 1],  [1, 1, 1]]
    grid = Grid(matrix=matrix)

    start = grid.node(startr, startc)
    end = grid.node(5,2)

    finder = DijkstraFinder(diagonal_movement=DiagonalMovement.never)
    #(diagonal_movement=DiagonalMovement.always)
    #finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
    path, runs = finder.find_path(start, end, grid)

    print('operations:', runs, 'path length:', len(path))
    print(grid.grid_str(path=path, start=start, end=end))
    
    result=0
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
#puzzle_02()
print("-------------------------------")
