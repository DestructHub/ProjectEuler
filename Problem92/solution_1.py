#coding=utf-8
"""
Square digit chains
Problem 92

A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""
#answer: 8581146  
#primeiro algoritmo:230s+- (brute-force super simples)
#outra versão usando lista = 314s #
#usando dic(atual): 65s

def sequence_end(n, finalnum):
	start = 0
	dic = {}
	end_count = 0
	while start +1 < n:
		start += 1
		if start in dic:
			if dic[start] == finalnum:
				end_count += 1 
				continue
			else:
				continue
		end = start
		nums = [end]
		while end != 1 and end != 89:
			end = sum(map(lambda x: x * x, (int(x) for x in str(end))))
			if end in dic:
				end = dic[end]
				break
			else:
				nums.append(end)

		for num in nums:
			dic[num] = end

		if end == finalnum:
			end_count += 1

	return end_count

total = sequence_end(10 ** 7, 89)
print(total)