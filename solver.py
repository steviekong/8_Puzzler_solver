import numpy;
import sys;
from array import *; 


def bfs(startNode):
 	return 0

def ucs(startNode):
	return 0

def gbf(startNode):
	return 0
def heuristicSearch(startNode):
	return 0

class node:
	def __init__(self, state, parent, depth, path_cost, children):
		self.state = state
		self.parent = parent
		self.depth = depth
		self.path_cost = path_cost
		self.children = children

	def generate_child_nodes():
		return 1

	def find_zero(self):
		for i, e in enumerate(self.state):
			try:
				return i, e.index(0)
			except:
				pass


	def is_goal(self):
		goal = [[0, 1, 2],[3, 4, 5],[6, 7, 8]]
		return self.state == goal

def process_args():
	strategy = ''
	path = ''
	try:
		strategy = str(sys.argv[1])
		path = str(sys.argv[2])
		print (strategy + " " + path)
	except:
		print("Invalid Input: The correct way to run the program is \"python solver.py strategy path\"")

	'''if strategy == 'bfs':
		bfs()
	elif strategy == 'ucost':
		ucs()
	elif strategy == 'greedy':
		gbf()
	else:
		heuristicSearch()
	'''
	print(strategy_to_array(path).find_zero())


def strategy_to_array(path):
	board = []
	i = 0; 
	j = 0;
	with open(path, 'r') as openFile:
			for line in openFile.read().splitlines():
				board.append([])
				for number in line.split(' '):
					if number == '.':
						board[i].append(int(0))
						j += 1
					else: 
						board[i].append(int(number))
						j += 1
					if j == 3:
						j = 0
						i += 1
	return node(board, None, 0, 0, None)


process_args();


