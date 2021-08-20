#importing factorial function from math
from math import factorial

#time module for execution time calculation
import time

#time at the start of execution
start = time.time()

#creating a list with the digits of factorial
a = list(str(factorial(100)))

#converting the string to int
a = [int(x) for x in a]

#sum of the numbers
#factorial digit sum(fds)
fds = sum(a)

#time at the end of execution
end = time.time()

#print execution time and the solution
print 'Found {} in {} seconds'.format(fds,end-start)