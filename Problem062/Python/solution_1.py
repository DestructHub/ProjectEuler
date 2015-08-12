#coding=utf-8
"""
Cubic permutations
Problem 62

The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""

def cubesGen(n, start = 1):
	return map(lambda x: str(x*x*x), range(start, n + 1))

def getId(n):
	return sum([2 ** int(x) for x in n]) * sum([int(x) for x in list(n)])
def isPerm(a, b):
	for i in a:
		for j in b:
			if i not in b or j not in a:
				return False
	return getId(a) == getId(b)

def cubeRoot(n):
	return int(n ** (1/3) + 0.00001)

def mostCube(n):
	most = int(''.join(sorted(n, reverse = True)))
	return cubeRoot(most)
def lowerCube(n):
	lower = int(''.join(sorted(n)))
	return cubeRoot(lower)

#my_solution... after much hard work the results final is this... i want to break free XD
def problem62(max):
	maxCube = 10 ** 15
	for cube_a in cubesGen(maxCube):
		permCubes = 0
		for cube_b in cubesGen(int(mostCube(cube_a)), start = int(lowerCube(cube_a))):
			if isPerm(cube_a, cube_b):
				permCubes += 1
		if permCubes == max:
			print('Answer: ' %cube_a)
			return


#the solution of one guy, much more efficient.
def main2():
	from time import time

	def cubes():
		i = 1
		while True:
			yield i * i * i
			i += 1

	start = time()
	cube_dict = {}
	for c in cubes():
		digits = ''.join(sorted(str(c)))
		if digits in cube_dict:
			cube_list = cube_dict[digits]
			cube_list.append(c)
			if(len(cube_list)) == 5:
				print('Found solution {} in {} seconds'.format(cube_list, time() - start))
				print(min(cube_list))
				break
		else:
			cube_dict[digits] = [c]


main2()
#problem62()

#wrong answer: 1000600120008 (because its included the self number, this answer contain 6 permutations)
#correct answer: 127035954683 (5 permutations!)