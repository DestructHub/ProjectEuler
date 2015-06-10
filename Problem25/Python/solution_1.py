#How the term of the first 1000-digit number in the fibonacci sequence?
#answer: 4782
def fib(max_lenght):
	a, b = 1, 1
	term = 1
	while len(str(a)) < max_lenght:
		term += 1
		a, b = b, a + b
	return term
print(fib(1000))