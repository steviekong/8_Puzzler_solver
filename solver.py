import numpy;
import sys;
from array import *; 
import copy; 
from queue import *
from heapq import *

class node:
	def __init__(self, state, parent, depth, path_cost, children, self_cost):
		self.state = state
		self.parent = parent
		self.depth = depth
		self.path_cost = path_cost
		self.children = children
		self.self_cost = self_cost

	def find_zero(self):
		for i, e in enumerate(self.state):
			try:
				return i, e.index(0)
			except:
				pass

	def left_move_child(self, i, j, child_list):
			if(j-1 >= 0):
				temp = copy.deepcopy(self.state)
				temp[i][j-1], temp[i][j] = temp[i][j], temp[i][j-1]
				child_list.append(node(temp, self, self.depth+1, self.path_cost+temp[i][j],None,temp[i][j])) 

	def right_move_child(self, i, j, child_list):
			if(j+1 <= 2):
				temp = copy.deepcopy(self.state)
				temp[i][j+1], temp[i][j] = temp[i][j], temp[i][j+1]
				child_list.append(node(temp, self, self.depth+1, self.path_cost+temp[i][j],None,temp[i][j]))

	def up_move_child(self, i, j, child_list):
			if(i-1 >= 0):
				temp = copy.deepcopy(self.state)
				temp[i-1][j], temp[i][j] = temp[i][j], temp[i-1][j]
				child_list.append(node(temp, self, self.depth+1, self.path_cost+temp[i][j],None,temp[i][j]))

	def down_move_child(self, i, j, child_list):
			if(i+1 <= 2):
				temp = copy.deepcopy(self.state)
				temp[i+1][j], temp[i][j] = temp[i][j], temp[i+1][j]
				child_list.append(node(temp, self, self.depth+1, self.path_cost+temp[i][j],None,temp[i][j]))

	def generate_child_nodes(self):
		i, j = self.find_zero()

		child_list = []

		self.left_move_child(i, j, child_list)
		self.right_move_child(i, j, child_list)
		self.up_move_child(i, j, child_list)
		self.down_move_child(i, j, child_list)
		self.children = child_list


	def is_goal(self):
		goal = [[0, 1, 2],[3, 4, 5],[6, 7, 8]]
		return self.state == goal

def manhattanDistance(s_1, s_2):

	return

def gbf(start_node):
	frontier = Queue()
	explored = Queue()
	frontier.put(start_node)
	frontier_count = 0 
	expanded_count = 0

	while(not frontier.empty()):
		node = frontier.get()
		if node.is_goal():
			return node, node.path_cost, frontier_count, expanded_count
		explored.put(node)
		node.generate_child_nodes()
		expanded_count += 1
		for n in node.children:
			if n not in frontier.queue and n not in explored.queue :
				frontier_count += 1
				frontier.put(n)


def ucs(start_node):
	frontier = []
	explored = Queue()
	heappush(frontier, (0, id(start_node), start_node))
	frontier_count = 0 
	expanded_count = 0

	while(frontier):
		node = heappop(frontier)[2]
		if node.is_goal():
			return node, node.path_cost, frontier_count, expanded_count
		explored.put(node)
		node.generate_child_nodes()
		expanded_count += 1
		for n in node.children:
			if not any(x[2].state == n.state for x in frontier) and not any(x.state == n.state for x in explored.queue):
				heappush(frontier, (n.path_cost ,id(n), n))
				frontier_count += 1

def bfs(start_node):
	frontier = Queue()
	explored = Queue()
	frontier.put(start_node)
	frontier_count = 1 
	expanded_count = 0

	while(not frontier.empty()):
		node = frontier.get()
		explored.put(node)
		node.generate_child_nodes()
		expanded_count += 1
		for n in node.children:
			if not any(x.state == n.state for x in frontier.queue) and not any(x.state == n.state for x in explored.queue):
				if n.is_goal():
					return n, n.path_cost, frontier_count, expanded_count
				else:
					frontier_count += 1
					frontier.put(n)
def print_node(n):
	for i in range(len(n.state)):
		line = ""
		for j in range(len(n.state[i])):
			if n.state[i][j] is not 0:
				line += str(n.state[i][j])+" "
			else:
				line += ". "
		print(line)
		line = ""
	print("")

def print_results(algorithm, start_node):
	results = algorithm(start_node)
	curr = results[0]
	stack = []
	while(curr is not None):
		stack.append(curr)
		curr = curr.parent

	while(stack):
		print_node(stack.pop())

	print("path cost: "+str(results[1]))
	print("frontier: "+str(results[2]))
	print("expanded: "+str(results[3]))


def process_args():
	strategy = ''
	path = ''
	try:
		strategy = str(sys.argv[1])
		path = str(sys.argv[2])
	except:
		print("Invalid Input: The correct way to run the program is \"python solver.py strategy path\"")

	if strategy == 'bfs':
		print_results(bfs, strategy_to_array(path))
	elif strategy == 'ucost':
		print_results(ucs, strategy_to_array(path))
		'''
	elif strategy == 'greedy':
		gbf()
	else:
		heuristicSearch()
	'''


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
	return node(board, None, 0, 0, None, 0)


process_args();


