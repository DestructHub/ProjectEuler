#coding=utf-8
"""
Lattice paths
Problem 15

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""
#answer: 137846528820
#c(40,20) = 40!/20!20!
def pascal(n):
	line = [1]
	lines = 0
	while lines < n:
		i = 0
		newline = [1, 1]
		while len(newline) -1 <= lines and len(line) - 1 > i:
			new = line[i] + line[i + 1] 
			newline.insert(i + 1, new)
			i += 1
		line = newline
		lines += 1
		#yield ' '.join([str(x) + ' ' for x in line])
	return line
		
p = pascal(20)
for x in p:
	print x



