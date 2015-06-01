#Good Solution found on forum thread in the projecteuler

def divisors(x):
    '''
    exponents(28) --> 6 because 28 = 2**2 * 7*1 --> total number of divisors of 28: (2+1)*(1+1) = 6
    '''
    expList = []
    count = 0
    divisor = 2
    while divisor <= x: 
        while x%divisor == 0:
            x = x/divisor
            count += 1
        if count != 0: 
            expList.append(count+1)
        divisor += 1
        count = 0
    return reduce(lambda x, y: x * y, expList, 1)

#Find the first triangle number to have over n divisors
def diviTri(n):
    '''
    Triangle numbers = sum of all previous the natural numbers
    Ex: The 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28
    The first triangular number to have over 5 divisors is 28, whose divisors are 1, 2, 4, 7, 14, 28
    '''
    start = timeit.default_timer()
    
    natural = 1
    triangular = 0

    while True:
        triangular += natural
        natural += 1 
        if divisors(triangular) > n:
            stop = timeit.default_timer(); print "Elapsed:", stop - start
            break
    print "First triangular number to have over", n, "divisors:",  triangular

