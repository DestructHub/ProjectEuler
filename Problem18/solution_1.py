#search the biggest sum nums adjacent on the row of the triangle below
#python3.4
triangle = '''\
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''


def int_triangle(data):
	return [[int(x) for x in y.split()] for y in [x for x in data.split('\n')]]

def arrows_recursive(data, total = [], main = [], x = 0, y = 0):
	temp = [] + main
	if x < len(data) and y < len(data):
		temp.append(data[y][x])
		total = arrows_recursive(data, total = total, main = temp, x = x, y = y + 1)
		total = arrows_recursive(data, total = total, main = temp, x = x + 1, y = y + 1)
	if len(temp) >= len(data):
		total.append(temp)	
	return total

if __name__ == '__main__':
	lista = int_triangle(triangle)
	p = arrows_recursive(lista)
	print(max(map(sum, p)))

