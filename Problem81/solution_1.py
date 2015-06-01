"""
Path sum: two ways
Problem 81

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.

link: https://projecteuler.net/problem=81

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.
"""

def int_triangle(data):
	return [[int(x) for x in y.split(',')] for y in [x for x in data.split('\n')]]
#derived from class tree in problem67
class grid(object):
	def __init__(self, data):
		self.data = data
		self.index = (0, 0) #y, x
		self.bestways = {(0, 0):[(0, 0)]} #best way for that point! index:route
		self.sums = {}
		self.routes = []
	def solution(self):
		self.search()
		return min(self.calcroute(route) for route in self.routes)
	def calcroute(self, route):
		return sum([self.data[y][x] for y, x in route])
	def num(self, index):
		y, x = index
		return self.data[y][column]
	def search(self): 
		for y in range(len(self.data)):
			for x in range(len(self.data)):
				if (x + y) == 0:
					continue
				self.index = (y, x)
				self.decise()
	def insert_route(self, last):
		newroute = self.bestways[last] + [self.index]
		self.bestways[self.index] = newroute
		self.sums[self.index] = self.calcroute(newroute)
		if len(newroute) == len(self.data) *2 - 1:
			self.routes.append(newroute)
	def decise(self):
		y, x = self.index
		if x == 0:
			last = ((y - 1), x)	 #left extrem of the tree, it's just possible to walk by left
		elif y == 0:
			last = (y, (x - 1))  #right extrem of the tree , it's just possible to walk by right
		else:
			up = (y , (x - 1)) 
			left = ((y-1) , x)
			if self.sums[up] < self.sums[left]:
				last = up
			else:
				last = left
		self.insert_route(last)

test = [[131, 673, 234, 103, 18],
		[201, 96, 342, 965, 150],
		[630, 803, 746, 422, 111],
		[537, 699, 497, 121, 956],
		[805, 732, 524, 37, 331]]
#2427 é o mínimo
f = open('p081_matrix.txt', 'r')
data = int_triangle(f.read()[:-1])
g = grid(data)
print(g.solution())
f.close()