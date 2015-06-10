#coding=utf-8
#search the biggest sum nums adjacent on the row of the triangle below
#python3.4
#need a more efficient algorithm to search the biggest sum in a row in the tree binary.
#The maxarrow function search for or all routes, and the tree as been 100 lines, than have 2 ^ 100 routes! 
#Obviouslly, not is possible use this to solution that problem.
#It's not possible to trying all routes, it's take veryyyyyyyyyyyyy long time. 
#I used OO concept to construct a clever method! :D

def int_triangle(data):
	return [[int(x) for x in y.split()] for y in [x for x in data.split('\n')]]

class tree(object):
	def __init__(self, data):
		self.data = data
		self.index = (0, 0) #y, x
		self.bestways = {(0, 0):[(0, 0)]} #best way for that point! index:route
		self.sums = {}
		self.routes = []
	def solution(self):
		self.search()
		return max(self.calcroute(route) for route in self.routes)
	def calcroute(self, route):
		return sum([self.data[y][x] for y, x in route])
	def num(self, index):
		y, x = index
		return self.data[y][column]
	def search(self): 
		for y in range(1, len(self.data)):
			for x in range(y + 1):
				self.index = (y, x)
				self.decise()
	def insert_route(self, last):
		newroute = self.bestways[last] + [self.index]
		self.bestways[self.index] = newroute
		self.sums[self.index] = self.calcroute(newroute)
		if len(newroute) == len(self.data):
			self.routes.append(newroute)
	def decise(self):
		y, x = self.index
		if x == y:	
			last = ((y - 1), (x - 1)) #left extrem of the tree, it's just possible to walk by left
		elif x == 0:
			last = ((y - 1), x)  #right extrem of the tree , it's just possible to walk by right
		else:
			left = ((y - 1), (x - 1)) 
			right = ((y - 1), x)
			if self.sums[left] > self.sums[right]:
				last = left
			else:
				last = right

		self.insert_route(last)
if __name__ == '__main__':
	f = open('p067_triangle.txt')
	data = int_triangle(f.read()[:-1])
	t = tree(data)
	print(t.solution())