import math, random, types, copy
from enum import Enum

class CellType(Enum):
	Empty = 1
	Block = 2
	
class CellMark(Enum):
	No = 0
	Start = 1
	End = 2
	
class Cell:
	def __init__(self, type = CellType.Empty, pos = None, weight=0):
		self.type = type
		self.weight = weight
		self.count = 0
		self.mark = CellMark.No
		self.path_from = None
		self.pos = pos

		
class CellGrid:
	def __init__(self, board):
		self.board = board

	def get_size(self):
		return [len(self.board), len(self.board[0])]
		
	def at(self, pos):
		return self.board[pos[0]][pos[1]]
		
	def clone(self):
		return CellGrid( copy.deepcopy(self.board) )
		
	def clear_count(self, count):
		for o in self.board:
			for i in o:
				i.count = count
				i.path_from = None

	def is_valid_point(self, pos):
		sz = self.get_size()
		return pos[0] >= 0 and pos[1] >= 0 and pos[0] < sz[0] and pos[1] < sz[1]
 
def findgrid(grid,s):
	for i,r in enumerate(grid):
		#print(r,index)
		#print (r,s)
		try:
			x=r.index(s)
			y=i
			#print("found: {},{}".format(x,y)) 
			return x,y
		except:
			continue
def create_aoc_maze( matrix,startingpoint=None ):
	y=len(matrix)
	x=len(matrix[0])
	if startingpoint:
		startx = startingpoint[0]
		starty = startingpoint[1]
		print(startingpoint,startx,starty)
	else:
		startx,starty=findgrid(matrix,"S")
	#print(startx,starty)
	#matrix[starty][startx]="a"
	endx,endy=findgrid(matrix,"E")
	#print(endx,endy)
	#print(matrix)
	#print(matrix[endy][endx])
	#matrix[endy][endx]="z"
	m2=[]
	
	for i,c in enumerate(matrix):
		m=[]
		for j,r in enumerate(c):
			#print(i,j)
			if r=="E":
				m.append(ord("z")-97)
			elif r=="S":
				m.append(ord("a")-97)
			else:
				m.append(int(ord(matrix[i][j])-97))
		m2.append(m)
    
	return types.SimpleNamespace( 
		board = CellGrid( [[Cell(type = CellType.Empty, pos=[ix,iy], weight=m2[iy][ix]) for iy in range(y)] for ix in range(x)] ),
		start = [startx, starty],
		end = [endx, endy])
	
def create_wall_maze( x, y ):
	board = [[Cell(type = CellType.Empty, pos=[ix,iy]) for iy in range(y)] for ix in range(x)]
	for i in range(0,x):
		board[i][int(y/2)].type = CellType.Block
	for i in range(0,y):
		board[int(x/2)][i].type = CellType.Block
		
	board[random.randint(0,x/2-1)][int(y/2)].type = CellType.Empty
	board[random.randint(x/2+1,x-1)][int(y/2)].type = CellType.Empty
	board[int(x/2)][random.randint(0,y/2-1)].type = CellType.Empty
	board[int(x/2)][random.randint(y/2+1,y-1)].type = CellType.Empty
	
	return types.SimpleNamespace( board = CellGrid(board),
		start = [random.randrange(0,x/2), random.randrange(y/2+1,y)],
		end = [random.randrange(x/2+1,x), random.randrange(0,y/2)] )
	

def add_point(a,b):
	return [a[0] + b[0], a[1] + b[1]]
