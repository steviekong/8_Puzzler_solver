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
	def _init_(self, state, parent, depth, path_cost, children):
		self.state = state
		self.parent = parent
		self.depth = depth
		self.path_cost = path_cost
		self.chidren = chidren

	def generate_child_nodes():
		return 1

	def is_goal(self):
		goal = [[0],[1],[2],[3],[4],[5],[6],[7],[8]]
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
	print(strategy_to_array(path))


def strategy_to_array(path):
	board = []
	i = 0; 
	with open(path, 'r') as openFile:
			for line in openFile.read().splitlines():
				for number in line.split(' '):
					board.append([])
					if number == '.':
						board[i].append(0)
					else: 
						board[i].append(int(number))
					i+=1
	return board; 


process_args();


